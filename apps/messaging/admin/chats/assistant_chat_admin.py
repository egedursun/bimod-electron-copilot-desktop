#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: chat_admin.py
#  Last Modified: 2024-10-25 04:29:43
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:29:43
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin

from apps.messaging.models import MultimodalAssistantChat
from apps.messaging.utils import (MULTIMODAL_ASSISTANT_CHAT_ADMIN_LIST, MULTIMODAL_ASSISTANT_CHAT_ADMIN_FILTER,
                                  MULTIMODAL_ASSISTANT_CHAT_ADMIN_SEARCH)


@admin.register(MultimodalAssistantChat)
class MultimodalChatAdmin(admin.ModelAdmin):
    list_display = MULTIMODAL_ASSISTANT_CHAT_ADMIN_LIST
    list_filter = MULTIMODAL_ASSISTANT_CHAT_ADMIN_FILTER
    search_fields = MULTIMODAL_ASSISTANT_CHAT_ADMIN_SEARCH
    ordering = ['-created_at']
    readonly_fields = ['created_at']
