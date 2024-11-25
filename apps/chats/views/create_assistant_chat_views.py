#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_assistant_chat_views.py
#  Last Modified: 2024-10-25 19:05:07
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:41:13
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
import uuid

from django.shortcuts import redirect
from django.views.generic import TemplateView

from django.contrib import messages

from apps.chats.models import MultimodalAssistantChat
from apps.connections.models import AssistantConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ChatView_AssistantCreate(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['connections'] = AssistantConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        connection_id = request.POST.get('connection')

        if not connection_id:
            messages.error(request, "Please select a Assistant connection.")
            return redirect('chats:assistant_create')

        try:
            connection = AssistantConnection.objects.get(id=connection_id)

        except AssistantConnection.DoesNotExist:
            messages.error(request, "Selected Assistant connection does not exist.")
            return redirect('chats:assistant_create')

        chat = MultimodalAssistantChat(
            uuid=str(uuid.uuid4()),
            connection=connection
        )
        chat.save()

        messages.success(request, "Assistant Chat instance created successfully.")
        return redirect('chats:assistant_create')
