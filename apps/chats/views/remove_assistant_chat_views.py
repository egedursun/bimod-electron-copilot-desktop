#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: remove_assistant_chat_views.py
#  Last Modified: 2024-10-25 18:41:45
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:42:45
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
#


import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.chats.models import MultimodalAssistantChat
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ChatView_AssistantRemove(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['chats'] = MultimodalAssistantChat.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        chat_id = request.POST.get('chat_id')

        if not chat_id:
            messages.error(request, "No chat ID provided.")
            return redirect('chats:assistant_remove')

        try:
            chat = MultimodalAssistantChat.objects.get(id=chat_id)
            chat.delete()
            messages.success(request, "Chat instance deleted successfully.")

        except MultimodalAssistantChat.DoesNotExist:
            messages.error(request, "Chat instance not found.")

        return redirect('chats:assistant_remove')
