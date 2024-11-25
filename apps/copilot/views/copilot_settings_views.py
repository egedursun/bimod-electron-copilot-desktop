#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_settings_views.py
#  Last Modified: 2024-10-25 21:11:57
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 21:11:57
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages

from apps.chats.models import (
    MultimodalAssistantChat,
    MultimodalLeanmodChat,
    MultimodalOrchestrationChat,
    MultimodalVoidForgerChat
)

from apps.connections.models import (
    AssistantConnection,
    LeanmodConnection,
    OrchestrationConnection,
    VoidForgerConnection
)

from apps.copilot.models import CopilotModal
from apps.copilot.utils import COPILOT_CONNECTION_TYPES
from web_project import TemplateLayout


class CopilotView_Settings(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        copilot_instance = CopilotModal.objects.first()
        context['copilot_instance'] = copilot_instance
        context['copilot_connection_types'] = COPILOT_CONNECTION_TYPES

        context['assistant_connections'] = AssistantConnection.objects.all()
        context['assistant_chats'] = MultimodalAssistantChat.objects.all()

        context['leanmod_connections'] = LeanmodConnection.objects.all()
        context['leanmod_chats'] = MultimodalLeanmodChat.objects.all()

        context['orchestration_connections'] = OrchestrationConnection.objects.all()
        context['orchestration_chats'] = MultimodalOrchestrationChat.objects.all()

        context['voidforger_connections'] = VoidForgerConnection.objects.all()
        context['voidforger_chats'] = MultimodalVoidForgerChat.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        copilot_instance = CopilotModal.objects.first()

        if 'activate' in request.POST:

            if not copilot_instance:
                copilot_instance = CopilotModal.objects.create()
                messages.success(request, "Copilot activated.")

            else:
                messages.info(request, "Copilot is already activated.")

        elif 'deactivate' in request.POST:

            if copilot_instance:
                copilot_instance.delete()
                messages.success(request, "Copilot deactivated.")

            return redirect('copilot:settings')

        active_connection_type = request.POST.get('active_connection_type')

        required_connection = request.POST.get(f'selected_{active_connection_type}')
        required_chat = request.POST.get(f'selected_{active_connection_type}_chat')

        if not active_connection_type or not required_connection or not required_chat:
            messages.error(request, f"Please select a connection and chat to proceed.")
            return redirect('copilot:settings')

        copilot_instance.is_active = 'is_active' in request.POST
        copilot_instance.active_connection_type = active_connection_type

        copilot_instance.selected_assistant_id = request.POST.get('selected_assistant')
        copilot_instance.selected_leanmod_id = request.POST.get('selected_leanmod')
        copilot_instance.selected_orchestration_id = request.POST.get('selected_orchestration')
        copilot_instance.selected_voidforger_id = request.POST.get('selected_voidforger')

        copilot_instance.selected_assistant_chat_id = request.POST.get('selected_assistant_chat')
        copilot_instance.selected_leanmod_chat_id = request.POST.get('selected_leanmod_chat')
        copilot_instance.selected_orchestration_chat_id = request.POST.get('selected_orchestration_chat')
        copilot_instance.selected_voidforger_chat_id = request.POST.get('selected_voidforger_chat')

        copilot_instance.save()

        messages.success(request, "Copilot settings updated successfully.")
        return redirect('copilot:settings')
