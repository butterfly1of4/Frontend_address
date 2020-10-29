from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    user_name = models.CharField(max_length=200, default="username", unique=True)
    user_email = models.CharField(max_length=400, default="email")
    user_password = models.CharField(max_length=300, default="password")


    def __str__(self):
        return self.user_name


# # NEW MODEL
class Contact(models.Model):
    contact_user=models.ManyToManyField(User)
    contact_email = models.CharField(max_length=300, default='contactemail', unique=True)
    contact_firstName = models.CharField(max_length=200, default="first")
    contact_lastName = models.CharField(max_length=300, default="last")
    contact_phoneNumber = PhoneNumberField(default=int())
    contact_address = models.TextField(default="address")
    contact_relation = models.CharField(max_length = 200, default="relation")
    contact_group = models.CharField(max_length=300, default="group")
    contact_age = models.CharField(max_length=5, default="age")
    contact_notes= models.TextField(default="notes")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.contact_email
    
    
    # def get_absolute_url(self):
    #     return(reverse('contact_info', kwargs={'pk': self.pk}))
    
    
    
    
    
    
    # On original python_cli database list

        # FROM CLI MODEL
# db = PostgresqlDatabase('frontend', user='postgres', password='',
#                         host='localhost', port=5432)
# db.connect()


# class BaseModel(Model):
#     class Meta:
#         database = db


# class frontend(BaseModel):
#     first_name= CharField(max_length=200,default='first')
#     last_name = CharField(max_length=200,default='last')
#     number =  NumberInput(default='phone')
#     email = EmailInput(max_length=200, default='email')
#     address = TextField(max_length=500, default='address')
#     relation = CharField(max_length=400, default='relation')
#     group = TextField(max_length=500, default='group')
#     age = NumberInput(default='age')
#     notes = TextField(max_length=1000, default='notes')
