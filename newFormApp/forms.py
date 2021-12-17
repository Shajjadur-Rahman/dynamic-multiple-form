from .models import (
    Team,
    Venue,
    ScheduleMonth,
    ScheduleYear,
    MatchScheduleWrap,
    ScheduleTeam,
    ScheduleList
)
from django import forms

class TeamForm(forms.ModelForm):
    class Meta:
        model  = Team
        fields = '__all__'

class VenueForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class ScheduleMonthForm(forms.ModelForm):
    class Meta:
        model  = ScheduleMonth
        fields = '__all__'


class ScheduleYearForm(forms.ModelForm):
    class Meta:
        model  = ScheduleYear
        fields = '__all__'


class MatchScheduleWrapForm(forms.ModelForm):
    class Meta:
        model  = MatchScheduleWrap
        fields = '__all__'

class ScheduleTeamForm(forms.ModelForm):
    class Meta:
        model  = ScheduleTeam
        fields = ['team', 'team_squad', ]


class ScheduleListForm(forms.ModelForm):
    class Meta:
        model  = ScheduleList
        fields = ['team_one', 'team_two', 'match_venue']

