from django.urls import path, include
from passman import urls as passman_urls


urlpatterns = [
    path('passman/', include(passman_urls))
]
