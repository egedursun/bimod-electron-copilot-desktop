#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: copilot_configuration_models.py
#  Last Modified: 2024-10-25 22:54:57
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 22:54:58
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models

from apps.copilot.utils import COPILOT_CONNECTION_TYPES, CopilotConnectionTypesNames


class CopilotModal(models.Model):
    is_active = models.BooleanField(default=True)
    active_connection_type = models.CharField(
        max_length=255,
        choices=COPILOT_CONNECTION_TYPES,
        default=CopilotConnectionTypesNames.VOIDFORGER
    )

    selected_assistant = models.ForeignKey(
        'connections.AssistantConnection',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_leanmod = models.ForeignKey(
        'connections.LeanmodConnection',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_orchestration = models.ForeignKey(
        'connections.OrchestrationConnection',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_voidforger = models.ForeignKey(
        'connections.VoidForgerConnection',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    #####

    selected_assistant_chat = models.ForeignKey(
        'chats.MultimodalAssistantChat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_leanmod_chat = models.ForeignKey(
        'chats.MultimodalLeanmodChat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_orchestration_chat = models.ForeignKey(
        'chats.MultimodalOrchestrationChat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    selected_voidforger_chat = models.ForeignKey(
        'chats.MultimodalVoidForgerChat',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    last_toggled_is_active_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.active_connection_type} - {self.is_active}'

    class Meta:
        verbose_name = 'Copilot Modal'
        verbose_name_plural = 'Copilot Modals'
