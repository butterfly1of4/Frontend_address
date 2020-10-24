from django.urls import path
from . import views

urlpatterns = [
    #USER URLS
    path('', views.user_list, name='user_list'),
    #CONTACT URLS
    path('/contacts', views.contact_list, name='contact_list'),
]