from django.contrib import admin
from .models import Enigma
from .models import Contestant

admin.site.register(Enigma)
admin.site.register(Contestant)