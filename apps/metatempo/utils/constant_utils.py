#  Copyright (c) 2024 BMD™ Autonomous Holdings. All rights reserved.
#
#  Project: Bimod.io™
#  File: constant_utils.py
#  Last Modified: 2024-10-30 00:35:39
#  Author: Ege Dogan Dursun (Co-Founder & Chief Executive Officer / CEO @ BMD™ Autonomous Holdings)
#  Created: 2024-10-30 00:35:39
#
#  This software is proprietary and confidential. Unauthorized copying,
#  distribution, modification, or use of this software, whether for
#  commercial, academic, or any other purpose, is strictly prohibited
#  without the prior express written permission of BMD™ Autonomous
#  Holdings.
#
#   For permission inquiries, please contact: admin@Bimod.io.


METATEMPO_MEMBER_LOG_INTERVALS = [
    ('times_12_per_hour', '12 Times Per Hour'),
    ('times_6_per_hour', '6 Times Per Hour'),
    ('times_4_per_hour', '4 Times Per Hour'),
    ('times_3_per_hour', '3 Times Per Hour'),
    ('times_2_per_hour', '2 Times Per Hour'),
    ('hourly', 'Hourly'),
    ('every_2_hours', 'Every 2 Hours'),
    ('every_4_hours', 'Every 4 Hours'),
]


class MetaTempoMemberLogIntervalsNames:
    TIMES_12_PER_HOUR = 'times_12_per_hour'
    TIMES_6_PER_HOUR = 'times_6_per_hour'
    TIMES_4_PER_HOUR = 'times_4_per_hour'
    TIMES_3_PER_HOUR = 'times_3_per_hour'
    TIMES_2_PER_HOUR = 'times_2_per_hour'
    HOURLY = 'hourly'
    EVERY_2_HOURS = 'every_2_hours'
    EVERY_4_HOURS = 'every_4_hours'

    @staticmethod
    def as_list():
        return [MetaTempoMemberLogIntervalsNames.TIMES_12_PER_HOUR,
                MetaTempoMemberLogIntervalsNames.TIMES_6_PER_HOUR,
                MetaTempoMemberLogIntervalsNames.TIMES_4_PER_HOUR,
                MetaTempoMemberLogIntervalsNames.TIMES_3_PER_HOUR,
                MetaTempoMemberLogIntervalsNames.TIMES_2_PER_HOUR,
                MetaTempoMemberLogIntervalsNames.HOURLY,
                MetaTempoMemberLogIntervalsNames.EVERY_2_HOURS,
                MetaTempoMemberLogIntervalsNames.EVERY_4_HOURS]


META_TEMPO_CONNECTION_CONFIGURATION_ADMIN_LIST = ('is_tracking_active', 'member_log_intervals', 'tracking_start_time', 'tracking_end_time')
META_TEMPO_CONNECTION_CONFIGURATION_ADMIN_FILTER = ('is_tracking_active', 'member_log_intervals', 'tracking_start_time', 'tracking_end_time')
META_TEMPO_CONNECTION_CONFIGURATION_ADMIN_SEARCH = ('is_tracking_active', 'member_log_intervals', 'tracking_start_time', 'tracking_end_time')
META_TEMPO_LOG_RECORD_ADMIN_LIST = ('identifier_uuid', 'timestamp')
META_TEMPO_LOG_RECORD_ADMIN_FILTER = ('timestamp',)
META_TEMPO_LOG_RECORD_ADMIN_SEARCH = ('identifier_uuid', 'timestamp')
