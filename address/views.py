from django.shortcuts import render, redirect
from .models import User, Contact
from .forms import UserForm, ContactForm


# Create your views here.


#USER VIEWS
#USER CREATE/POST

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user =  form.save()
            return redirect('user_info', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'address/user_form.html', {'form': form})
            
#USER LIST/GET
#GET ALL
def user_list(request):
    users= User.objects.all()
    return render(request, 'address/user_list.html', {'users': users})
#GET ONE
def user_info(request,pk):
    user = User.objects.get(id=pk)
    return render(request, 'address/user_info.html', {'user':user})


#CONTACT VIEWS
#CONTACT CREATE/POST
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return  redirect('conact_info', pk=contact.pk)
    else:   
        form = ContactForm()
    return render(request, 'address/contact_info.html', {'form': form})

# #CONTACT LIST
#GET ALL
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'address/contact_list.html', {'contacts': contacts})

#GET ONE
def contact_info(request,pk):
    contact =  Contact.objects.get(id=pk)
    return render(request, 'address/contact_info.html', {'contact': contact})