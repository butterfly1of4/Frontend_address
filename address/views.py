from django.shortcuts import render
from .models import User, Contact
# Create your views here.


#USER LIST
def user_list(request):
    users= User.objects.all()
    return render(request, 'address/user_list.html', {'users': users})

def user_info(request,pk):
    user = User.objects.get(id=pk)
    return render(request, 'address/user_info.html', {'user':user})
# #CONTACT LIST
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'address/contact_list.html', {'contacts': contacts})

def contact_info(request,pk):
    contact =  Contact.objects.get(id=pk)
    return render(request, 'address/contact_info.html', {'contact': contact})