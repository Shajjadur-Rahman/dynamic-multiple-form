from django.shortcuts import render
from django.views import generic
# from django.forms import formset_factory
from django.forms import modelformset_factory
from .models import MatchScheduleWrap, ScheduleTeam, ScheduleList
from .forms import (
    TeamForm,
    VenueForm,
    ScheduleMonthForm,
    ScheduleYearForm,
    MatchScheduleWrapForm,
    ScheduleTeamForm,
    ScheduleListForm
)
from django.db import transaction, IntegrityError




def match_schedule_wrap(request):
    match_scheduler_form = MatchScheduleWrapForm()
    schedule_team_formset = modelformset_factory(ScheduleTeam, form=ScheduleTeamForm, extra=0)
    schedule_list_formset = modelformset_factory(ScheduleList, form=ScheduleListForm, extra=0)

    if request.method == "POST":
        match_scheduler_form = MatchScheduleWrapForm(request.POST or None)
        st_formset = schedule_team_formset(request.POST or None, queryset=ScheduleTeam.objects.none())
        sl_formset = schedule_list_formset(request.POST or None, queryset=ScheduleList.objects.none())
        if match_scheduler_form.is_valid() and st_formset.is_valid() and sl_formset.is_valid():
            form_instance = match_scheduler_form.save(commit=False)
            form_instance.save()
            for st in st_formset:
                data = st.save(commit=False)
                data.schedule_id=form_instance.id
                data.save()
            for sl in sl_formset:
                data2 = sl.save(commit=False)
                data2.schedule_id=form_instance.id
                data2.save()

    context = {
        'match_scheduler_form': match_scheduler_form,
        'st_formset': schedule_team_formset(queryset= ScheduleTeam.objects.none()),
        'sl_formset': schedule_list_formset(queryset= ScheduleList.objects.none())
    }

    return render(request, 'form.html', context=context)

