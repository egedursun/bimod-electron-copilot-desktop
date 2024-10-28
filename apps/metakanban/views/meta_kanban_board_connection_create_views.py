#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: meta_kanban_board_connection_create_views.py
#  Last Modified: 2024-10-28 17:42:03
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-28 17:42:03
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from apps.metakanban.models import MetaKanbanBoardConnection


class MetaKanbanView_BoardConnectionCreate(View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        api_key = request.POST.get('board_connection_api_key')

        try:
            connection, created = MetaKanbanBoardConnection.objects.get_or_create(
                defaults={'board_connection_api_key': api_key}
            )

            if not created:
                connection.board_connection_api_key = api_key
                connection.save()
        except Exception as e:
            messages.error(request, "Failed to create MetaKanban Board connection.")
            return redirect("metakanban:connection_manage")

        messages.success(request, "MetaKanban Board connection updated successfully.")
        return redirect("metakanban:connection_manage")
