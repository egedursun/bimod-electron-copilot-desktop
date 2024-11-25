#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: orchestration_chat_admin.py
#  Last Modified: 2024-10-25 15:54:19
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:32:07
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
#


from django.contrib import admin

from apps.chats.models import MultimodalOrchestrationChat
from apps.chats.utils import (
    MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_LIST,
    MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_FILTER,
    MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_SEARCH
)


@admin.register(MultimodalOrchestrationChat)
class MultimodalChatAdmin(admin.ModelAdmin):
    list_display = MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_LIST
    list_filter = MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_FILTER
    search_fields = MULTIMODAL_ORCHESTRATION_CHAT_ADMIN_SEARCH
    ordering = ['-created_at']
    readonly_fields = ['created_at']
