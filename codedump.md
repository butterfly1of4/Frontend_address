




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





