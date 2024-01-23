from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_name, name='user_name'),
    path('user/search', views.user_by_name, name='user_by_name'),
]