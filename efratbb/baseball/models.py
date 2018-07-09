from django.db import models

# Create your models here.
class Game(models.Model):
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
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('1:00', '1:00'),
        ('1:30', '1:30'),
        ('2:00', '2:00'),
        ('2:30', '2:30'),
        ('3:00', '3:00'),
        ('3:30', '3:30'),
        ('4:00', '4:00'),
        ('4:30', '4:30'),
        ('5:00', '5:00'),
        ('5:30', '5:30'),
        ('6:00', '6:00'),
        ('6:30', '6:30'),
        ('7:00', '7:00'),
        ('7:30', '7:30'),
        ('8:00', '8:00')
    ]
    month = models.CharField('Month', max_length=4, choices=months)
    day = models.IntegerField('Day')
    time = models.CharField('Game Time', max_length=5, choices=times )
    away_team = models.CharField('Away Team', max_length=30)
    home_team = models.CharField('Home Team', max_length=30)
    away_team_score = models.IntegerField('Away Team Score')
    home_team_score = models.IntegerField('Home Team Score')

    def __str__(self):
        return '{0} @ {1} - {2}, {3}'.format(self.away_team, self.home_team, self.month, self.day)
