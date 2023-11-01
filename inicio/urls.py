from django.urls import path
from inicio.views import inicio,conciertos, crear_conciertos

urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('conciertos/', conciertos, name='conciertos'),
    path('conciertos/crear/', crear_conciertos, name='crear_concierto'),
]
