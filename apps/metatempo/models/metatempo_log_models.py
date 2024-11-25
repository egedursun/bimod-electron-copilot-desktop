#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: metatempo_log_models.py
#  Last Modified: 2024-10-30 00:37:19
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:37:19
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

import uuid

from django.db import models


class MetaTempoLogRecord(models.Model):
    identifier_uuid = models.UUIDField(default=uuid.uuid4)
    screenshot_image_png = models.ImageField(
        upload_to='metatempo/logs/',
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    is_sent_successfully = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.identifier_uuid} - {self.timestamp}'

    class Meta:
        db_table = 'metatempo_log_record'
        verbose_name = 'MetaTempo Log Record'
        verbose_name_plural = 'MetaTempo Log Records'
        ordering = ['-timestamp']
        indexes = [
            models.Index(
                fields=[
                    'identifier_uuid'
                ]
            ),
            models.Index(
                fields=[
                    'timestamp'
                ]
            ),
        ]
