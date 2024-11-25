#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-28 15:48:55
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-28 15:49:02
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.urls import path

from apps.metakanban.views import (MetaKanbanView_BoardConnectionCreate, MetaKanbanView_BoardConnectionDelete,
                                   MetaKanbanView_BoardConnectionManage)

app_name = 'metakanban'

urlpatterns = [
    path(
        'board/connection/create/',
        MetaKanbanView_BoardConnectionCreate.as_view(),
        name='connection_create'
    ),

    path(
        'board/connection/delete/',
        MetaKanbanView_BoardConnectionDelete.as_view(),
        name='connection_delete'
    ),

    path(
        'board/connection/manage/',
        MetaKanbanView_BoardConnectionManage.as_view(
            template_name='metakanban/meta_kanban_board_connection.html'
        ),
        name='connection_manage'
    ),
]
