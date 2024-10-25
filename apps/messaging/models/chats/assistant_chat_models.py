#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: chat_models.py
#  Last Modified: 2024-10-25 04:28:04
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:28:04
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models


class MultimodalAssistantChat(models.Model):
    connection = models.ForeignKey('messaging.AssistantConnection', on_delete=models.CASCADE,
                                   related_name='multimodal_assistant_chats', null=True, blank=True)

    organization_name = models.CharField(max_length=10000, blank=True, null=True)
    agent_name = models.CharField(max_length=10000, blank=True, null=True)
    chat_name = models.CharField(max_length=10000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organization_name + " - " + self.agent_name + " - " + self.chat_name + " - " + self.created_at.strftime(
            "%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "Multimodal Assistant Chat"
        verbose_name_plural = "Multimodal Assistant Chats"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]
