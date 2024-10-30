#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: metatempo_connection_update_middleware.py
#  Last Modified: 2024-10-30 01:51:38
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 01:51:39
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
import requests

from apps.metatempo.models import MetaTempoConnectionConfiguration
from config import settings


class MetaTempoConnectionUpdateMiddleware:
    _has_run_once = False

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if we've already run the update logic once
        if not MetaTempoConnectionUpdateMiddleware._has_run_once:
            self.update_metatempo_connection()
            MetaTempoConnectionUpdateMiddleware._has_run_once = True

        response = self.get_response(request)
        return response

    def update_metatempo_connection(self):
        """ Function to initialize or update MetaTempo connection at first request after application startup. """
        try:
            connection = MetaTempoConnectionConfiguration.objects.first()
            if connection:
                mainframe_url = f"{settings.SERVER_BASE_URL}/app/metatempo/tempo/connection/config/"
                response = requests.post(mainframe_url, data={'api_key': connection.connection_api_key})

                if response.status_code == 200:
                    data = response.json().get('data', {})
                    connection.is_tracking_active = data.get('is_tracking_active', True)
                    connection.member_log_intervals = data.get('member_log_intervals')
                    connection.tracked_weekdays = data.get('tracked_weekdays', [])
                    connection.tracking_start_time = data.get('tracking_start_time')
                    connection.tracking_end_time = data.get('tracking_end_time')
                    connection.save()
                    print(f"""
                        ================================================================
                        || SUCCESS: [ MetaTempo connection updated successfully. ]
                        ================================================================
                    """)
                else:
                    print("Failed to fetch data from the mainframe server.")
            else:
                print(f"""
                ================================================================
                || SUCCESS: [ No active MetaTempo connections at the moment. ]
                ================================================================
                """)
        except Exception as e:
            print(f"Failed to update MetaTempo connection: {e}")
