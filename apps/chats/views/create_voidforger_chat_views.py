#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_voidforger_chat_views.py
#  Last Modified: 2024-11-25 00:49:38
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-25 00:49:38
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

import uuid

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.chats.models import MultimodalVoidForgerChat
from apps.connections.models import VoidForgerConnection
from web_project import TemplateLayout


class ChatView_VoidForgerCreate(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['connections'] = VoidForgerConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        connection_id = request.POST.get('connection')

        if not connection_id:
            messages.error(request, "Please select a VoidForger connection.")
            return redirect('chats:voidforger_create')

        try:
            connection = VoidForgerConnection.objects.get(id=connection_id)

        except VoidForgerConnection.DoesNotExist:
            messages.error(request, "Selected VoidForger connection does not exist.")
            return redirect('chats:voidforger_create')

        chat = MultimodalVoidForgerChat(
            uuid=str(uuid.uuid4()),
            connection=connection
        )
        chat.save()

        messages.success(request, "VoidForger Chat instance created successfully.")
        return redirect('chats:voidforger_create')
