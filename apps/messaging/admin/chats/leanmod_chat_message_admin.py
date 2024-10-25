#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: leanmod_chat_message_admin.py
#  Last Modified: 2024-10-25 15:47:29
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 15:47:29
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin

from apps.messaging.models import MultimodalLeanmodChatMessage
from apps.messaging.utils import MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_LIST, \
    MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_FILTER, MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_SEARCH


@admin.register(MultimodalLeanmodChatMessage)
class MultimodalChatMessageAdmin(admin.ModelAdmin):
    list_display = MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_LIST
    list_filter = MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_FILTER
    search_fields = MULTIMODAL_LEANMOD_CHAT_MESSAGE_ADMIN_SEARCH
    ordering = ('-sent_at',)
    readonly_fields = ('sent_at',)
