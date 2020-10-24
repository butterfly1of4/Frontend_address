from django.shortcuts import render
from .models import User, Contact
# Create your views here.


#USER LIST
def user_list(request):
    users= User.objects.all()
    return render(request, 'address/user_list.html', {'users': users})

def user_detail(request,unique):
    user = User.objects.get(unique=True)
    return render(request, 'address/user_detail.html', {'user':user})

#CONTACT LIST
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'address/contact_list.html', {'contacts': contacts})