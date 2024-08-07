from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth         #iske kuch methods--> authenticate, login, logout

def login(request):
 
    if request.method == 'POST':
        input_username = request.POST.get("username")
        input_password = request.POST.get("password")

        user = auth.authenticate(username = input_username, password = input_password)
        # print(user)
        if user is not None:

            auth.login(request, user) #isse session create ho rha hai ---or--- is request ke pass user ki details save ho rhi hai
            return redirect("to_do")
        
        else:
            return redirect("landing_page") 

    return render(request, "accounts/login.html") 

def register(request):  

    if request.method == "POST":
        input_username = request.POST.get("username")
        input_first_name = request.POST.get("first_name")
        input_last_name = request.POST.get("last_name")
        input_email = request.POST.get("email")
        input_password = request.POST.get("password")

        new_user = User(
            username = input_username,
            first_name = input_first_name,
            last_name = input_last_name,
            email = input_email,
        )

        new_user.set_password(input_password)
        new_user.save()

        return redirect("login")
    
    return render(request, "accounts/register.html")   