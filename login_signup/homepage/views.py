from django.http import HttpResponse,Http404
from .models import user
from django.template import loader
from django.shortcuts import render
#from django.contrib.auth import login

def login_view(request):
    if request.method == "GET":
        return render(request,'loginpage.html')

    elif request.method == "POST":
        username_temp = request.POST.get('usrname')
        password_temp = request.POST.get('usrpass')
        if(len(user.objects.filter(username=username_temp,password=password_temp))!=0):
            userss=user.objects.get(username=username_temp)
            return render(request,'index.html',{'users':userss})
        else:
            return HttpResponse("<h3>wrong username or password</h3>"
                                "<a href='/'><input type='button' value='login'></a>")



def signup(request):
    if request.method == "GET":
        return render(request,'signuppage.html')

    elif request.method == "POST":
        username_temp = user_obj=request.POST.get('usrname')
        password_temp = request.POST.get('pass')
        phone = request.POST.get('tel')
        email_temp = request.POST.get('email')
        all_user=user.objects.all()
        flag=0
        for a in all_user:
            if a.username==username_temp:
                flag=1
        if flag==1:
            return HttpResponse("<h3>Username all ready there.<br>Choose a different username</h3>"
                                "<a href='/signup/'><input type='button' value='SignUp'></a>")
        else:
            user_instance = user.objects.create(username=username_temp,password=password_temp,phone_number=phone,email=email_temp)
            return render(request,'index.html',{'users':user_instance})



