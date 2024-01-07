import pyotp
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.staticfiles.finders import find
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from quality_education import settings
from . import models


users = User.objects.all()
c_language = models.c_language.objects.all()

def home(request):
    pass



#authentication
def user_login(request):
    err = {}
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']

        user = authenticate(username = uname, password = password )
        if user is not None:
            login(request, user)
            request.session['username'] = uname
            return redirect('profile')

        else:
            return redirect('login')
            err['loginerr'] = "invalid credintails!"
    return render(request, "authentication/login.html",err)


def register(request):
    values = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        email = request.POST['email']
        uname = request.POST['uname']
        if User.objects.filter(email=email).exists():
            #print("email")
            values['emailerr'] = "email already exists."
            values['fname'] = fname
            values['lname'] = lname
            values['email'] = email
            values['uname'] = uname

        elif User.objects.filter(username=uname).exists():
            #print("uname")
            values['fname'] = fname
            values['lname'] = lname
            values['email'] = email
            values['uname'] = uname
            values['exists'] = "UserName already exists."
        else:
            values['email'] = email
            # print("email")
            request.session['fname'] = fname
            request.session['lname'] = lname
            request.session['pass1'] = pass1
            request.session['email'] = email
            request.session['uname'] = uname
            # Generate OTP
            otp_secret = pyotp.random_base32()
            totp = pyotp.TOTP(otp_secret)
            otp = totp.now()
            print(otp)
            subject = 'Welcome to the website'
            message = f'Hello {fname} { lname }!!\n\nplease verify your account\nYour OTP for email verification is: {otp}\n\nThank You!!!'

            # Send OTP via email
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            sent = send_mail(subject, message, from_email, to_list, fail_silently=True)
            print(sent)
            request.session['otp'] = otp

            return redirect('otp_verification')
    return render(request, "authentication/register.html", values)


def otp_verification(request):
    values = {}
    fname = request.session.get('fname', '')
    lname = request.session.get('lname', '')
    pass1 = request.session.get('pass1', '')
    email = request.session.get('email', '')
    uname = request.session.get('uname', '')
    otp = request.session.get('otp', '')
    values['email'] = email
    if request.method == 'POST':
        user_otp = request.POST['otp']
        if user_otp == otp:
            userobj = User.objects.create_user(
                username=uname,
                password=pass1,
                email=email,
                first_name=fname,
                last_name=lname
            )
            userobj.save()
            models.c_language.objects.create(
                username = uname
            )
            user = authenticate(username = uname, password = pass1 )
            login(request, user)
            return redirect('profile')
        else:
            values['opterr'] = "Invalid OTP"

    return render(request, 'authentication/otp_verification.html', values)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user_data = {}
    uname = request.user.username
    user = User.objects.get(username = uname)
    user_data['user'] = user
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        oldpass = request.POST['oldpass']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if fname.isalnum() and lname.isalnum():
            if len(password)>6 and password.isalnum():
                if password == cpassword :
                    if user.check_password(oldpass):
                        # The old password matches, update user information
                        user.username = uname
                        user.first_name = fname
                        user.last_name = lname

                        # Check if a new password is provided and update it
                        if password:
                            user.set_password(password)
                            # Update the session authentication hash
                            update_session_auth_hash(request, user)

                        user.save()
                        user_data['success'] = "Updated Successfully"
                        user_data['warning'] = None
                    else:
                        user_data['warning'] = "Check your Old Password"
                else:
                    user_data['warning'] = "Password and Confirm Password doesn't match"
            else:
                 user_data['warning'] = "Password must be at least 6 characters long and should contain both alphabets and numbers"
        else:
            user_data['warning'] = "First Name and Last Name must contain only Alphabets"

    # print(user_data['first_name'])
    return render(request, "profile.html", user_data)