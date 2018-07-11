from django.db import models

# Create your models here.
class D1_Team(models.Model):
    team_name = models.CharField('Team Name', max_length=30)
    team_color = models.CharField('Team Color', max_length=30)

    def __str__(self):
        return '{}'.format(self.team_name)

class D1_Game(models.Model):
    months = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')
    ]
    times = [
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('11:45', '11:45'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('12:45', '12:45'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('1:45', '1:45'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('2:45', '2:45'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('3:45', '3:45'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('4:45', '4:45'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('5:45', '5:45'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('6:45', '6:45'),
        ('7:00', '7:00'),
        ('7:30', '7:30'),
        ('7:45', '7:45'),
        ('8:00', '8:00')
    ]
    month = models.CharField('Month', max_length=4, choices=months)
    day = models.IntegerField('Day')
    time = models.CharField('Game Time', max_length=5, choices=times )
    away_team = models.ForeignKey(D1_Team, related_name='away_games', default=None)
    home_team = models.ForeignKey(D1_Team, related_name='home_games', default=None)
    away_team_score = models.IntegerField('Away Team Score', blank=True, null=True)
    home_team_score = models.IntegerField('Home Team Score', blank=True, null=True)



    def __str__(self):
        return '{0} @ {1} - {2}, {3}'.format(self.away_team, self.home_team, self.month, self.day)
class D2_Team(models.Model):
    team_name = models.CharField('Team Name', max_length=30)
    team_color = models.CharField('Team Color', max_length=30)

    def __str__(self):
        return '{}'.format(self.team_name)

class D2_Game(models.Model):
    months = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')
    ]
    times = [
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('11:45', '11:45'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('12:45', '12:45'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('1:45', '1:45'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('2:45', '2:45'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('3:45', '3:45'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('4:45', '4:45'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('5:45', '5:45'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('6:45', '6:45'),
        ('7:00', '7:00'),
        ('7:30', '7:30'),
        ('7:45', '7:45'),
        ('8:00', '8:00')
    ]
    month = models.CharField('Month', max_length=4, choices=months)
    day = models.IntegerField('Day')
    time = models.CharField('Game Time', max_length=5, choices=times )
    away_team = models.ForeignKey(D2_Team, related_name='away_games', default=None)
    home_team = models.ForeignKey(D2_Team, related_name='home_games', default=None)
    away_team_score = models.IntegerField('Away Team Score', blank=True, null=True)
    home_team_score = models.IntegerField('Home Team Score', blank=True, null=True)



    def __str__(self):
        return '{0} @ {1} - {2}, {3}'.format(self.away_team, self.home_team, self.month, self.day)
class D3_Team(models.Model):
    team_name = models.CharField('Team Name', max_length=30)
    team_color = models.CharField('Team Color', max_length=30)

    def __str__(self):
        return '{}'.format(self.team_name)

class D3_Game(models.Model):
    months = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')
    ]
    times = [
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('11:45', '11:45'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('12:45', '12:45'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('1:45', '1:45'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('2:45', '2:45'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('3:45', '3:45'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('4:45', '4:45'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('5:45', '5:45'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('6:45', '6:45'),
        ('7:00', '7:00'),
        ('7:30', '7:30'),
        ('7:45', '7:45'),
        ('8:00', '8:00')
    ]
    month = models.CharField('Month', max_length=4, choices=months)
    day = models.IntegerField('Day')
    time = models.CharField('Game Time', max_length=5, choices=times )
    away_team = models.ForeignKey(D3_Team, related_name='away_games', default=None)
    home_team = models.ForeignKey(D3_Team, related_name='home_games', default=None)
    away_team_score = models.IntegerField('Away Team Score', blank=True, null=True)
    home_team_score = models.IntegerField('Home Team Score', blank=True, null=True)



    def __str__(self):
        return '{0} @ {1} - {2}, {3}'.format(self.away_team, self.home_team, self.month, self.day)
