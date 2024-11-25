#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 20:27:24
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:27:25
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.urls import path

from apps.chats.views import (
    ChatView_LeanmodCreate,
    ChatView_OrchestrationCreate,
    ChatView_AssistantCreate,
    ChatView_AssistantRemove,
    ChatView_LeanmodRemove,
    ChatView_OrchestrationRemove,
    ChatView_VoidForgerCreate,
    ChatView_VoidForgerRemove,
)

app_name = 'chats'

urlpatterns = [
    path(
        'assistant/create/',
        ChatView_AssistantCreate.as_view(
            template_name='chats/create/create_assistant_chat.html'
        ),
        name='assistant_create'
    ),
    path(
        'assistant/remove/',
        ChatView_AssistantRemove.as_view(
            template_name='chats/remove/remove_assistant_chats.html'
        ),
        name='assistant_remove'
    ),

    #####

    path(
        'leanmod/create/',
        ChatView_LeanmodCreate.as_view(
            template_name='chats/create/create_leanmod_chat.html'
        ),
        name='leanmod_create'
    ),
    path(
        'leanmod/remove/',
        ChatView_LeanmodRemove.as_view(
            template_name='chats/remove/remove_leanmod_chats.html'
        ),
        name='leanmod_remove'
    ),

    #####

    path(
        'orchestration/create/',
        ChatView_OrchestrationCreate.as_view(
            template_name='chats/create/create_orchestration_chat.html'
        ),
        name='orchestration_create'
    ),
    path(
        'orchestration/remove/',
        ChatView_OrchestrationRemove.as_view(
            template_name='chats/remove/remove_orchestration_chats.html'
        ),
        name='orchestration_remove'
    ),

    ######

    path(
        'voidforger/create/',
        ChatView_VoidForgerCreate.as_view(
            template_name='chats/create/create_voidforger_chat.html'
        ),
        name='voidforger_create'
    ),

    path(
        'voidforger/remove/',
        ChatView_VoidForgerRemove.as_view(
            template_name='chats/remove/remove_voidforger_chats.html'
        ),
        name='voidforger_remove'
    ),
]
