#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: orchestration_dashboard_views.py
#  Last Modified: 2024-10-25 20:51:32
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:51:32
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from apps.chats.models import MultimodalOrchestrationChat, MultimodalOrchestrationChatMessage
from web_project import TemplateLayout


class DashboardView_Orchestration(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['available_chats'] = MultimodalOrchestrationChat.objects.all()
        chat_id = self.request.GET.get('chat_id')

        if chat_id:
            selected_chat = get_object_or_404(MultimodalOrchestrationChat, id=chat_id)
            context['selected_chat'] = selected_chat
            context['chat_messages'] = MultimodalOrchestrationChatMessage.objects.filter(chat=selected_chat).order_by(
                'sent_at')
        else:
            context['selected_chat'] = None
            context['chat_messages'] = None

        return context

    def post(self, request, *args, **kwargs):
        chat_id = request.POST.get('chat_id')
        message_text = request.POST.get('message_content')
        attached_file = request.FILES.get('attached_file')
        attached_image = request.FILES.get('attached_image')

        if not chat_id or not message_text:
            messages.error(request, "Please select a chat and enter a message.")
            return redirect('orchestration_chat')

        chat = get_object_or_404(MultimodalOrchestrationChat, id=chat_id)
        MultimodalOrchestrationChatMessage.objects.create(
            chat=chat,
            message_role='user',
            message_text=message_text,
            message_file_uris=[attached_file.url] if attached_file else [],
            message_image_uris=[attached_image.url] if attached_image else []
        )

        messages.success(request, "Message sent successfully.")
        return redirect('orchestration_chat', chat_id=chat.id)
