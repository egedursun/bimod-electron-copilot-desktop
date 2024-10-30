#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: metatempo_log_admin.py
#  Last Modified: 2024-10-30 00:37:41
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:37:41
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


from django.contrib import admin

from apps.metatempo.models import MetaTempoLogRecord
from apps.metatempo.utils import META_TEMPO_LOG_RECORD_ADMIN_LIST, META_TEMPO_LOG_RECORD_ADMIN_FILTER, \
    META_TEMPO_LOG_RECORD_ADMIN_SEARCH


@admin.register(MetaTempoLogRecord)
class MetaTempoLogRecordAdmin(admin.ModelAdmin):
    list_display = META_TEMPO_LOG_RECORD_ADMIN_LIST
    list_filter = META_TEMPO_LOG_RECORD_ADMIN_FILTER
    search_fields = META_TEMPO_LOG_RECORD_ADMIN_SEARCH
    ordering = ('-timestamp',)
