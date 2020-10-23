from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, default='username')
    password = models.Charfield(max_length=300, default='password')
    
    def __str__(self):
        return self.first_name
    
    
    
# # NEW MODEL
class Contact(models.Model):
    # On original python_cli database list  
    first_name  = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='number', default='phone')
    email = models.TextField(default='email')
    
    # adding to cli list 
    address = models.TextField( default='address')
    relation = models.CharField(max_length=200, default='relation')
    group = models.CharField(max_length=500, default='group')
    age = models.IntegerField(default='age')
    notes = models.TextField( default='notes')
    
    def __str__(self):
            return self.first_name
        
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
