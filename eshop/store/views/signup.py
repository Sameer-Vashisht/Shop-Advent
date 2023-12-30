from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self , request):
        return render(request ,  "signup.html")
    
    def post(self , request):
        post_data = request.POST
        firstname = post_data.get("firstname")
        lastname = post_data.get("lastname")
        phone_no = post_data.get("phone_no")
        email = post_data.get("email")
        password = post_data.get("password")

        value = {
            "firstname" : firstname,
            "lastname"  : lastname,
            "phone_no"  : phone_no,
            "email"     : email
        }

        #validation
        error_message = None

        customer = Customer(firstname = firstname,
                            lastname = lastname,
                            phone_no = phone_no,
                            email = email,
                            password = password)
        
        error_message = self.validateCustomer(customer)

        if not error_message:  
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("homepage")
        else :
            data = {
                "error" : error_message,
                "values" : value
            }
            return render(request , "signup.html" , data)
    
    def validateCustomer(self , customer):
        error_message = None

        if not customer.firstname:
            error_message = "firstname required"
        elif len(customer.firstname) < 4:
            error_message = "firstname should be 4 characters long or more"
        elif not customer.lastname:
            error_message = "lastname required"
        elif len(customer.lastname) < 4:    
            error_message = "lastname should be 4 characters long or more"
        elif not customer.phone_no :
            error_message = "phone No. required"
        elif len (customer.phone_no) < 10:
            error_message = "phone No. must be 10 digits long"
        elif not customer.email:
            error_message = "email required"
        elif len(customer.email) < 10:    
            error_message = "email should be 10 characters long or more"  
        elif not customer.password:
            error_message = "password required"
        elif len(customer.password) < 10:    
            error_message = "password should be 10 characters long or more"
        elif customer.isExists():
            error_message = "email already exists"

        return error_message