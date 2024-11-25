#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: voidforger_chat_message_admin.py
#  Last Modified: 2024-11-25 00:45:53
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-25 00:45:54
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from apps.chats.models import MultimodalVoidForgerChatMessage

from django.contrib import admin

from apps.chats.utils import (
    MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_LIST,
    MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_FILTER,
    MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_SEARCH
)


@admin.register(MultimodalVoidForgerChatMessage)
class MultimodalVoidForgerChatMessageAdmin(admin.ModelAdmin):
    list_display = MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_LIST
    list_filter = MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_FILTER
    search_fields = MULTIMODAL_VOIDFORGER_CHAT_MESSAGE_ADMIN_SEARCH
    ordering = ('-sent_at',)
    readonly_fields = ('sent_at',)
