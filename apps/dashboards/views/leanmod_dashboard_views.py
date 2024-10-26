#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: leanmod_dashboard_views.py
#  Last Modified: 2024-10-25 20:51:13
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:51:14
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
import json

import requests
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from apps.chats.models import MultimodalLeanmodChat, MultimodalLeanmodChatMessage
from web_project import TemplateLayout


class DashboardView_Leanmod(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['available_chats'] = MultimodalLeanmodChat.objects.all()
        chat_id = self.request.GET.get('chat_id')

        if chat_id:
            selected_chat = get_object_or_404(MultimodalLeanmodChat, id=chat_id)
            context['selected_chat'] = selected_chat
            context['chat_messages'] = MultimodalLeanmodChatMessage.objects.filter(chat=selected_chat).order_by(
                'sent_at')
        else:
            context['selected_chat'] = None
            context['chat_messages'] = None

        return context

    def post(self, request, *args, **kwargs):
        chat_id = request.POST.get('chat_id')
        message_text = request.POST.get('message_content')
        attached_files = request.POST.get('file_uris')
        attached_images = request.POST.get('image_uris')
        if not chat_id or not message_text:
            messages.error(request, "Please provide a chat ID and a message.")
            return redirect('dashboards:leanmod_dashboard')

        chat = get_object_or_404(MultimodalLeanmodChat, id=chat_id)
        MultimodalLeanmodChatMessage.objects.create(
            chat=chat,
            message_role='user',
            message_text=message_text,
            message_file_uris=attached_files,
            message_image_uris=attached_images
        )

        chat_messages = MultimodalLeanmodChatMessage.objects.filter(chat=chat).order_by('sent_at')
        chat_history = [
            {
                "role": msg.message_role,
                "content": msg.message_text,
                "file_uris": msg.message_file_uris,
                "image_uris": msg.message_image_uris
            }
            for msg in chat_messages
        ]

        try:
            _ = self.get_leanmod_response(chat=chat, chat_history=chat_history)
        except Exception as e:
            messages.error(request, f"Error while sending the message: {e}")
            return redirect('dashboards:leanmod_dashboard')

        messages.success(request, "Message sent successfully.")
        return redirect(f"{request.build_absolute_uri('/dashboards/leanmod/')}?chat_id={chat_id}")

    @staticmethod
    def get_leanmod_response(chat, chat_history):
        endpoint = chat.connection.connection_endpoint
        api_key = chat.connection.connection_api_key
        if api_key and "Bearer" not in api_key:
            api_key = f"Bearer {api_key}"
        headers = {"Authorization": f"{api_key}", "Content-Type": "application/json"}
        payload = json.dumps({"chat_history": chat_history})
        try:
            response = requests.post(endpoint, headers=headers, data=payload)
            response_data = response.json()
            response_data = response_data["data"]
            if response.status_code == 200:
                assistant_message = response_data.get("message", {}).get("content")
                if assistant_message:
                    MultimodalLeanmodChatMessage.objects.create(
                        chat=chat, message_role='assistant', message_text=assistant_message
                    )
            else:
                raise requests.RequestException(f"Error {response.status_code}: {response_data.get('message')}")
        except Exception as e:
            raise requests.RequestException(f"Error while sending the message: {e}")
        return response
