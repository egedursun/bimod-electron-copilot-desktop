#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: metatempo_connection_delete_views.py
#  Last Modified: 2024-10-30 00:38:24
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:38:25
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from apps.metatempo.models import MetaTempoConnectionConfiguration


class MetaTempoView_ConnectionDelete(View):

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        try:
            connection = get_object_or_404(MetaTempoConnectionConfiguration)
            connection.delete()

        except Exception as e:
            messages.error(request, "Failed to delete MetaTempo connection.")
            return redirect("metatempo:connections_manage")

        messages.success(request, "MetaTempo connection deleted successfully.")
        return redirect("metatempo:connections_manage")
