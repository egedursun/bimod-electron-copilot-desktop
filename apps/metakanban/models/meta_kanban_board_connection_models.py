#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: meta_kanban_board_connection_models.py
#  Last Modified: 2024-10-28 15:51:32
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-28 15:51:32
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.db import models


class MetaKanbanBoardConnection(models.Model):
    board_connection_api_key = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.board_connection_api_key

    class Meta:
        db_table = 'meta_kanban_board_connection'
        verbose_name = 'Meta Kanban Board Connection'
        verbose_name_plural = 'Meta Kanban Board Connections'
        indexes = [
            models.Index(fields=['board_connection_api_key']),
            models.Index(fields=['created_at']),
        ]
