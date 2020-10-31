from django.urls import path
from . import views

urlpatterns = [
    #HOME URL
    #path('', views.user_list, name="home")
    # #USER URLS
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>', views.user_info, name='user_info'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
    
    
     # #CONTACT URLS
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:pk>', views.contact_info, name='contact_info'),
    path('contacts/new', views.contact_create, name="contact_create"),
    path('contacts/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete', views.contact_delete, name="contact_delete")
]
