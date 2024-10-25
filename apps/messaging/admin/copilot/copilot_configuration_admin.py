#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_configuration_admin.py
#  Last Modified: 2024-10-25 04:30:32
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:30:32
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin

from apps.messaging.models import ElectronCopilotConfiguration
from apps.messaging.utils import ELECTRON_COPILOT_CONFIGURATION_ADMIN_LIST, \
    ELECTRON_COPILOT_CONFIGURATION_ADMIN_FILTER, ELECTRON_COPILOT_CONFIGURATION_ADMIN_SEARCH


@admin.register(ElectronCopilotConfiguration)
class ElectronCopilotConfigurationAdmin(admin.ModelAdmin):
    list_display = ELECTRON_COPILOT_CONFIGURATION_ADMIN_LIST
    list_filter = ELECTRON_COPILOT_CONFIGURATION_ADMIN_FILTER
    search_fields = ELECTRON_COPILOT_CONFIGURATION_ADMIN_SEARCH
    ordering = ('-last_toggled_is_active_at',)
