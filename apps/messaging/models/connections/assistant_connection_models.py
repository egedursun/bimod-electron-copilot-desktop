#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: assistant_connection_models.py
#  Last Modified: 2024-10-25 04:27:28
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:27:28
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models


class AssistantConnection(models.Model):
    connection_endpoint = models.CharField(max_length=10000, null=True, blank=True)
    connection_is_public = models.BooleanField(default=False)
    connection_api_key = models.CharField(max_length=10000, null=True, blank=True)

    connection_agent_name = models.CharField(max_length=10000, null=True, blank=True)
    connection_agent_description = models.CharField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.connection_endpoint + " - " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "Assistant Connection"
        verbose_name_plural = "Assistant Connections"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]
