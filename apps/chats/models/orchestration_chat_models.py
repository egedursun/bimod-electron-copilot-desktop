#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: orchestration_chat_models.py
#  Last Modified: 2024-10-25 15:54:19
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 21:02:09
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
#
#  Project: Bimod.io™
#  File: orchestration_chat_models.py
#  Last Modified: 2024-10-25 15:42:39
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 15:42:41
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models


class MultimodalOrchestrationChat(models.Model):
    uuid = models.CharField(max_length=1000, null=True, blank=True)
    connection = models.ForeignKey('connections.OrchestrationConnection', on_delete=models.CASCADE,
                                   related_name='multimodal_orchestration_chats', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uuid + " - " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "Multimodal Orchestration Chat"
        verbose_name_plural = "Multimodal Orchestration Chats"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]
