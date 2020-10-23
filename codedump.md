    
    contactEmail = models.CharField(max_length=400, default='email', unique=True)
    firstName  = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phone = models.IntegerField(default='phone')
    # adding to cli list 
    contactAddress = models.CharField(max_length=100)
    relation = models.CharField(max_length=200, default='relation')
    group = models.CharField(max_length=500, default='group')
    age = models.IntegerField( default='age')
    notes = models.TextField( default='notes')
    
    def __str__(self):
            return self.contactEmail
        


{
  
    },
    