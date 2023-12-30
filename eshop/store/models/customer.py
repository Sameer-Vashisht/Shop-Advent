from django.db import models

class Customer (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=340)

    def register (self):
        return self.save()
    
    @staticmethod
    def getCustomer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
        
    
    def isExists (self):
        if Customer.objects.filter(email = self.email):
            return True
        
        return False