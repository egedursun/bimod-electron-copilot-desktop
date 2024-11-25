#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: meta_kanban_board_connection_delete_views.py
#  Last Modified: 2024-10-28 17:42:59
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-28 17:42:59
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from apps.metakanban.models import MetaKanbanBoardConnection


class MetaKanbanView_BoardConnectionDelete(View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        try:
            connection = get_object_or_404(MetaKanbanBoardConnection)
            connection.delete()

        except Exception as e:
            messages.error(request, "Failed to delete MetaKanban Board connection.")
            return redirect("metakanban:connection_manage")

        messages.success(request, "MetaKanban Board connection deleted successfully.")
        return redirect("metakanban:connection_manage")
