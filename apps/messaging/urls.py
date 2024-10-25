#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 04:24:41
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:24:41
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.urls import path

from apps.messaging.views import (MessagingView_AssistantChatCreate, MessagingView_CopilotAssignAssistantChat,
                                  MessagingView_CopilotAssignActiveConnectionType,
                                  MessagingView_OrchestrationConnectionVerify,
                                  MessagingView_AssistantConnectionVerify, MessagingView_LeanmodConnectionVerify,
                                  MessagingView_CopilotToggleVisibility, MessagingView_CopilotMainModal,
                                  MessagingView_MainManagerPanel, MessagingView_OrchestrationSendMessage,
                                  MessagingView_CopilotAssignAssistantConnection,
                                  MessagingView_CopilotAssignOrchestrationConnection,
                                  MessagingView_CopilotAssignLeanmodConnection, MessagingView_CopilotAssignLeanmodChat,
                                  MessagingView_CopilotAssignOrchestrationChat, MessagingView_OrchestrationChatCreate,
                                  MessagingView_AssistantConnectionCreate, MessagingView_AssistantConnectionRemove,
                                  MessagingView_LeanmodConnectionRemove, MessagingView_LeanmodConnectionCreate,
                                  MessagingView_OrchestrationConnectionRemove,
                                  MessagingView_OrchestrationConnectionCreate, MessagingView_OrchestrationChatRemove,
                                  MessagingView_AssistantChatRemove, MessagingView_LeanmodChatRemove,
                                  MessagingView_LeanmodChatCreate, MessagingView_LeanmodSendMessage,
                                  MessagingView_AssistantSendMessage)

app_name = 'messaging'

urlpatterns = [
    #################################################################################################################
    # HTTP VIEWS
    #################################################################################################################

    # Connections
    #   - Assistant
    #       - Create
    path('assistant/connection/create',
         MessagingView_AssistantConnectionCreate.as_view(), name='assistant_connection_create'),
    #       - Remove
    path('assistant/connection/remove',
         MessagingView_AssistantConnectionRemove.as_view(), name='assistant_connection_remove'),
    #       - Verify
    path('assistant/connection/verify',
         MessagingView_AssistantConnectionVerify.as_view(), name='assistant_connection_verify'),
    #   - Leanmod
    #       - Create
    path('leanmod/connection/create',
         MessagingView_LeanmodConnectionCreate.as_view(), name='leanmod_connection_create'),
    #       - Remove
    path('leanmod/connection/remove',
         MessagingView_LeanmodConnectionRemove.as_view(), name='leanmod_connection_remove'),
    #       - Verify
    path('leanmod/connection/verify',
         MessagingView_LeanmodConnectionVerify.as_view(), name='leanmod_connection_verify'),
    #   - Orchestration
    #       - Create
    path('orchestration/connection/create',
         MessagingView_OrchestrationConnectionCreate.as_view(), name='orchestration_connection_create'),
    #       - Remove
    path('orchestration/connection/remove',
         MessagingView_OrchestrationConnectionRemove.as_view(), name='orchestration_connection_remove'),
    #       - Verify
    path('orchestration/connection/verify',
         MessagingView_OrchestrationConnectionVerify.as_view(), name='orchestration_connection_verify'),

    # Chats
    #   - Assistant
    #       - Create
    path('assistant/chat/create',
         MessagingView_AssistantChatCreate.as_view(), name='assistant_chat_create'),
    #       - Remove
    path('assistant/chat/remove',
         MessagingView_AssistantChatRemove.as_view(), name='assistant_chat_remove'),
    #       - Send Message
    path('assistant/chat/send_message',
         MessagingView_AssistantSendMessage.as_view(), name='assistant_send_message'),
    #   - Leanmod
    #       - Create
    path('leanmod/chat/create',
         MessagingView_LeanmodChatCreate.as_view(), name='leanmod_chat_create'),
    #       - Remove
    path('leanmod/chat/remove',
         MessagingView_LeanmodChatRemove.as_view(), name='leanmod_chat_remove'),
    #       - Send Message
    path('leanmod/chat/send_message',
         MessagingView_LeanmodSendMessage.as_view(), name='leanmod_send_message'),
    #   - Orchestration
    #       - Create
    path('orchestration/chat/create',
         MessagingView_OrchestrationChatCreate.as_view(), name='orchestration_chat_create'),
    #       - Remove
    path('orchestration/chat/remove',
         MessagingView_OrchestrationChatRemove.as_view(), name='orchestration_chat_remove'),
    #       - Send Message
    path('orchestration/chat/send_message',
         MessagingView_OrchestrationSendMessage.as_view(), name='orchestration_send_message'),

    # Copilot
    #   - Visibility
    #       - Toggle Visibility
    path('copilot/toggle_visibility',
         MessagingView_CopilotToggleVisibility.as_view(), name='copilot_toggle_visibility'),
    #   - Connection Type
    #       - Assign Active Connection Type
    path('copilot/assign/active_connection_type',
         MessagingView_CopilotAssignActiveConnectionType.as_view(), name='copilot_assign_active_connection_type'),
    #   - Connection
    #       - Assign Assistant Connection
    path('copilot/assign/assistant_connection',
         MessagingView_CopilotAssignAssistantConnection.as_view(), name='copilot_assign_assistant_connection'),
    #       - Assign Leanmod Connection
    path('copilot/assign/leanmod_connection',
         MessagingView_CopilotAssignLeanmodConnection.as_view(), name='copilot_assign_leanmod_connection'),
    #       - Assign Orchestration Connection
    path('copilot/assign/orchestration_connection',
         MessagingView_CopilotAssignOrchestrationConnection.as_view(), name='copilot_assign_orchestration_connection'),
    #   - Chat
    #       - Assign Assistant Chat
    path('copilot/assign/assistant_chat',
         MessagingView_CopilotAssignAssistantChat.as_view(), name='copilot_assign_assistant_chat'),
    #       - Assign Leanmod Chat
    path('copilot/assign/leanmod_chat',
         MessagingView_CopilotAssignLeanmodChat.as_view(), name='copilot_assign_leanmod_chat'),
    #       - Assign Orchestration Chat
    path('copilot/assign/orchestration_chat',
         MessagingView_CopilotAssignOrchestrationChat.as_view(), name='copilot_assign_orchestration_chat'),

    #################################################################################################################

    # ...

    #################################################################################################################
    # TEMPLATE / HTML VIEWS
    #################################################################################################################

    # Main Manager
    #   - Dashboard
    path('',
         MessagingView_MainManagerPanel.as_view(
             template_name='messaging/messaging_main.html'
         ), name='main_manager_panel'),

    # Modals
    #   - Copilot
    path('copilot/main_modal',
         MessagingView_CopilotMainModal.as_view(
             template_name='messaging/copilot_modal.html'
         ), name='copilot_main_modal'),

    #################################################################################################################

]
