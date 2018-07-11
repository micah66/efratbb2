from django.contrib import admin
from .models import D1_Team, D1_Game, D2_Team, D2_Game, D3_Team, D3_Game
# Register your models here.
admin.site.register(D1_Team)
admin.site.register(D1_Game)
admin.site.register(D2_Team)
admin.site.register(D2_Game)
admin.site.register(D3_Team)
admin.site.register(D3_Game)
