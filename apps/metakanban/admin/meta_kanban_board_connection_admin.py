#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: meta_kanban_board_connection_admin.py
#  Last Modified: 2024-10-28 17:35:45
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-28 17:35:46
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.contrib import admin

from apps.metakanban.models import MetaKanbanBoardConnection
from apps.metakanban.utils import (
    META_KANBAN_BOARD_CONNECTION_ADMIN_LIST,
    META_KANBAN_BOARD_CONNECTION_ADMIN_SEARCH,
    META_KANBAN_BOARD_CONNECTION_ADMIN_FILTER
)


@admin.register(MetaKanbanBoardConnection)
class MetaKanbanBoardConnectionAdmin(admin.ModelAdmin):
    list_display = META_KANBAN_BOARD_CONNECTION_ADMIN_LIST
    search_fields = META_KANBAN_BOARD_CONNECTION_ADMIN_SEARCH
    list_filter = META_KANBAN_BOARD_CONNECTION_ADMIN_FILTER
    ordering = ['-created_at']
