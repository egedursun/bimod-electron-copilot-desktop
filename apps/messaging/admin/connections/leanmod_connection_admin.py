#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: leanmod_connection_admin.py
#  Last Modified: 2024-10-25 04:30:07
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:30:07
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin

from apps.messaging.models import LeanmodConnection
from apps.messaging.utils import LEANMOD_CONNECTION_ADMIN_LIST, LEANMOD_CONNECTION_ADMIN_FILTER, \
    LEANMOD_CONNECTION_ADMIN_SEARCH


@admin.register(LeanmodConnection)
class LeanmodConnectionAdmin(admin.ModelAdmin):
    list_display = LEANMOD_CONNECTION_ADMIN_LIST
    list_filter = LEANMOD_CONNECTION_ADMIN_FILTER
    search_fields = LEANMOD_CONNECTION_ADMIN_SEARCH
    ordering = ["-created_at"]
