#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_assistant_connection_views.py
#  Last Modified: 2024-10-25 19:14:24
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:06:55
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

from apps.connections.models import AssistantConnection
from web_project import TemplateLayout

logger = logging.getLogger(__name__)


class ConnectionView_AssistantCreate(TemplateView):
    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['default_connection_is_public'] = False
        return context

    def post(self, request, *args, **kwargs):
        connection_endpoint = request.POST.get('connection_endpoint')
        connection_is_public = request.POST.get('connection_is_public', 'off') == 'on'
        connection_api_key = request.POST.get('connection_api_key') if not connection_is_public else None

        if "export_assistants" not in connection_endpoint:
            messages.error(request, "Assistant connection endpoint must contain 'export_assistants'.")
            return redirect('connections:assistant_create')

        if not connection_endpoint:
            messages.error(request, "Assistant connection endpoint is required.")
            return redirect('connections:assistant_create')

        if not connection_is_public and not connection_api_key:
            messages.error(request, "API key is required when Assistant connection is not public.")
            return redirect('connections:assistant_create')

        health_check_url = connection_endpoint.replace("app", "health")
        if health_check_url.endswith("/"):
            health_check_url = health_check_url[:-1]
        if connection_api_key and "Bearer" not in connection_api_key:
            connection_api_key = f"Bearer {connection_api_key}"
        headers = {"Authorization": f"{connection_api_key}"} if connection_api_key else {}
        try:
            response = requests.post(health_check_url, headers=headers)
            if response.status_code != 200:
                try:
                    error_message = response.json().get('message', 'The endpoint did not pass the health check.')
                except ValueError:
                    error_message = "Received a non-JSON response from the health check endpoint."
                messages.error(request, f"Health check failed: {error_message}")
                return redirect('connections:assistant_create')
        except requests.RequestException as e:
            messages.error(request, f"Could not connect to the endpoint. Please check the URL and network: {e}")
            return redirect('connections:assistant_create')

        try:
            new_connection = AssistantConnection(
                connection_endpoint=connection_endpoint, connection_is_public=connection_is_public,
                connection_api_key=connection_api_key
            )
            new_connection.save()
        except Exception as e:
            logger.error(f"Error creating Assistant connection: {e}")
            messages.error(request, f"Error creating Assistant connection: {e}")
            return redirect('connections:assistant_create')

        messages.success(request, "Assistant connection created successfully.")
        return redirect('connections:assistant_create')
