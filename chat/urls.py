
from django.urls import path, re_path
from chat import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<room_name>/<token>/', views.room, name='room'),
    path('centrifugo/connect/', views.connect, name='connect'),
    path('centrifugo/refresh/', views.refresh, name='connect'),
    path('centrifugo/subscribe/', views.subscribe, name='subscribe'),
    path('centrifugo/publish/', views.publish, name='publish'),
]
