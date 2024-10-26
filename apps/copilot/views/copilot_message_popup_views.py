#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_message_popup_views.py
#  Last Modified: 2024-10-26 17:30:32
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-26 17:30:32
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.chats.models import MultimodalAssistantChatMessage, MultimodalLeanmodChatMessage, \
    MultimodalOrchestrationChatMessage
from apps.copilot.models import CopilotModal
from apps.copilot.utils import CopilotConnectionTypesNames
from apps.dashboards.views import DashboardView_Assistant, DashboardView_Leanmod, DashboardView_Orchestration
from web_project import TemplateLayout, TemplateHelper


class CopilotView_MessagePopup(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context.update({
            "layout": "blank", "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            "display_customizer": False})

        copilots = CopilotModal.objects.all()
        if not copilots:
            messages.error(self.request, "Copilot is not activated, please first active the copilot.")
            return context
        copilot: CopilotModal = copilots.first()

        copilot_service_type = copilot.active_connection_type
        if copilot_service_type == CopilotConnectionTypesNames.ASSISTANT:
            copilot_chat = copilot.selected_assistant_chat
            chat_history = MultimodalAssistantChatMessage.objects.filter(chat=copilot_chat).order_by('sent_at').all()
            context.update({"chat_item": copilot_chat, "chat_messages": chat_history, "copilot": copilot})
            return context
        elif copilot_service_type == CopilotConnectionTypesNames.LEANMOD:
            copilot_chat = copilot.selected_leanmod_chat
            chat_history = MultimodalLeanmodChatMessage.objects.filter(chat=copilot_chat).order_by('sent_at').all()
            context.update({"chat_item": copilot_chat, "chat_messages": chat_history, "copilot": copilot})
        elif copilot_service_type == CopilotConnectionTypesNames.ORCHESTRATION:
            copilot_chat = copilot.selected_orchestration_chat
            chat_history = MultimodalOrchestrationChatMessage.objects.filter(chat=copilot_chat).order_by(
                'sent_at').all()
            context.update({"chat_item": copilot_chat, "chat_messages": chat_history, "copilot": copilot})
        else:
            messages.error(self.request, "Copilot service type is not valid.")
            return context
        return context

    def post(self, request, *args, **kwargs):
        copilots = CopilotModal.objects.all()
        if not copilots:
            messages.error(request, "Copilot is not activated, please first active the copilot.")
            return redirect('copilot:message_popup')

        copilot: CopilotModal = copilots.first()
        copilot_service_type = copilot.active_connection_type

        message_text = request.POST.get('message_content')
        attached_files = request.POST.get('file_uris')
        attached_images = request.POST.get('image_uris')

        if copilot_service_type == CopilotConnectionTypesNames.ASSISTANT:
            try:
                copilot_chat = copilot.selected_assistant_chat

                MultimodalAssistantChatMessage.objects.create(
                    chat=copilot_chat, message_role='user', message_text=message_text,
                    message_file_uris=attached_files,
                    message_image_uris=attached_images)

                chat_messages = MultimodalAssistantChatMessage.objects.filter(chat=copilot_chat).order_by('sent_at')
                chat_history = [
                    {
                        "role": msg.message_role,
                        "content": msg.message_text,
                        "file_uris": msg.message_file_uris,
                        "image_uris": msg.message_image_uris
                    }
                    for msg in chat_messages
                ]

                _ = DashboardView_Assistant.get_assistant_response(
                    chat=copilot_chat, chat_history=chat_history)
            except Exception as e:
                messages.error(request, f"Error while sending the message: {e}")
                return redirect('copilot:message_popup')
            return redirect('copilot:message_popup')

        elif copilot_service_type == CopilotConnectionTypesNames.LEANMOD:
            try:
                copilot_chat = copilot.selected_leanmod_chat

                MultimodalLeanmodChatMessage.objects.create(
                    chat=copilot_chat, message_role='user', message_text=message_text,
                    message_file_uris=attached_files,
                    message_image_uris=attached_images)

                chat_messages = MultimodalLeanmodChatMessage.objects.filter(chat=copilot_chat).order_by('sent_at')
                chat_history = [
                    {
                        "role": msg.message_role,
                        "content": msg.message_text,
                        "file_uris": msg.message_file_uris,
                        "image_uris": msg.message_image_uris
                    }
                    for msg in chat_messages
                ]

                _ = DashboardView_Leanmod.get_leanmod_response(chat=copilot_chat, chat_history=chat_history)
            except Exception as e:
                messages.error(request, f"Error while sending the message: {e}")
                return redirect('copilot:message_popup')
            return redirect('copilot:message_popup')

        elif copilot_service_type == CopilotConnectionTypesNames.ORCHESTRATION:
            try:
                copilot_chat = copilot.selected_orchestration_chat

                MultimodalOrchestrationChatMessage.objects.create(
                    chat=copilot_chat, message_role='user', message_text=message_text,
                    message_file_uris=attached_files,
                    message_image_uris=attached_images)

                chat_messages = MultimodalOrchestrationChatMessage.objects.filter(chat=copilot_chat).order_by(
                    'sent_at')
                chat_history = [
                    {
                        "role": msg.message_role,
                        "content": msg.message_text,
                        "file_uris": msg.message_file_uris,
                        "image_uris": msg.message_image_uris
                    }
                    for msg in chat_messages
                ]

                _ = DashboardView_Orchestration.get_orchestration_response(chat=copilot_chat,
                                                                           chat_history=chat_history)
            except Exception as e:
                messages.error(request, f"Error while sending the message: {e}")
                return redirect('copilot:message_popup')
            return redirect('copilot:message_popup')

        else:
            messages.error(request, "Copilot service type is not valid.")
            return redirect('copilot:message_popup')
