#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: leanmod_chat_message_models.py
#  Last Modified: 2024-10-25 15:54:19
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:35:57
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

from apps.chats.utils import CHAT_ROLES, ChatRolesNames


class MultimodalLeanmodChatMessage(models.Model):
    chat = models.ForeignKey('chats.MultimodalLeanmodChat', on_delete=models.CASCADE, related_name='leanmod_messages')
    message_role = models.CharField(max_length=200, choices=CHAT_ROLES, default=ChatRolesNames.SYSTEM)

    message_text = models.TextField(blank=True, null=True)
    message_file_uris = models.TextField(blank=True, null=True)
    message_image_uris = models.TextField(blank=True, null=True)

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_role + " - " + self.sent_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "Multimodal LeanMod Chat Message"
        verbose_name_plural = "Multimodal LeanMod Chat Messages"
        ordering = ["-sent_at"]
        indexes = [
            models.Index(fields=["sent_at"]),
        ]
