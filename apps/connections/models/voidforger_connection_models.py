#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: voidforger_connection_models.py
#  Last Modified: 2024-11-24 23:57:30
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-24 23:57:31
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.db import models


class VoidForgerConnection(models.Model):
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
        verbose_name = "VoidForger Connection"
        verbose_name_plural = "VoidForger Connections"
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=[
                    "created_at"
                ]
            ),
        ]
