#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: constant_utils.py
#  Last Modified: 2024-10-25 20:01:24
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:01:25
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


ASSISTANT_CONNECTION_ADMIN_LIST = [
    'connection_endpoint',
    'connection_is_public',
    'connection_api_key',
    'created_at'
]
ASSISTANT_CONNECTION_ADMIN_FILTER = [
    'connection_is_public',
    'created_at'
]
ASSISTANT_CONNECTION_ADMIN_SEARCH = [
    'connection_endpoint',
    'connection_api_key',
    'created_at'
]

LEANMOD_CONNECTION_ADMIN_LIST = [
    "connection_endpoint",
    "connection_is_public",
    "connection_api_key",
    "created_at"
]
LEANMOD_CONNECTION_ADMIN_FILTER = [
    "connection_is_public",
    "created_at"
]
LEANMOD_CONNECTION_ADMIN_SEARCH = [
    "connection_endpoint",
    "connection_api_key",
    "created_at"
]

ORCHESTRATION_CONNECTION_ADMIN_LIST = [
    'connection_endpoint',
    'connection_is_public',
    'connection_api_key',
    'created_at'
]
ORCHESTRATION_CONNECTION_ADMIN_FILTER = [
    'connection_is_public',
    'created_at'
]
ORCHESTRATION_CONNECTION_ADMIN_SEARCH = [
    'connection_endpoint',
    'connection_api_key',
    'created_at'
]

VOIDFORGER_CONNECTION_ADMIN_LIST = [
    'connection_endpoint',
    'connection_is_public',
    'connection_api_key',
    'created_at'
]
VOIDFORGER_CONNECTION_ADMIN_FILTER = [
    'connection_is_public',
    'created_at'
]
VOIDFORGER_CONNECTION_ADMIN_SEARCH = [
    'connection_endpoint',
    'connection_api_key',
    'created_at'
]

CONNECTION_TYPES = [
    ('assistant', 'Assistant'),
    ('leanmod', 'Leanmod'),
    ('orchestration', 'Orchestration'),
    ('voidforger', 'VoidForger')
]


class ConnectionTypesNames:
    ASSISTANT = 'assistant'
    LEANMOD = 'leanmod'
    ORCHESTRATION = 'orchestration'

    @staticmethod
    def as_list():
        return [
            ConnectionTypesNames.ASSISTANT,
            ConnectionTypesNames.LEANMOD,
            ConnectionTypesNames.ORCHESTRATION
        ]
