#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 20:00:58
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 20:01:36
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.
from django.urls import path

from apps.connections.views import ConnectionView_AssistantCreate, ConnectionView_AssistantRemove, \
    ConnectionView_LeanmodCreate, ConnectionView_LeanmodRemove, ConnectionView_OrchestrationCreate, \
    ConnectionView_OrchestrationRemove

app_name = 'connections'

urlpatterns = [
    path('assistant/create/',
         ConnectionView_AssistantCreate.as_view(
             template_name='connections/create/create_assistant_connection.html'
         ), name='assistant_create'),
    path('assistant/remove/',
         ConnectionView_AssistantRemove.as_view(
             template_name='connections/remove/remove_assistant_connections.html'
         ), name='assistant_remove'),

    path('leanmod/create/',
         ConnectionView_LeanmodCreate.as_view(
             template_name='connections/create/create_leanmod_connection.html'
         ), name='leanmod_create'),
    path('leanmod/remove/',
         ConnectionView_LeanmodRemove.as_view(
             template_name='connections/remove/remove_leanmod_connections.html'
         ), name='leanmod_remove'),

    path('orchestration/create/',
         ConnectionView_OrchestrationCreate.as_view(
             template_name='connections/create/create_orchestration_connection.html'
         ), name='orchestration_create'),
    path('orchestration/remove/',
         ConnectionView_OrchestrationRemove.as_view(
             template_name='connections/remove/remove_orchestration_connections.html'
         ), name='orchestration_remove'),
]
