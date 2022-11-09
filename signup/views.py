from django.shortcuts import render,redirect,HttpResponse
from signup.forms import signUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import random
from signup.models import userotp
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def user(request):
    if request.method=='POST':
        get_otp=request.POST.get('e_otp')
        if get_otp is not None:        
            get_user=request.POST.get('usr')
            usr=User.objects.get(username=get_user)
            if int(get_otp)==userotp.objects.filter(user_otp=usr).last().otp:
                usr.is_active=True
                usr.save()
                return render(request,'login.html')
            else:
                msg='Your enter a wrong OTP .'

                return render(request,'signup.html ',{'otp':True},{'msg':msg})


        form= signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            usr=User.objects.get(username=username)
            usr.email=username
            usr.is_active=False
            usr.save()            
            otp1=random.randint(100000,999999)
            userotp.objects.create(user_otp=usr,otp=otp1)

            msg=f"Hello ,\n Your otp is {otp1}\nThanks ! "
            send_mail(
                    'welcom in Jobseeker -verify your E-mail',
                    msg,
                    settings.EMAIL_HOST_USER,
                    [usr.email],
                    fail_silently=False,
                )

            return render(request,'signup.html ',{'otp':True, 'usr':usr})

    else: 
        form = signUpForm()   
    
    return render(request,"signup.html",{'form':form})

       

        
def ulogin(request):
    if request.method=="POST":
        uname=request.POST.get("mail")
        passwd=request.POST.get("Pw")
        user = authenticate(request, username=uname , password=passwd)
        print(user)
       
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print('Please Enter valid Password !')
            msg1 ='Please Enter valid Password !'
            return render(request,"login.html",{'msg':msg1}) 
    else:
        
        return render(request,"login.html" )


def userlogout(request):
    logout(request)
    return redirect("/")
    

def reset_pw(request):    
    if request.method=="POST":
        mail=request.POST.get('mail')
        user=User.objects.filter(username=mail)
        user.exists()
        usr=User.objects.get(username=mail)
        otp2 = random.randint(100000, 999999)
        userotp.objects.create(user_otp = usr , otp = otp2)
        mess = f"Hello ,\nYour OTP is {otp2}\nThanks!"
        send_mail(
			"welcom in Jobseeker -Reset your passward",
			mess,
			settings.EMAIL_HOST_USER,
			[usr.email],
			fail_silently = False
			)
        
        usr=User.objects.get(username=mail)
        return render (request, 'create_pw.html',{'usr':usr})

    else:
        
        return render(request,'resend.html')    

def update_pa(request):
    if request.method=='POST':
        get_otp=request.POST.get('Pw')
        if get_otp is not None:        
            get_user=request.POST.get('mail')
            User.objects.get(username=get_user) and int(get_otp)==userotp.objects.filter(user_otp=get_otp).last()
        
            form=signUpForm()       
            return render(request,'new_pw.html',{'form':form})
    else:
        m='invalid otp '
        return render(request,'new_pw.html' ,{'m':m})


def conf_pw(request):
    if request.method=='POST':
        get_otp=request.POST.get('Pw')
        usr=User.objects.create(password=get_otp)
        usr.save()
        return render(request,'login.html') 

    else:

        return HttpResponse('Error')
    
    
