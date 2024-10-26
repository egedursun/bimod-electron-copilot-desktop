#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: remove_leanmod_connection_views.py
#  Last Modified: 2024-10-25 18:47:08
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:09:51
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.connections.models import LeanmodConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ConnectionView_LeanmodRemove(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['connections'] = LeanmodConnection.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        connection_id = request.POST.get('connection_id')
        if connection_id:
            try:
                connection = LeanmodConnection.objects.get(id=connection_id)
                connection.delete()
                messages.success(request, "LeanMod connection successfully deleted.")
            except LeanmodConnection.DoesNotExist:
                messages.error(request, "LeanMod connection not found.")
        else:
            messages.error(request, "No connection ID provided.")

        return redirect('connections:leanmod_remove')
