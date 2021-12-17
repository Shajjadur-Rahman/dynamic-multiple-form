from django.contrib import admin
from .models import (
    Team,
    Venue,
    ScheduleMonth,
    ScheduleYear,
    MatchScheduleWrap,
    ScheduleTeam,
    ScheduleList
)

admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(ScheduleMonth)
admin.site.register(ScheduleYear)
admin.site.register(MatchScheduleWrap)
admin.site.register(ScheduleTeam)
admin.site.register(ScheduleList)

