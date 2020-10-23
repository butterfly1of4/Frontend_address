from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    userName = models.CharField(max_length=200, default='useremail', unique=True)
    userEmail = models.CharField(max_length=400, default='email')
    password = models.CharField(max_length=300, default='password')

    def __str__(self):
        return self.userName


# # NEW MODEL
class Contact(models.Model):
    contactEmail = models.CharField(max_length=300, default='contactemail', unique=True)
    owner = models.CharField(User, max_length=200, default="owner")
    firstName = models.CharField(max_length=200, default="first")
    lastName = models.CharField(max_length=300, default="last")
    phone_number = PhoneNumberField(default=int())
    contactAddress = models.TextField(default="address")
    relation = models.CharField(max_length = 200, default="relation")
    group = models.CharField(max_length=300, default="group")
    age = models.CharField(max_length=5, default='age')
    notes= models.TextField(default="notes")

    def __str__(self):
        return self.contactEmail
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
