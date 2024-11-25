#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_orchestration_connection_views.py
#  Last Modified: 2024-10-25 19:16:20
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:07:39
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

import logging

import requests
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView

from apps.connections.models import OrchestrationConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ConnectionView_OrchestrationCreate(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['default_connection_is_public'] = False
        return context

    def post(self, request, *args, **kwargs):
        connection_endpoint = request.POST.get('connection_endpoint')
        connection_is_public = request.POST.get('connection_is_public', 'off') == 'on'
        connection_api_key = request.POST.get('connection_api_key') if not connection_is_public else None

        if "export_orchestrations" not in connection_endpoint:
            messages.error(request, "Orchestration connection endpoint must contain 'export_orchestrations'.")
            return redirect('connections:orchestration_create')

        if not connection_endpoint:
            messages.error(request, "Orchestration connection endpoint is required.")
            return redirect('connections:orchestration_create')

        if not connection_is_public and not connection_api_key:
            messages.error(request, "API key is required when Orchestration connection is not public.")
            return redirect('connections:orchestration_create')

        health_check_url = connection_endpoint.replace("exported", "health")

        try:
            response = requests.post(health_check_url)
            if response.status_code != 200:

                try:
                    error_message = response.json().get('message', 'The endpoint did not pass the health check.')

                except ValueError:
                    error_message = "Received a non-JSON response from the health check endpoint."

                messages.error(request, f"Health check failed: {error_message}")
                return redirect('connections:orchestration_create')

        except requests.RequestException as e:
            messages.error(request, f"Could not connect to the endpoint. Please check the URL and network: {e}")
            return redirect('connections:orchestration_create')

        try:
            new_connection = OrchestrationConnection(
                connection_endpoint=connection_endpoint,
                connection_is_public=connection_is_public,
                connection_api_key=connection_api_key
            )
            new_connection.save()

        except Exception as e:
            logger.error(f"Error creating Orchestration connection: {e}")
            messages.error(request, f"Error creating Orchestration connection: {e}")
            return redirect('connections:orchestration_create')

        messages.success(request, "Orchestration connection created successfully.")
        return redirect('connections:orchestration_create')
