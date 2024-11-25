#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: remove_assistant_connection_views.py
#  Last Modified: 2024-10-25 18:46:35
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:09:08
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
#

import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.connections.models import AssistantConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ConnectionView_AssistantRemove(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['connections'] = AssistantConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        connection_id = request.POST.get('connection_id')

        if connection_id:
            try:
                connection = AssistantConnection.objects.get(id=connection_id)
                connection.delete()
                messages.success(request, "Assistant connection successfully deleted.")

            except AssistantConnection.DoesNotExist:
                messages.error(request, "Assistant connection not found.")
        else:
            messages.error(request, "No Assistant connection ID provided.")

        return redirect('connections:assistant_remove')
