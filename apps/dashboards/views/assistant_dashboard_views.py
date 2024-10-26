#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: assistant_dashboard_views.py
#  Last Modified: 2024-10-25 20:50:22
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:50:23
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
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from apps.chats.models import MultimodalAssistantChat, MultimodalAssistantChatMessage
from web_project import TemplateLayout


class DashboardView_Assistant(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['available_chats'] = MultimodalAssistantChat.objects.all()
        chat_id = self.request.GET.get('chat_id')
        if chat_id:
            selected_chat = get_object_or_404(MultimodalAssistantChat, id=chat_id)
            context['selected_chat'] = selected_chat
            context['chat_messages'] = MultimodalAssistantChatMessage.objects.filter(chat=selected_chat).order_by(
                'sent_at')
        else:
            context['selected_chat'] = None
            context['chat_messages'] = None

        return context

    def post(self, request, *args, **kwargs):
        chat_id = request.POST.get('chat_id')
        message_text = request.POST.get('message_content')
        attached_files = request.FILES.getlist('attached_file')
        attached_images = request.FILES.getlist('attached_image')

        if not chat_id or not message_text:
            messages.error(request, "Please provide a chat ID and a message.")
            return redirect('dashboards:assistant_dashboard')

        chat = get_object_or_404(MultimodalAssistantChat, id=chat_id)
        file_uris = []
        for attached_file in attached_files:
            file_name = default_storage.save(f'chat_files/{attached_file.name}', ContentFile(attached_file.read()))
            file_uris.append(default_storage.url(file_name))

        image_uris = []
        for attached_image in attached_images:
            image_name = default_storage.save(f'chat_images/{attached_image.name}', ContentFile(attached_image.read()))
            image_uris.append(default_storage.url(image_name))

        MultimodalAssistantChatMessage.objects.create(
            chat=chat, message_role='user', message_text=message_text, message_file_uris=file_uris,
            message_image_uris=image_uris
        )

        chat_messages = MultimodalAssistantChatMessage.objects.filter(chat=chat).order_by('sent_at')
        chat_history = [
            {"role": msg.message_role, "content": msg.message_text} for msg in chat_messages
        ]

        endpoint = chat.connection.connection_endpoint
        api_key = chat.connection.connection_api_key
        if "Bearer" not in api_key:
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
                    MultimodalAssistantChatMessage.objects.create(
                        chat=chat, message_role='assistant', message_text=assistant_message
                    )
            else:
                messages.error(request, "There has been an error while sending the message: "
                                        f"{response_data.get('message', '')}")
        except requests.RequestException as e:
            messages.error(request, f"Error while sending the message: {e}")

        messages.success(request, "Message sent successfully.")
        return redirect(f"{request.build_absolute_uri('/dashboards/assistant/')}?chat_id={chat_id}")
