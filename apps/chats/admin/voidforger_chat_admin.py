#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: voidforger_chat_admin.py
#  Last Modified: 2024-11-25 00:45:47
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-25 00:45:47
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.contrib import admin

from apps.chats.models import MultimodalVoidForgerChat
from apps.chats.utils import (
    MULTIMODAL_VOIDFORGER_CHAT_ADMIN_LIST,
    MULTIMODAL_VOIDFORGER_CHAT_ADMIN_FILTER,
    MULTIMODAL_VOIDFORGER_CHAT_ADMIN_SEARCH
)


@admin.register(MultimodalVoidForgerChat)
class MultimodalChatAdmin(admin.ModelAdmin):
    list_display = MULTIMODAL_VOIDFORGER_CHAT_ADMIN_LIST
    list_filter = MULTIMODAL_VOIDFORGER_CHAT_ADMIN_FILTER
    search_fields = MULTIMODAL_VOIDFORGER_CHAT_ADMIN_SEARCH
    ordering = ['-created_at']
    readonly_fields = ['created_at']
