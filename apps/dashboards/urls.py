#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 20:28:32
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:28:32
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.urls import path

from apps.dashboards.views import (DashboardView_Assistant, DashboardView_Leanmod, DashboardView_Orchestration,
                                   DashboardView_Index)

app_name = 'dashboards'

urlpatterns = [
    path("", DashboardView_Index.as_view(template_name='dashboards/index.html'), name='index'),
    path('assistant/', DashboardView_Assistant.as_view(template_name='dashboards/assistant_dashboard.html'),
         name='assistant_dashboard'),
    path('leanmod/', DashboardView_Leanmod.as_view(template_name='dashboards/leanmod_dashboard.html'),
         name='leanmod_dashboard'),
    path('orchestration/',
         DashboardView_Orchestration.as_view(template_name='dashboards/orchestration_dashboard.html'),
         name='orchestration_dashboard'),
]
