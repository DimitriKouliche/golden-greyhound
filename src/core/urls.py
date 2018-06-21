from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^enigma/', include('enigma.urls', namespace='enigma')),
    url(r'^admin/', include(admin.site.urls)),
]
