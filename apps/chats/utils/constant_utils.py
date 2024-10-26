#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: constant_utils.py
#  Last Modified: 2024-10-25 20:26:52
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:26:53
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


MULTIMODAL_ASSISTANT_CHAT_ADMIN_LIST = ['uuid', 'created_at']
MULTIMODAL_ASSISTANT_CHAT_ADMIN_FILTER = ['uuid', 'created_at']
MULTIMODAL_ASSISTANT_CHAT_ADMIN_SEARCH = ['uuid', 'created_at']

MULTIMODAL_LEANMOD_CHAT_ADMIN_LIST = ['uuid', 'created_at']
MULTIMODAL_LEANMOD_CHAT_ADMIN_FILTER = ['uuid', 'created_at']
MULTIMODAL_LEANMOD_CHAT_ADMIN_SEARCH = ['uuid', 'created_at']

MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_LIST = ['uuid', 'created_at']
MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_FILTER = ['uuid', 'created_at']
MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_SEARCH = ['uuid', 'created_at']

MULTIMODAL_ASSISTANT_CHAT_MESSAGE_ADMIN_LIST = ('chat', 'message_role', 'sent_at')
MULTIMODAL_ASSISTANT_CHAT_MESSAGE_ADMIN_FILTER = ('chat', 'message_role', 'sent_at')
MULTIMODAL_ASSISTANT_CHAT_MESSAGE_ADMIN_SEARCH = ('chat', 'message_role', 'message_text', 'sent_at')

MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_LIST = ('chat', 'message_role', 'sent_at')
MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_FILTER = ('chat', 'message_role', 'sent_at')
MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_SEARCH = ('chat', 'message_role', 'message_text', 'sent_at')

MULTIMODAL_ORCHESTRATION_CHAT_MESSAGE_ADMIN_LIST = ('chat', 'message_role', 'sent_at')
MULTIMODAL_ORCHESTRATION_CHAT_MESSAGE_ADMIN_FILTER = ('chat', 'message_role', 'sent_at')
MULTIMODAL_ORCHESTRATION_CHAT_MESSAGE_ADMIN_SEARCH = ('chat', 'message_role', 'message_text', 'sent_at')

ELECTRON_COPILOT_CONFIGURATION_ADMIN_LIST = ['is_active', 'connection_type_selection', 'last_toggled_is_active_at']
ELECTRON_COPILOT_CONFIGURATION_ADMIN_FILTER = ['is_active', 'connection_type_selection']
ELECTRON_COPILOT_CONFIGURATION_ADMIN_SEARCH = ['connection_type_selection']

CHAT_ROLES = [
    ('system', 'System'),
    ('assistant', 'Assistant'),
    ('user', 'User'),
]


class ChatRolesNames:
    SYSTEM = 'system'
    ASSISTANT = 'assistant'
    USER = 'user'

    @staticmethod
    def as_list():
        return [ChatRolesNames.SYSTEM, ChatRolesNames.ASSISTANT, ChatRolesNames.USER]
