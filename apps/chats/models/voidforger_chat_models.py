#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: voidforger_chat_models.py
#  Last Modified: 2024-11-25 00:42:07
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-11-25 00:42:07
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models


class MultimodalVoidForgerChat(models.Model):
    uuid = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )
    connection = models.ForeignKey(
        'connections.VoidForgerConnection',
        on_delete=models.CASCADE,
        related_name='multimodal_voidforger_chats',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uuid}" + " - " + f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Multimodal VoidForger Chat"
        verbose_name_plural = "Multimodal VoidForger Chats"
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=[
                    "created_at"
                ]
            ),
        ]
