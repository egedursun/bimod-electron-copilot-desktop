#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_orchestration_chat_views.py
#  Last Modified: 2024-10-25 18:41:15
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:42:20
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

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.chats.models import MultimodalOrchestrationChat
from apps.connections.models import OrchestrationConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ChatView_OrchestrationCreate(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['connections'] = OrchestrationConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        connection_id = request.POST.get('connection')

        if not connection_id:
            messages.error(request, "Please select an Orchestration connection.")
            return redirect('chats:orchestration_create')

        try:
            connection = OrchestrationConnection.objects.get(id=connection_id)

        except OrchestrationConnection.DoesNotExist:
            messages.error(request, "Selected Orchestration connection does not exist.")
            return redirect('chats:orchestration_create')

        chat = MultimodalOrchestrationChat(
            uuid=str(uuid.uuid4()),
            connection=connection
        )
        chat.save()

        messages.success(request, "Orchestration Chat instance created successfully.")
        return redirect('chats:orchestration_create')
