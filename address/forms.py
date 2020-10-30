from django import forms
from .models import User, Contact


class UserForm(forms.ModelForm):
    
    class Meta:
            model= User
            fields = ('user_name', 'user_email', 'user_password')
            
class ContactForm(forms.ModelForm):
    
    class Meta:
            model = Contact
            fields = ('contact_user', 'contact_email', 'contact_first_name', 'contact_last_name', 'contact_phone_number', 'contact_home_address', 'contact_relation', 'contact_group', 'contact_age', 'contact_notes')