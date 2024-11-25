#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: create_metatempo_connection_views.py
#  Last Modified: 2024-10-30 00:37:58
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:37:58
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

import requests
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from apps.metatempo.models import MetaTempoConnectionConfiguration
from config.settings import SERVER_BASE_URL


class MetaTempoView_ConnectionCreate(View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        connection_api_key = request.POST.get('connection_api_key')
        user_auth_key = request.POST.get('user_auth_key')

        try:
            mainframe_url = f"{SERVER_BASE_URL}/app/metatempo/tempo/connection/config/"

            response = requests.post(
                mainframe_url,
                data={
                    'api_key': connection_api_key
                }
            )

            if response.status_code != 200:
                messages.error(request, "Failed to fetch data from the mainframe server.")
                return redirect("metatempo:connections_manage")

            response_json = response.json()

            try:
                data = response_json.get('data')

            except Exception as e:
                error = response_json.get('error', "Failed to fetch data from the mainframe server.")
                messages.error(request, error)
                return redirect("metatempo:connections_manage")

            connection, created = MetaTempoConnectionConfiguration.objects.get_or_create(
                defaults={
                    'connection_api_key': connection_api_key,
                    'user_auth_key': user_auth_key,
                    'is_tracking_active': data.get(
                        'is_tracking_active',
                        True
                    ),
                    'member_log_intervals': data.get(
                        'member_log_intervals'
                    ),
                    'tracked_weekdays': data.get(
                        'tracked_weekdays', []
                    ),
                    'tracking_start_time': data.get(
                        'tracking_start_time'
                    ),
                    'tracking_end_time': data.get(
                        'tracking_end_time'
                    )
                }
            )

            if not created:
                connection.connection_api_key = connection_api_key
                connection.user_auth_key = user_auth_key
                connection.is_tracking_active = data.get(
                    'is_tracking_active',
                    True
                )
                connection.member_log_intervals = data.get(
                    'member_log_intervals'
                )
                connection.tracked_weekdays = data.get(
                    'tracked_weekdays', []
                )
                connection.tracking_start_time = data.get(
                    'tracking_start_time'
                )
                connection.tracking_end_time = data.get(
                    'tracking_end_time'
                )
                connection.save()

        except Exception as e:
            messages.error(request, "Failed to create or update MetaTempo connection: " + str(e))
            return redirect("metatempo:connections_manage")

        messages.success(request, "MetaTempo connection updated successfully.")
        return redirect("metatempo:connections_manage")
