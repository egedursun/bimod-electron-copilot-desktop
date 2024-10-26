#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_configuration_admin.py
#  Last Modified: 2024-10-25 22:55:37
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 22:55:37
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.contrib import admin

from apps.copilot.models import CopilotModal
from apps.copilot.utils import COPILOT_MODAL_ADMIN_LIST, COPILOT_MODAL_ADMIN_FILTER, COPILOT_MODAL_ADMIN_SEARCH


@admin.register(CopilotModal)
class CopilotModalAdmin(admin.ModelAdmin):
    list_display = COPILOT_MODAL_ADMIN_LIST
    list_filter = COPILOT_MODAL_ADMIN_FILTER
    search_fields = COPILOT_MODAL_ADMIN_SEARCH
