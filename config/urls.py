#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 16:23:14
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 18:54:50
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import admin
from django.urls import include, path
from apps.dashboards.views import DashboardView_Index

urlpatterns = [
    path("admin/", admin.site.urls),
    ########################################
    path("", DashboardView_Index.as_view(template_name="dashboards/index.html"), name="index"),
    path("dashboards/", include("apps.dashboards.urls")),
    path("connections/", include("apps.connections.urls")),
    path("chats/", include("apps.chats.urls")),
    path("copilot/", include("apps.copilot.urls")),
    path("metakanban/", include("apps.metakanban.urls")),
    ########################################
]
