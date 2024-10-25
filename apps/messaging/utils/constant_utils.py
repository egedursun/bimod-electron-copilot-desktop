#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: constant_utils.py
#  Last Modified: 2024-10-25 04:23:16
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:23:58
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


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


CONNECTION_TYPES = [
    ('assistant', 'Assistant'),
    ('leanmod', 'Leanmod'),
    ('orchestration', 'Orchestration'),
]


class ConnectionTypesNames:
    ASSISTANT = 'assistant'
    LEANMOD = 'leanmod'
    ORCHESTRATION = 'orchestration'

    @staticmethod
    def as_list():
        return [ConnectionTypesNames.ASSISTANT, ConnectionTypesNames.LEANMOD, ConnectionTypesNames.ORCHESTRATION]


MULTIMODAL_ASSISTANT_CHAT_ADMIN_LIST = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_ASSISTANT_CHAT_ADMIN_FILTER = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_ASSISTANT_CHAT_ADMIN_SEARCH = ['organization_name', 'agent_name', 'chat_name', 'created_at']

MULTIMODAL_LEANMOD_CHAT_ADMIN_LIST = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_LEANMOD_CHAT_ADMIN_FILTER = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_LEANMOD_CHAT_ADMIN_SEARCH = ['organization_name', 'agent_name', 'chat_name', 'created_at']

MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_LIST = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_FILTER = ['organization_name', 'agent_name', 'chat_name', 'created_at']
MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_SEARCH = ['organization_name', 'agent_name', 'chat_name', 'created_at']

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

ASSISTANT_CONNECTION_ADMIN_LIST = ['connection_endpoint', 'connection_is_public', 'connection_api_key',
                                   'connection_agent_name', 'created_at']
ASSISTANT_CONNECTION_ADMIN_FILTER = ['connection_is_public', 'created_at']
ASSISTANT_CONNECTION_ADMIN_SEARCH = ['connection_endpoint', 'connection_agent_name', 'connection_agent_description']

LEANMOD_CONNECTION_ADMIN_LIST = ["connection_endpoint", "connection_is_public", "connection_api_key",
                                 "connection_agent_name", "created_at"]
LEANMOD_CONNECTION_ADMIN_FILTER = ["connection_is_public", "created_at"]
LEANMOD_CONNECTION_ADMIN_SEARCH = ["connection_endpoint", "connection_api_key", "connection_agent_name", "created_at"]

ORCHESTRATION_CONNECTION_ADMIN_LIST = ['connection_endpoint', 'connection_is_public', 'connection_api_key',
                                       'connection_agent_name', 'created_at']
ORCHESTRATION_CONNECTION_ADMIN_FILTER = ['connection_is_public', 'created_at']
ORCHESTRATION_CONNECTION_ADMIN_SEARCH = ['connection_endpoint', 'connection_agent_name']
