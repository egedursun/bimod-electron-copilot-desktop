#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: urls.py
#  Last Modified: 2024-10-25 04:24:41
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-25 04:24:41
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.urls import path

from apps.messaging.views import (MessagingView_OrchestrationSendMessage, MessagingView_LeanmodSendMessage,
                                  MessagingView_AssistantSendMessage)

app_name = 'messaging'

urlpatterns = [
    path('assistant/send_message/<int:pk>/',
         MessagingView_AssistantSendMessage.as_view(), name='assistant_send_message'),
    path('leanmod/send_message/<int:pk>/',
         MessagingView_LeanmodSendMessage.as_view(), name='leanmod_send_message'),
    path('leanmod/send_message/<int:pk>/',
         MessagingView_OrchestrationSendMessage.as_view(), name='orchestration_send_message'),
]
