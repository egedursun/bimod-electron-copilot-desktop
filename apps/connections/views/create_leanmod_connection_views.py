#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_leanmod_connection_views.py
#  Last Modified: 2024-10-25 19:15:49
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:07:26
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


class ConnectionView_LeanmodCreate(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['default_connection_is_public'] = False
        return context

    def post(self, request, *args, **kwargs):
        connection_endpoint = request.POST.get('connection_endpoint')
        connection_is_public = request.POST.get('connection_is_public', 'off') == 'on'
        connection_api_key = request.POST.get('connection_api_key') if not connection_is_public else None

        if not connection_endpoint:
            messages.error(request, "LeanMod connection endpoint is required.")
            return redirect('connections:leanmod_create')

        if not connection_is_public and not connection_api_key:
            messages.error(request, "API key is required when LeanMod connection is not public.")
            return redirect('connections:leanmod_create')

        new_connection = LeanmodConnection(
            connection_endpoint=connection_endpoint, connection_is_public=connection_is_public,
            connection_api_key=connection_api_key)
        new_connection.save()

        messages.success(request, "LeanMod connection created successfully.")
        return redirect('connections:leanmod_create')
