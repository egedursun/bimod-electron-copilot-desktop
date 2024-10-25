#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: assistant_connection_admin.py
#  Last Modified: 2024-10-25 04:30:00
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:30:00
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin

from apps.messaging.models import AssistantConnection
from apps.messaging.utils import ASSISTANT_CONNECTION_ADMIN_LIST, ASSISTANT_CONNECTION_ADMIN_FILTER, \
    ASSISTANT_CONNECTION_ADMIN_SEARCH


@admin.register(AssistantConnection)
class AssistantConnectionAdmin(admin.ModelAdmin):
    list_display = ASSISTANT_CONNECTION_ADMIN_LIST
    list_filter = ASSISTANT_CONNECTION_ADMIN_FILTER
    search_fields = ASSISTANT_CONNECTION_ADMIN_SEARCH
    ordering = ['created_at']
