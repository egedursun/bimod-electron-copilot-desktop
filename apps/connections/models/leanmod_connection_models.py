#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: leanmod_connection_models.py
#  Last Modified: 2024-10-25 15:15:11
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 21:58:16
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
#

from django.db import models


class LeanmodConnection(models.Model):
    connection_endpoint = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
        unique=True
    )
    connection_is_public = models.BooleanField(default=False)
    connection_api_key = models.CharField(
        max_length=10000,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.connection_endpoint + " - " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "LeanMod Connection"
        verbose_name_plural = "LeanMod Connections"
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=[
                    "created_at"
                ]
            ),
        ]
