***URLS.PY***
from django.urls import path
from . import views
from rest_framework import views


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








***VIEWS***  

#USER VIEWS
#USER CREATE/POST
def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user =  form.save()
            return redirect('user_info', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'address/user_form.html', {'form': form})
 
#USER EDIT
def user_edit(request, pk):
    user= User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user=form.save()
            return redirect('user_info', pk=user.pk)
    else:
        form = UserForm(instance=user)
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

#USER DELETE
def user_delete(request,pk):
    User.objects.get(id=pk).delete()
    return redirect('user_list')


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
    return render(request, 'address/contact_form.html', {'form': form})

#CONTACT EDIT
def contact_edit(request,pk):
    contact=Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form=ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact=form.save()
            return render(request, 'address/contact_form.html', {'form': form})
    else:
        form = ContactForm(instance=contact)
    return render(request, 'address/contact_edit.html', {'form': form})
# #CONTACT LIST
#GET ALL
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'address/contact_list.html', {'contacts': contacts})

#GET ONE
def contact_info(request,pk):
    contact =  Contact.objects.get(id=pk)
    return render(request, 'address/contact_info.html', {'contact': contact})

#CONTACT DELETE
def contact_delete(request,pk):
    Contact.objects.get(id=pk).delete()
    return redirect('contact_list')      
       
########################
       
        "contact_home_address": "706 Azalea dr. Rockville, MD 20850",

        "contact_home_address": "567 Grant st, Chicago, IL  534543",

        "contact_home_address": "4186 Palomino ln, Middletown, MD 21769",
            "contact_home_address": "4186 Palomino ln, Middletown, MD 21769",



  [  {"model": "address.User",
  
    "fields": {
        "userName": "goodbyee",
        "userEmail":"helpMe@gmail.com",
        "password": "helpMe"
    }},
    {"model": "address.User",
  
        "fields": {
            "userName": "hellooo",
            "userEmail":"jhouck29@gmail.com",
            "password": "address"
        }}
    ,{     
        "model": "address.Contact",
        "fields": {
     "id
: 3            "contactEmail": "judythouck@gmail.com",
            "firstName":"Judy",
            "lastName": "Houck",
            "phone_number": "3014445555",
            "contactAddress": "4186 Palomino ln, Middletown, MD 21769",
            "relation": "Mother",
            "group": "Family",
            "age": "69",
            "notes": "This is my mother!"
    }
},
{
    "model": "address.Contact",

    "fields": {
 "id
: 3        "contactEmail": "lee@gmail.com",
        "firstName":"Lee",
        "lastName": "Houck",
        "phone_number": "3015556666",
        "contactAddress": "4186 Palomino ln, Middletown, MD 21769",
        "relation": "Father",
        "group": "Family",
        "age": "72",
        "notes": "This is Dad!"
    }
},
{
    "model": "address.Contact",

    "fields": {
         "id: 3        
         "contactEmail": "aimee@gmail.com",
        "firstName":"Aimee",
        "lastName": "Houck",
        "phone_number": "3015552222",
        "contactAddress": "567 Grant st, Chicago, IL  534543",
        "relation": "Sister",
        "group": "Family",
        "age": "32",
        "notes": "This is my sister!"
    }
},
{
    "model": "address.Contact",

 
    "fields": {
 "id
: 4       "contactEmail": "arthur@gmail.com",
        "firstName":"Arthur",
        "lastName": "Shmidt",
        "phone_number": "2408885454",
        "contactAddress": "706 Azalea dr. Rockville, MD 20850",
        "relation": "Fiancee",
        "group": "Family",
        "age": "37",
        "notes": "This is who I'm marrying!"
    }
}
]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default="user")
    contactEmail = models.CharField(max_length=300, default='contactemail', unique=True)
    firstName = models.CharField(max_length=200, default="first")
    lastName = models.CharField(max_length=300, default="last")
  phone_number = PhoneNumberField(default=int())
    contactAddress = models.TextField(default="address")
    relation = models.CharField(max_length = 200, default="relation")
    group = models.CharField(max_length=300, default="group")
    age = models.CharField(max_length=5, default='age')
    notes= models.TextField(default="notes")





