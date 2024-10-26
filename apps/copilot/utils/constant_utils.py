#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: constant_utils.py
#  Last Modified: 2024-10-25 22:54:28
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 22:54:28
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


COPILOT_CONNECTION_TYPES = [
    ('assistant', 'Assistant'),
    ('leanmod', 'LeanMod'),
    ('orchestration', 'Orchestration'),
]


class CopilotConnectionTypesNames:
    ASSISTANT = 'assistant'
    LEANMOD = 'leanmod'
    ORCHESTRATION = 'orchestration'

    @staticmethod
    def as_list():
        return [
            CopilotConnectionTypesNames.ASSISTANT,
            CopilotConnectionTypesNames.LEANMOD,
            CopilotConnectionTypesNames.ORCHESTRATION,
        ]


COPILOT_MODAL_ADMIN_LIST = ['active_connection_type', 'is_active', 'last_toggled_is_active_at']
COPILOT_MODAL_ADMIN_FILTER = ['active_connection_type', 'is_active']
COPILOT_MODAL_ADMIN_SEARCH = ['active_connection_type']
