from django.urls import path
from . import views

urlpatterns = [
    # path('', views.MatchScheduleWrapView.as_view(), name='create-match-schedule')
    path('', views.match_schedule_wrap, name='create-match-schedule'),
    # path('', views.match_schedule_wrap2, name='create-match-schedule2'),

]