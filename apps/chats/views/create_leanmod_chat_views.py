#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_leanmod_chat_views.py
#  Last Modified: 2024-10-25 20:24:02
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:42:09
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

from apps.chats.models import MultimodalLeanmodChat
from apps.connections.models import LeanmodConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ChatView_LeanmodCreate(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['connections'] = LeanmodConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        connection_id = request.POST.get('connection')

        if not connection_id:
            messages.error(request, "Please select a LeanMod connection.")
            return redirect('chats:leanmod_create')

        try:
            connection = LeanmodConnection.objects.get(id=connection_id)

        except LeanmodConnection.DoesNotExist:
            messages.error(request, "Selected LeanMod connection does not exist.")
            return redirect('chats:leanmod_create')

        chat = MultimodalLeanmodChat(
            uuid=str(uuid.uuid4()),
            connection=connection
        )
        chat.save()

        messages.success(request, "LeanMod Chat instance created successfully.")
        return redirect('chats:leanmod_create')
