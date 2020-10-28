from django.urls import path
from . import views

urlpatterns = [
    # #USER URLS
    path('', views.user_list, name='user_list'),
#     path('users/<int:pk>', views.user_info, name='user_info'),
#     # #CONTACT URLS
    path('contacts/', views.contact_list, name='contact_list'),
#     path('contacts/<int:pk>', views.contact_info, name='contact_info')
]
