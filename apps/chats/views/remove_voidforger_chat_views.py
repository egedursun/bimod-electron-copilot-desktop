#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: remove_voidforger_chat_views.py
#  Last Modified: 2024-11-25 00:49:45
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-25 00:49:45
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.chats.models import MultimodalVoidForgerChat
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ChatView_VoidForgerRemove(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['chats'] = MultimodalVoidForgerChat.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        chat_id = request.POST.get('chat_id')

        if not chat_id:
            messages.error(request, "No chat ID provided.")
            return redirect('chats:voidforger_remove')

        try:
            chat = MultimodalVoidForgerChat.objects.get(id=chat_id)
            chat.delete()
            messages.success(request, "VoidForger chat instance deleted successfully.")

        except MultimodalVoidForgerChat.DoesNotExist:
            messages.error(request, "VoidForger chat instance not found.")

        return redirect('chats:voidforger_remove')
