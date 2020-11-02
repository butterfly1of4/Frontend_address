from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    #HOME URL
    #path('', views.user_list, name="home")
     
    #USER SERIALIZER PATHS
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserInfo.as_view(), name = 'user_info'),
    
    # #USER URLS
    # path('users/', views.user_list, name='user_list'),
    # path('users/<int:pk>', views.user_info, name='user_info'),
    path('users/new', views.user_create, name='user_create'),
    path('users/<int:pk>/edit', views.user_edit, name='user_edit'),
    path('users/<int:pk>/delete', views.user_delete, name='user_delete'),
    
    #CONTACTT SERIALIZER PATHS  
    path('contacts/', views.ContactList.as_view(), name="contact_list"),
    path('contacts/<int:pk>', views.ContactInfo.as_view(), name="contact_info"),
    
    
     # #CONTACT URLS
    # path('contacts/', views.contact_list, name='contact_list'),
    # path('contacts/<int:pk>', views.contact_info, name='contact_info'),
    path('contacts/new', views.contact_create, name="contact_create"),
    path('contacts/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete', views.contact_delete, name="contact_delete")
]





