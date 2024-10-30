#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: metatempo_connection_models.py
#  Last Modified: 2024-10-30 00:37:13
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:37:13
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models
from apps.metatempo.utils import METATEMPO_MEMBER_LOG_INTERVALS, MetaTempoMemberLogIntervalsNames


class MetaTempoConnectionConfiguration(models.Model):
    is_tracking_active = models.BooleanField(default=True)
    member_log_intervals = models.CharField(max_length=1000, choices=METATEMPO_MEMBER_LOG_INTERVALS,
                                            default=MetaTempoMemberLogIntervalsNames.TIMES_6_PER_HOUR)
    tracked_weekdays = models.JSONField(blank=True, null=True)
    tracking_start_time = models.TimeField(blank=True, null=True)
    tracking_end_time = models.TimeField(blank=True, null=True)

    connection_api_key = models.CharField(max_length=10000, blank=True, null=True)
    user_auth_key = models.CharField(max_length=10000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.is_tracking_active}' + ' - ' + f'{self.member_log_intervals}' + ' - '

    class Meta:
        db_table = 'metatempo_board_connection'
        verbose_name = 'MetaTempo Connection Configuration'
        verbose_name_plural = 'MetaTempo Connection Configurations'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['is_tracking_active']),
            models.Index(fields=['member_log_intervals']),
            models.Index(fields=['connection_api_key']),
            models.Index(fields=['user_auth_key']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]
