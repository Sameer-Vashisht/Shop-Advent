from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    
    def get(self , request):
        return render(request , "login.html")
    
    def post(self , request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.getCustomer_by_email(email)

        value = {
            "email" : email
        }

        error_message = None

        if customer:
            flag = check_password(password , customer.password)

            if flag:
                request.session["customer"] = customer.id
                return redirect("homepage")
            else:
                error_message = "Email or password invalid!!!"

        else:
            error_message = "Email or password invalid!!!"

        data = {
            "error"  : error_message,
            "values" : value,
        }
        return render(request , "login.html" , data)
    
def logout(request):
    request.session.clear()
    return redirect("login")