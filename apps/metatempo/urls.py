#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-30 00:36:40
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:36:41
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.urls import path

from apps.metatempo.views import (MetaTempoView_ConnectionCreate, MetaTempoView_ConnectionDelete,
                                  MetaTempoView_ConnectionManage)

app_name = 'metatempo'

urlpatterns = [
    path('board/connection/create/', MetaTempoView_ConnectionCreate.as_view(), name='connection_create'),
    path('board/connection/delete/', MetaTempoView_ConnectionDelete.as_view(), name='connection_delete'),
    path('board/connections/manage/', MetaTempoView_ConnectionManage.as_view(
        template_name='metatempo/metatempo_board_connection.html'
    ), name='connections_manage'),
]
