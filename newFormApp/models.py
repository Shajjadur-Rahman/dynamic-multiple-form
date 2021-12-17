from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=256, null=False, unique=True, verbose_name="Team Name")
    team_desc = models.CharField(max_length=512, null=True, verbose_name="Team Description")

    def __str__(self):
        return self.team_name


class Venue(models.Model):
    venue_name = models.CharField(max_length=256, null=False, unique=True, verbose_name="Venue Name")
    venue_desc = models.CharField(max_length=512, null=True, verbose_name="Venue Description")

    def __str__(self):
        return self.venue_name


class ScheduleMonth(models.Model):
    month_name = models.CharField(max_length=256, null=False, unique=True, verbose_name="Month Name")
    month_desc = models.CharField(max_length=512, null=True, verbose_name="Month Description")

    def __str__(self):
        return self.month_name


class ScheduleYear(models.Model):
    year_name = models.IntegerField(null=False, unique=True, verbose_name="Year Name")
    year_desc = models.CharField(max_length=512, null=True, verbose_name="Year Description")

    def __str__(self):
        return str(self.year_name)


class MatchScheduleWrap(models.Model):
    schedule_title = models.CharField(max_length=512, null=True, verbose_name="Schedule Title") #Also Meta Title
    def __str__(self):
        return self.schedule_title


class ScheduleTeam(models.Model):
    schedule = models.ForeignKey(MatchScheduleWrap, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    team_squad = models.CharField(max_length=1024, null=True, verbose_name="Team Squad")

    def __str__(self):
        return str(self.pk)

class ScheduleList(models.Model):
    schedule = models.ForeignKey(MatchScheduleWrap, on_delete=models.CASCADE)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='team_one', verbose_name="Team One")
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='team_two', verbose_name="Team Two")
    match_venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Match Venue")


    def __str__(self):
        return str(self.pk)