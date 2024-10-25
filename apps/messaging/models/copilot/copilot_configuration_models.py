#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_configuration_models.py
#  Last Modified: 2024-10-25 04:28:20
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:28:20
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.db import models

from apps.messaging.utils import CONNECTION_TYPES, ConnectionTypesNames


class ElectronCopilotConfiguration(models.Model):
    is_active = models.BooleanField(default=True)
    connection_type_selection = models.CharField(
        max_length=255, choices=CONNECTION_TYPES, default=ConnectionTypesNames.ASSISTANT)

    assistant_connection = models.ForeignKey(
        'messaging.AssistantConnection', on_delete=models.CASCADE, null=True, blank=True,
        related_name="assistant_connection")
    leanmod_connection = models.ForeignKey(
        'messaging.LeanmodConnection', on_delete=models.CASCADE, null=True, blank=True,
        related_name="leanmod_connection")
    orchestration_connection = models.ForeignKey(
        'messaging.OrchestrationConnection', on_delete=models.CASCADE, null=True, blank=True,
        related_name="orchestration_connection")

    assistant_chat = models.ForeignKey(
        'messaging.MultimodalAssistantChat', on_delete=models.CASCADE, null=True, blank=True,
        related_name="assistant_chat")
    leanmod_chat = models.ForeignKey(
        'messaging.MultimodalLeanmodChat', on_delete=models.CASCADE, null=True, blank=True,
        related_name="leanmod_chat")
    orchestration_chat = models.ForeignKey(
        'messaging.MultimodalOrchestrationChat', on_delete=models.CASCADE, null=True, blank=True,
        related_name="orchestration_chat")

    last_toggled_is_active_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.connection_type_selection + " - " + self.last_toggled_is_active_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name = "Electron Copilot Configuration"
        verbose_name_plural = "Electron Copilot Configurations"
        ordering = ["-last_toggled_is_active_at"]
        indexes = [
            models.Index(fields=["last_toggled_is_active_at"]),
        ]
