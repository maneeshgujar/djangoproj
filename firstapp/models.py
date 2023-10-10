from django.db import models

from db_connections import db

person= db['members']
# person = db.members

# Create your models here.
class Member(models.Model):
    firstname= models.CharField(max_length=200)
    lastname= models.CharField(max_length=200)
    phno= models.IntegerField(null=True)
    dob= models.DateField(null=True)

    def __str__(self) :
        return f"{self.firstname} {self.lastname}"