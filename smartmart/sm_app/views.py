from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import sm_app_mainuser
from .models import mainuser
from .models import ShopOwner

# Create your views here.
from django.contrib import messages



# from .models import UserAccount
# from django.http import HttpResponseRedirect

def openwindow(request):
    return render(request, 'first.html')

def signup(request):
    return render(request, 'signup.html')

# def maps(request):
#     supermarkets = SuperMarket.objects.all()
#     return render(request, 'maps.html',  {'supermarkets': supermarkets})
#     # return render(request, 'maps.html')

from django.shortcuts import render
# from .models import SuperMarket

# def maps(request):
#     supermarkets = SuperMarket.objects.all()
#     context = {
#         'supermarkets': list(supermarkets.values())  # Serialize queryset to JSON-serializable format
#     }
#     return render(request, 'maps.html', context)

# views.py
from django.shortcuts import render
from .models import SuperMarket

# def maps(request):
#     supermarkets = SuperMarket.objects.all()
#     context = {
#         'supermarkets': supermarkets
#     }
#     return render(request, 'maps.html', context)

# views.py
# from django.shortcuts import render
# from django.contrib.gis.geos import Point
# from django.contrib.gis.db.models.functions import Distance
# from .models import SuperMarket

# def maps(request):
#     # Default location (e.g., center of the city)
#     user_location = Point(-0.09, 51.505, srid=4326)  # Longitude, Latitude

#     # Get nearby supermarkets within a radius (in meters)
#     nearby_supermarkets = SuperMarket.objects.annotate(
#         distance=Distance('location', user_location)
#     ).order_by('distance').filter(distance__lte=1000)  # Adjust radius as needed

#     context = {
#         'supermarkets': nearby_supermarkets
#     }
#     return render(request, 'myapp/map.html', context)

# views.py

from django.shortcuts import render
from .models import SuperMarket
from django.conf import settings

# def map(request):
#     # Fetch all supermarkets
#     supermarkets = SuperMarket.objects.all()

#     # Prepare data for the template
#     shops = []
#     for supermarket in supermarkets:
#         shop_data = {
#             "name": supermarket.s_name,
#             "lat": supermarket.latitude,
#             "lng": supermarket.longitude,
#         }
#         shops.append(shop_data)

#     context = {
#         'shops': shops,
#         'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
#     }
#     return render(request, 'shop_map.html', context)

from django.shortcuts import render
from .models import SuperMarket
from django.conf import settings

# def maps(request):
#     # Fetch all supermarkets
#     supermarkets = SuperMarket.objects.all()

#     # Prepare data for the template
#     shops = []
#     for supermarket in supermarkets:
#         shop_data = {
#             "id": supermarket.s_id,
#             "name": supermarket.s_name,
#             "lat": supermarket.latitude,
#             "lng": supermarket.longitude,
#             "type": supermarket.s_type,
#             "address": supermarket.s_address,
#             "opentime": supermarket.s_opentime,
#             "closetime": supermarket.s_closetime,
#         }
#         shops.append(shop_data)

#     context = {
#         'shops': shops,
#         'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
#     }
#     return render(request, 'maps.html', context)

# from django.shortcuts import render
# from .models import SuperMarket
# from django.conf import settings

# def maps(request):
#     # Fetch all supermarkets
#     supermarkets = SuperMarket.objects.all()

#     # Prepare data for the template
#     shops = []
#     for supermarket in supermarkets:
#         shop_data = {
#             "id": supermarket.s_id,
#             "name": supermarket.s_name,
#             "lat": supermarket.latitude,
#             "lng": supermarket.longitude,
#             "type": supermarket.s_type,
#             "address": supermarket.s_address,
#             "opentime": supermarket.s_opentime,
#             "closetime": supermarket.s_closetime,
#         }
#         shops.append(shop_data)

#     context = {
#         'shops': shops,
#         'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
#     }
#     return render(request, 'maps.html', context)

# views.py

# from django.shortcuts import render
# from .models import SuperMarket
# from django.conf import settings

# def maps(request):
#     # Fetch all supermarkets
#     supermarkets = SuperMarket.objects.all()

#     # Prepare data for the template
#     shops = []
#     for supermarket in supermarkets:
#         shop_data = {
#             "id":supermarket.s_id,
#             "name": supermarket.s_name,
#             "mail":supermarket.s_mail,
#             "lat": supermarket.latitude,
#             "lng": supermarket.longitude,
            
#         }
#         shops.append(shop_data)

#     context = {
#         'shops': shops,
#         'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
#     }
#     return render(request, 'maps.html', context)
from django.shortcuts import render
from .models import SuperMarket
from django.conf import settings
import json
from datetime import time

def time_to_string(t):
    return t.strftime('%H:%M:%S') if isinstance(t, time) else t

def maps(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        # Redirect to login page if user is not logged in
        return redirect('login')
      
  
    # Fetch all supermarkets
    supermarkets = SuperMarket.objects.all()

    # Prepare data for the template
    shops = []
    for supermarket in supermarkets:
        shop_data = {
            "id": supermarket.s_id,
            "name": supermarket.s_name,
            "mail": supermarket.s_mail,
            "lat": supermarket.latitude,
            "lng": supermarket.longitude,
            "type": supermarket.s_type,
            "address": supermarket.s_address,
            "opentime": time_to_string(supermarket.s_opentime),
            "closetime": time_to_string(supermarket.s_closetime),
        }
        shops.append(shop_data)
        message='done'

    context = {
        'shops': json.dumps(shops),
        'message':message# Serialize shops data to JSON
    }
    
    return render(request, 'maps.html', context)

def password_options(request):
    return render(request, 'password_resetoption.html')

def login(request):
    return render(request, 'login.html')

def aboutus(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        # Redirect to login page if user is not logged in
        return redirect('login')
    return render(request, 'aboutus.html')

def aboutusshopowner(request):
    return render(request,'aboutusshopowner.html')

def about(request):
    return render(request, 'about.html')


def forgotpass(request):
    return render(request, 'forgotoss.html')

def forgotpassshopowner(request):
    return render(request, 'forgotpassshopowner.html')


def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        # Redirect to login page if user is not logged in
        return redirect('login')
    return render(request, 'home.html')

def shopowner_reg(request):
    return render(request, 'shopowner_reg.html')



import base64

def encode_password(password):
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    return encoded_password




def decode_password(encoded_password):
    try:
        decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    except UnicodeDecodeError:
        # Handle the case where decoding fails due to invalid characters
        decoded_password = "Unable to decode password"
    return decoded_password
# def success_page(request):
#     return render(request,'home.html')
# def inseruser(request):
#     fname=request.POST['fname'];
#     lname=request.POST['lname'];
#     email=request.POST['email'];
#     cpass =request.POST['pass'];
#     dob=request.POST['dob'];
#     pnum=request.POST['num'];
#     us=sm_app_mainuser(user_fname=fname, user_lname=lname,user_mail=email,user_password=cpass,user_dob=dob,user_phonenumber=pnum);
#     us.save();
#     return render(request, 'home.html',{})



# def user_form_view(request):
#     if request.method == 'POST':
#         user = mainuser(
#             user_fname=request.POST['fname'],
#             user_lname=request.POST['lname'],
#             user_mail=request.POST['email'],
#             user_password=request.POST['pass'],
#             user_dob=request.POST['dob'],
#             user_phonenumber=request.POST['num']
#         )
#         user.save()
        
#     return render(request, 'home.html')



# def user_form_view(request):
#     # Check if the form is submitted
#     if request.method == 'POST':
#         # Extract data from the submitted form
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']

#         # if check_mail(user_mail) == True:
#         #     return
#         # Create a new instance of the mainuser model with the extracted data
#         new_user = mainuser(
#             user_fname=user_fname,
#             user_lname=user_lname,
#             user_mail=user_mail,
#             user_password=user_password,
#             user_dob=user_dob,
#             user_phonenumber=user_phonenumber
#         )

#         # Save the new user to the database
#         new_user.save()
        
#     # Render the home.html template, regardless of whether the form is submitted or not
#     return render(request, 'home.html')

# from django.db import IntegrityError
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.urls import reverse
# from django.http import HttpResponse

# def user_form_view(request):

#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password=encode_password(user_password)
#         print(user_password)
#         print(en_password)
#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."

#             # User with this email already exists, print a message or handle it as needed
#             # print("A user with this email already exists.")
#             # You can redirect to another page or render a template with an error message
#             return render(request, 'signup.html', {'error_message': error_message})

        
#         # Create a new ShopOwner instance
#         new_user = mainuser(
#                 user_fname=user_fname,
#                 user_lname=user_lname,
#                 user_mail=user_mail,
#                 user_password=en_password,
#                 user_dob=user_dob,
#                 user_phonenumber=user_phonenumber
#             )
#         # Save the new ShopOwner instance to the database
#         new_user.save()
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#                 'user': new_user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
#                 'token': default_token_generator.make_token(new_user),
#             })
#         send_mail(mail_subject, message, 'your_email@example.com', [user_mail])
#         return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         return render(request, 'signup.html')
#         # Redirect to welcome page with owner email as parameter
#     return render(request, 'login.html')


#     return render(request, 'signup.html')


# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.http import HttpResponse
# from .models import mainuser  # Ensure you import your user model
# # from .utils import encode_password  # Assuming you have a utility function for encoding passwords

# def user_form_view(request):
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password = encode_password(user_password)

#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."
#             return render(request, 'signup.html', {'error_message': error_message})

#         # Create a new mainuser instance
#         new_user = mainuser(
#             user_fname=user_fname,
#             user_lname=user_lname,
#             user_mail=user_mail,
#             user_password=en_password,
#             user_dob=user_dob,
#             user_phonenumber=user_phonenumber
#         )
#         new_user.save()

#         # Send confirmation email
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': new_user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
#             'token': default_token_generator.make_token(new_user),
#         })
#         send_mail(mail_subject, message, 'your_email@example.com', [user_mail])

#         return HttpResponse('Please confirm your email address to complete the registration')

#     else:
#         return render(request, 'signup.html')



# from django.contrib.auth import login

# # def activate(request, uidb64, token):
# #     try:
# #         uid = force_text(urlsafe_base64_decode(uidb64))
# #         user = mainuser.objects.get(pk=uid)
# #     except(TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
# #         user = None
    
# #     if user is not None and default_token_generator.check_token(user, token):
# #         user.is_active = True
# #         user.save()
# #         login(request, user)
# #         return HttpResponse('Thank you for your email confirmation. Now you can log in to your account.')
# #     else:
# #         return HttpResponse('Activation link is invalid!')

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = mainuser.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Thank you for your email confirmation. Now you can log in to your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')

# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.http import HttpResponse
# from django.contrib.auth import login
# from .models import mainuser  # Ensure you import your user model
# # from .utils import encode_password  # Assuming you have a utility function for encoding passwords

# def user_form_view(request):
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password = encode_password(user_password)

#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."
#             return render(request, 'signup.html', {'error_message': error_message})

#         # Create a new mainuser instance
#         new_user = mainuser(
#             user_fname=user_fname,
#             user_lname=user_lname,
#             user_mail=user_mail,
#             user_password=en_password,
#             user_dob=user_dob,
#             user_phonenumber=user_phonenumber
#         )
#         new_user.save()

#         # Send confirmation email
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': new_user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
#             'token': default_token_generator.make_token(new_user),
#         })
#         send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])

#         return HttpResponse('Please confirm your email address to complete the registration')

#     else:
#         return render(request, 'signup.html')

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = mainuser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Thank you for your email confirmation. Now you can log in to your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')




# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.http import HttpResponse
# from .models import mainuser  # Ensure you import your user model
# # from .utils import encode_password  # Assuming you have a utility function for encoding passwords

# def user_form_view(request):
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password = encode_password(user_password)

#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."
#             return render(request, 'signup.html', {'error_message': error_message})

#         # Create a new mainuser instance
#         new_user = mainuser(
#             user_fname=user_fname,
#             user_lname=user_lname,
#             user_mail=user_mail,
#             user_password=en_password,
#             user_dob=user_dob,
#             user_phonenumber=user_phonenumber
#         )
#         new_user.save()

#         # Send confirmation email
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': new_user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
#             'token': default_token_generator.make_token(new_user),
#         })
#         send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])

#         return HttpResponse('Please confirm your email address to complete the registration')

#     else:
#         return render(request, 'signup.html')

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = mainuser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Your account is now active. You can log in.')
#     else:
#         return HttpResponse('Activation link is invalid!')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import mainuser 
def user_form_view(request):
    if request.method == 'POST':
        user_fname = request.POST['fname']
        print(user_fname)
        user_lname = request.POST['lname']
        user_mail = request.POST['email']
        user_password = request.POST['pass']
        user_dob = request.POST['dob']
        user_phonenumber = request.POST['num']
        # en_password = encode_password(user_password)
        en_password=encode_password(user_password)
        # Check if a user with the same email already exists
        if mainuser.objects.filter(user_mail=user_mail).exists():
            error_message = "A user with this email already exists. Please use a different email."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create a new User instance
        user = User.objects.create_user(username=user_lname+user_fname, email=user_mail, password=user_password)
        user.first_name = user_fname
        user.last_name = user_lname
        user.is_active = False  # User is inactive until email confirmation
        user.save()

        # Create a new MainUser instance
        new_user = mainuser(
          
            user_fname=user_fname,
            user_lname=user_lname,
            user_mail=user_mail,
            user_password=en_password,
            user_dob=user_dob,
            user_phonenumber=user_phonenumber
        )
        new_user.save()

        # Send confirmation email
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        # send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])
        email_from = settings.EMAIL_HOST_USER
            # subject = 'Feedback from User'
        html_message = f"""
            {message}
            """
        sendemail = EmailMessage(mail_subject, html_message, email_from, [user_mail])
        sendemail.content_subtype = 'html'  # Set the content type to HTML
        sendemail.send()
        return render(request,'requestdone.html',{'user':new_user})
        # return HttpResponse('Please confirm your email address to complete the registration')
        # return render(request, 'acc_active_email.html', {'newuser': new_user})

    else:
        return render(request, 'signup.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'gotologin.html')
        # return HttpResponse('Thank you for your email confirmation. Your account is now active. You can log in.')
    else:
        return HttpResponse('Activation link is invalid!')


# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.http import HttpResponse
# from .models import mainuser  # Ensure you import your user model
# # from .utils import encode_password  # Assuming you have a utility function for encoding passwords

# def user_form_view(request):
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password = encode_password(user_password)
        
#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."
#             return render(request, 'signup.html', {'error_message': error_message})

#         # Create a new MainUser instance
#         new_user = mainuser(
#             user_fname=user_fname,
#             user_lname=user_lname,
#             user_mail=user_mail,
#             user_password=en_password,
#             user_dob=user_dob,
#             user_phonenumber=user_phonenumber,
#             is_active=False  # User is inactive until email confirmation
#         )
#         new_user.save()

#         # Send confirmation email
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': new_user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
#             'token': default_token_generator.make_token(new_user),
#         })
#         send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])

#         return HttpResponse('Please confirm your email address to complete the registration')

#     else:
#         return render(request, 'signup.html')

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         new_user = mainuser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         new_user = None

#     if new_user is not None and default_token_generator.check_token(new_user, token):
#         new_user.is_active = True
#         new_user.save()
#         return render(request, 'login.html')
#     else:
#         return HttpResponse('Activation link is invalid!')
# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = mainuser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return render(request, 'login.html')
#         # return HttpResponse('Thank you for your email confirmation. Your account is now active. You can log in.')
#     else:
#         return HttpResponse('Activation link is invalid!')

# # def user_form_view(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         en_password=encode_password(user_password)

#         try:
#             # Create a new instance of the mainuser model with the extracted data
#             new_user = mainuser(
#                 user_fname=user_fname,
#                 user_lname=user_lname,
#                 user_mail=user_mail,
#                 user_password=en_password,
#                 user_dob=user_dob,
#                 user_phonenumber=user_phonenumber
#             )

#             # Save the new user to the database
#             new_user.save()
            
#             # Redirect to home page after successful registration
#             return render(request, 'login.html')

#         except IntegrityError:
#             # If a user with the same email already exists, set error_message
#             error_message = "A user with this email already exists. Please use a different email."

#     # Render the signup page with the error message (if any)
#     return render(request, 'signup.html', {'error_message': error_message})


# def user_form_view(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_fname = request.POST['fname']
#         user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']

#     #     try:
    #         # Create a new instance of the mainuser model with the extracted data
    #         new_user = mainuser(
    #             user_fname=user_fname,
    #             user_lname=user_lname,
    #             user_mail=user_mail,
    #             user_password=user_password,
    #             user_dob=user_dob,
    #             user_phonenumber=user_phonenumber
    #         )

    #         # Save the new user to the database
    #         new_user.save()
            
    #         # Redirect to home page after successful registration
    #         return render(request, 'home.html')

    #     except IntegrityError:
    #         # If a user with the same email already exists, display an error message
    #         error_message = "A user with this email already exists. Please use a different email."
    #         return render(request, 'signup.html', {'error_message': error_message})

    # # Render the signup page
    # return render(request, 'signup.html')
    #     try:
    #         # Create a new instance of the mainuser model with the extracted data
    #         new_user = mainuser(
    #             user_fname=user_fname,
    #             user_lname=user_lname,
    #             user_mail=user_mail,
    #             user_password=user_password,
    #             user_dob=user_dob,
    #             user_phonenumber=user_phonenumber
    #         )

    #         # Save the new user to the database
    #         new_user.save()
            
    #         # Redirect to home page after successful registration
    #         return render(request, 'home.html')

    #     except IntegrityError:
    #         # If a user with the same email already exists, set error_message
    #         error_message = "A user with this email already exists. Please use a different email."

    # # Render the signup page with the error message (if any)
    # return render(request, 'signup.html', {'error_message': error_message})

# def login_operation(request):
#     if request.method == 'POST':
#         umail=request.POST['mail']
#         upass=request.POST['password']
        
        

# from django.shortcuts import render, redirect
# 
# from .models import mainuser

# def login_operation(request):
#     if request.method == 'POST':
#         user_email = request.POST.get('mail')
#         user_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = mainuser.objects.get(user_mail=user_email,user_password=user_pass)
            
#             # Check if the password matches
#             if user.check_password(user_email,user_pass) == True:
#                 # If authentication succeeds, redirect to home page
#                 # return redirect('home')  # Replace 'home' with the name of your home page URL pattern
#                 return render(request, 'home.html')
#             else:
#                 # If authentication fails, display an error message
#                 # messages.error(request, 'Invalid email or password.')
#                 # return redirect('login')  # Redirect back to the login page
#                 return render(request, 'error.html')
        
#         except mainuser.DoesNotExist:
#             # If user doesn't exist, display an error message
#             messages.error(request, 'User with this email does not exist.')
#             # return redirect('login')  # Redirect back to the login page
#             return render(request, 'first.html')
        
        
# def login_operation(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_email = request.POST.get('mail')
#         user_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = mainuser.objects.get(user_mail=user_email)
            
#             # Check if the email and password match
#             if check_password(user_pass, user.user_password):
                
#                 if user.check_password(user_email, user_pass):
#                 # If authentication succeeds, render the home page
#                  return render(request, 'home.html')
#             else:
#                 # If password does not match, render the error page
#             #    error_message = 'invaild password'
#                 # messages.error(request, 'User with this email does not exist.')
#                 error_message1= "Invaild  password.."
#                 return render(request,  'login.html',{'error_message1': error_message1})
          
                
#         except mainuser.DoesNotExist:
#             error_message2 = "Invaild email and password.."
#             return render(request,  'login.html',{'error_message2': error_message2})
#             # If user doesn't exist, render the first page
#             # return render(request, 'first.html')

# def login_operation(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_email = request.POST.get('mail')
#         user_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = mainuser.objects.get(user_mail=user_email)
            
#             # Check if the email and password match
#             if check_password(user_pass, user.user_password):
#                 #  if user.check_password(user_email, user_pass):
#                 # Authentication succeeds, redirect to the home page
#                 # return redirect('home')  # Replace 'home' with your home page URL name
#                     return render(request, 'home.html')
#             else:
#                 # Password does not match, render the login page with error message
#                 error_message = "Invalid password."
#                 return render(request, 'login.html', {'error_message': error_message})
          
#         except mainuser.DoesNotExist:
#             # User with provided email does not exist, render the login page with error message
#             error_message = "User with this email does not exist."
#             return render(request, 'login.html', {'error_message': error_message})

#     else:
#         # GET request, render the login page
#         return render(request, 'login.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import check_password
# from .models import mainuser

# def login_operation(request):
#     error_message1 = None
#     error_message2=None
    
#     if request.method == 'POST':
#         user_email = request.POST.get('mail')
#         user_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = mainuser.objects.get(user_mail=user_email)
            
#             # Check if the email and password match
#             if check_password(user_pass, user.user_password):
#                 # Authentication succeeds, redirect to the home page
#                 return redirect('home')
#             else:
#                 # Password does not match, render the login page with error message
#                 error_message1 = "Invalid password."
#                 return render(request, 'login.html', {'error_message1': error_message1})
          
#         except mainuser.DoesNotExist:
#             # User with provided email does not exist, render the login page with error message
#             error_message2 = "User with this email does not exist."
#             return render(request, 'login.html', {'error_message2': error_message2})

#     else:
#         # GET request, render the login page
#         return render(request, 'login.html')




from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import mainuser

def profile(request):
    # Retrieve the logged-in user based on session data
    user_id = request.session.get('user_id')
    if user_id:
        user = mainuser.objects.get(user_id=user_id)
        return render(request, 'userprofile.html', {'user': user})
    else:
        # Redirect to login page if user is not logged in
        return redirect('login')

def login_operation(request):
    error_message1 = None
    error_message2 = None
    
    if request.method == 'POST':
        user_email = request.POST.get('mail')
        user_pass = request.POST.get('password')

        try:
            # Retrieve user based on email
            user = mainuser.objects.get(user_mail=user_email)
            
            stored_password= base64.b64decode(user.user_password).decode('utf-8')
            # stored_password=decode_password(user.user_password)
            print(stored_password)
            if user_pass == stored_password:
                request.session['user_id'] = user.user_id
                # return redirect('home')
                success_message = "Successfully logged in."
                return render(request, 'home.html',{'success_message': success_message, 'username':user.user_fname+user.user_lname})
            else:
                 error_message1 = "Invalid password."
                 return render(request, 'login.html', {'error_message1': error_message1})
                
            # Check if the email and password match
            # if check_password(user_pass, user.user_password):
            #     # Authentication succeeds, store user ID in session and redirect to profile page
            #     request.session['user_id'] = user.user_id
            #     return redirect('home')
            # else:
                # Password does not match, render the login page with error message
                # error_message1 = "Invalid password."
                # return render(request, 'login.html', {'error_message1': error_message1})
          
        except mainuser.DoesNotExist:
            # User with provided email does not exist, render the login page with error message
            error_message2 = "User with this email does not exist."
            return render(request, 'login.html', {'error_message2': error_message2})

    else:
        # GET request, render the login page
        return render(request, 'login.html')





def user_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')

# def shop_owner_form(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_name = request.POST['uname']
        
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         user_address = request.POST['address']

#         try:
#             # Create a new instance of the mainuser model with the extracted data
#             new_user = ShopOwner(
#                 o_name=user_name,
                
#                 o_mail=user_mail,
#                 o_password=user_password,
#                 o_dob=user_dob,
#                 o_phonenumber=user_phonenumber,
#                 o_address=user_address
#             )

#             # Save the new user to the database
#             new_user.save()
            
#             # Redirect to home page after successful registration
#             return render(request, 'home.html')

#         except IntegrityError:
#             # If a user with the same email already exists, set error_message
#             error_message = "A user with this email already exists. Please use a different email."

#     # Render the signup page with the error message (if any)
#     return render(request, 'signup.html', {'error_message': error_message})



# def shop_owner_form(request):
#     error_message = None
    
#     if request.method == 'POST':
#         user_name = request.POST['uname']
#         user_mail = request.POST['email']
#         user_password = request.POST['pass']
#         user_dob = request.POST['dob']
#         user_phonenumber = request.POST['num']
#         user_address = request.POST['address']

#         try:
#             # Hash the password using bcrypt
#             # hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
#             hashed_password=encode_password(user_password)

#             # Create a new instance of the ShopOwner model with the hashed password
#             new_user = ShopOwner(
#                 o_name=user_name,
#                 o_mail=user_mail,
#                 o_password=hashed_password, # Decode the hashed password to store it as a string
#                 o_dob=user_dob,
#                 o_phonenumber=user_phonenumber,
#                 o_address=user_address
#             )
#             # depassword=hashed_password.decode('utf-8'),
#             # print(depassword)
#             # Save the new user to the database
#             new_user.save()
            
#             # Redirect to the home page after successful registration
#             # return render(request, 'home.html')
#             # show_owner(request,user_mail)
#             # return redirect('show_owner', email=user_mail)
#             return redirect('show_owner', email=user_mail)
            

#         except IntegrityError:
#             # If a user with the same email already exists, set error_message
#             error_message = "A user with this email already exists. Please use a different email."

#     # Render the signup page with the error message (if any)
#     return render(request, 'shopowner_reg.html', {'error_message': error_message})


# def display_user_info(request):
#     # Retrieve user information from the database (replace this with your actual retrieval code)
#     user = ShopOwner.objects.get(id=request.user.o_id)

#     # Pass the user information to the HTML template
#     return render(request, 'user_info.html', {'user': user})


# def decode_password(encoded_password):
#     decoded_password = base64.b64decode(encoded_password).decode('utf-8')
#     return decoded_password

# def shop_owner_details(request):
#     # Retrieve all shop owners from the database
#     #o_password=hashed_password.decode('utf-8'), 
#     # shop_owners = ShopOwner.objects.all()
#     # enpass = ShopOwner.objects.all().values('o_password')
#     # print(enpass)
#     # depass=decode_password(enpass)
#     # print(enpass)
#     shop_owners = ShopOwner.objects.all().values('o_name', 'o_mail','o_password' ,'o_password', 'o_phonenumber', 'o_address')
#     for owner in shop_owners:
#          depass = decode_password(owner['o_password'])
#          print(depass)
#     # Pass the shop owner data to the HTML template
#     return render(request, 'user_info.html', {'shop_owners': shop_owners})


def shop_owner_details(request):
    # Retrieve all shop owners from the database
    shop_owners = ShopOwner.objects.all().values('o_name', 'o_mail', 'o_phonenumber', 'o_address', 'o_password')

    # Decode the password for each shop owner
    for owner in shop_owners:
        owner['o_password'] = decode_password(owner['o_password'])

    # Pass the shop owner data to the HTML template
    return render(request, 'user_info.html', {'shop_owners': shop_owners})


# def show_owner(request):
#     owner_name=ShopOwner.objects.values('o_name')
#     return render(request,'welcome_page_to_owner.html', {'owner_name': owner_name})

# def show_owner(request):
#     # Retrieve only one row from the ShopOwner table
#     owner = ShopOwner.objects.first()  # Or you can use .get() if you have a specific condition
#     return render(request, 'welcome_page_to_owner.html', {'owner': owner})

# def show_owner(request):
#     # Retrieve rows from the ShopOwner table based on a condition
#     owner= ShopOwner.objects.filter(o_id=5)  # Replace 'condition_here' with your condition
#     return render(request, 'welcome_page_to_owner.html', {'owners': owner})

# def show_owner(request, email):
#     # Retrieve the shop owner with o_id=5 from the ShopOwner table
#     owner = ShopOwner.objects.filter(o_mail=email).first() #or .last()...  # Using first() to get only one object
#     return render(request, 'welcome_page_to_owner.html', {'owner': owner})



def show_owner(request, email):
    # Retrieve the shop owner with the given email from the ShopOwner table
    owner = ShopOwner.objects.filter(o_mail= email).first() 

    # Check if owner exists
    if owner:
        # Render the HTML page with the owner's information
        return render(request, 'welcome_page_to_owner.html', {'owner': owner})
    else:
        # If no owner found, you can render an error page or handle it as per your requirement
        return render(request, 'error.html', {'error_message': 'Owner not found'})
# def show_owner(request):
#     email = request.GET.get('email')
#     if email:
#         owner = ShopOwner.objects.filter(o_mail=email).first()
#         if owner:
#             return render(request, 'welcome_page_to_owner.html', {'owner': owner})
#         else:
#             return render(request, 'error.html', {'error_message': 'Owner not found'})
#     else:
#         return render(request, 'error.html', {'error_message': 'Email parameter is missing'})

def shopreg(request):
    return render(request,'shopreg.html')


# def shop_form(request):
#     error_message = None
    
#     if request.method == 'POST':
#         shop_name = request.POST['uname']
#         shop_mail = request.POST['email']
#         shop_type = request.POST['type']
#         shop_opentime = request.POST['opentime']
#         shop_closetime= request.POSt['closetime']
#         shop_phonenumber = request.POST['num']
#         shop_address = request.POST['address']

#         try:
#             # Hash the password using bcrypt
#             # hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
#             # hashed_password=encode_password(user_password)

#             # Create a new instance of the ShopOwner model with the hashed password
#             new_user = ShopOwner(
#                 s_name=shop_name,
#                 s_mail=shop_mail,
#                 s_phonenumber=shop_phonenumber,
#                 s_type=shop_type,
#                 s_address=shop_address,
#                 s_opentime=shop_opentime,
#                 s_closetime=shop_closetime,
#                 owner_id = ShopOwner.objects.get(o_id=)
                
#             )
#             # depassword=hashed_password.decode('utf-8'),
#             # print(depassword)
#             # Save the new user to the database
#             new_user.save()
            
#             # Redirect to the home page after successful registration
#             # return render(request, 'home.html')
#             # show_owner(request,user_mail)
#             # return redirect('show_owner', email=user_mail)
#             return redirect('show_owner', email=user_mail)
            

#         except IntegrityError:
#             # If a user with the same email already exists, set error_message
#             error_message = "A user with this email already exists. Please use a different email."

#     # Render the signup page with the error message (if any)
#     return render(request, 'shopowner_reg.html', {'error_message': error_message})

from django.shortcuts import render, redirect
from .models import ShopOwner, SuperMarket

# def register_shop(request):
#     if request.method == 'POST':
#         # Get the form data for ShopOwner
#         owner_name = request.POST.get('o_name')
#         owner_mail = request.POST.get('o_mail')
#         owner_password = request.POST.get('o_password')
#         owner_dob = request.POST.get('o_dob')
#         owner_phonenumber = request.POST.get('o_phonenumber')
#         owner_address = request.POST.get('o_address')

#         # Create a new ShopOwner instance and save it
#         owner = ShopOwner.objects.create(
#             o_name=owner_name,
#             o_mail=owner_mail,
#             o_password=owner_password,
#             o_dob=owner_dob,
#             o_phonenumber=owner_phonenumber,
#             o_address=owner_address
#         )

#         # Get the form data for SuperMarket
#         shop_name = request.POST['uname']
#         shop_mail = request.POST['email']
#         shop_type = request.POST['type']
#         shop_opentime = request.POST['opentime']
#         shop_closetime= request.POSt['closetime']
#         shop_phonenumber = request.POST['num']
#         shop_address = request.POST['address']
#         # Create a new SuperMarket instance, set the owner, and save it
#         market = SuperMarket.objects.create(
#             s_name=shop_name,
#             s_mail=shop_mail,
#             s_phonenumber=shop_phonenumber,
#             s_type=shop_type,
#             s_address=shop_address,
#             s_opentime=shop_opentime,
#             s_closetime=shop_closetime,
#             owner=owner  # Set the owner for the SuperMarket
#         )

#         return redirect('success_page')  # Redirect to a success page

#     return render(request, 'register_shop.html')


# from django.shortcuts import render, redirect
# from .models import ShopOwner, SuperMarket

# def register_shop(request):
#     if request.method == 'POST':
#         # Get the form data for ShopOwner
#         owner_email = request.POST.get('o_mail')

#         # Check if the owner with the given email already exists
#         owner = ShopOwner.objects.filter(o_mail=owner_email).first()

#         if owner:
#             # Owner exists, proceed to register the shop
#             # Get the form data for SuperMarket
#             shop_name = request.POST['uname']
#             shop_mail = request.POST['email']
#             shop_type = request.POST['type']
#             shop_opentime = request.POST['opentime']
#             shop_closetime = request.POST['closetime']
#             shop_phonenumber = request.POST['num']
#             shop_address = request.POST['address']

#             # Create a new SuperMarket instance, set the owner, and save it
#             market = SuperMarket.objects.create(
#                 s_name=shop_name,
#                 s_mail=shop_mail,
#                 s_phonenumber=shop_phonenumber,
#                 s_type=shop_type,
#                 s_address=shop_address,
#                 s_opentime=shop_opentime,
#                 s_closetime=shop_closetime,
#                 owner=owner  # Set the owner for the SuperMarket
#             )

#             return redirect('success_page')  # Redirect to a success page
#         else:
#             # Owner does not exist, redirect to a page indicating that the owner needs to register first
#             return redirect('shopowner_reg')

# #     return render(request, 'register_shop.html')


# from django.shortcuts import render, redirect
# from .models import ShopOwner, SuperMarket

# def shopowner_reg(request):
#     if request.method == 'POST':
#         # Get the form data for ShopOwner
#         owner_name = request.POST['o_name']
#         owner_mail = request.POST['o_mail']
#         owner_password = request.POST['o_password']
#         owner_dob = request.POST['o_dob']
#         owner_phonenumber = request.POST['o_phonenumber']
#         owner_address = request.POST['o_address']

#         # Create a new ShopOwner instance and save it
#         owner = ShopOwner.objects.create(
#             o_name=owner_name,
#             o_mail=owner_mail,
#             o_password=owner_password,
#             o_dob=owner_dob,
#             o_phonenumber=owner_phonenumber,
#             o_address=owner_address
#         )

#         return redirect('welcome_page_to_owner', email=owner_mail)  # Redirect to welcome page

#     return render(request, 'shopowner_reg.html')

# def welcome_page_to_owner(request, email):
#     owner = ShopOwner.objects.filter(o_mail=email).first()
#     return render(request, 'welcome_page_to_owner.html', {'owner': owner})

# def register_shop(request):
#     if request.method == 'POST':
#         # Get the form data for SuperMarket
#         shop_name = request.POST['uname']
#         shop_mail = request.POST['email']
#         shop_type = request.POST['type']
#         shop_opentime = request.POST['opentime']
#         shop_closetime = request.POST['closetime']
#         shop_phonenumber = request.POST['num']
#         shop_address = request.POST['address']
#         owner_email = request.POST['owner_email']  # Add this line to get owner email from form

#         # Check if the owner with the given email already exists
#         owner = ShopOwner.objects.filter(o_mail=owner_email).first()

#         if owner:
#             # Owner exists, proceed to register the shop
#             # Create a new SuperMarket instance, set the owner, and save it
#             market = SuperMarket.objects.create(
#                 s_name=shop_name,
#                 s_mail=shop_mail,
#                 s_phonenumber=shop_phonenumber,
#                 s_type=shop_type,
#                 s_address=shop_address,
#                 s_opentime=shop_opentime,
#                 s_closetime=shop_closetime,
#                 owner=owner  # Set the owner for the SuperMarket
#             )

#             return redirect('success_page')  # Redirect to success page
#         else:
#             # Owner does not exist, redirect to a page indicating that the owner needs to register first
#             return redirect('shopowner_reg')

#     return render(request, 'shopreg.html')

# def success_page(request):
#     return render(request, 'success.html')

# from django.shortcuts import render, redirect
# from .models import ShopOwner, SuperMarket

# def shopowner_reg(request):
#     if request.method == 'POST':
#         # Get the form data for ShopOwner
#         owner_name = request.POST['o_name']
#         owner_mail = request.POST['o_mail']
#         owner_password = request.POST['o_password']
#         owner_dob = request.POST['o_dob']
#         owner_phonenumber = request.POST['o_phonenumber']
#         owner_address = request.POST['o_address']

#         # Create a new ShopOwner instance and save it
#         owner = ShopOwner.objects.create(
#             o_name=owner_name,
#             o_mail=owner_mail,
#             o_password=owner_password,
#             o_dob=owner_dob,
#             o_phonenumber=owner_phonenumber,
#             o_address=owner_address
#         )

#         # Redirect to welcome page with owner email as parameter
#         return redirect('welcome_page_to_owner', email=owner_mail)

#     return render(request, 'shopowner_reg.html')

from django.shortcuts import render, redirect
from .models import ShopOwner

def shopowner_reg_form(request):
    
    error_message=None
    if request.method == 'POST':
        # Get the form data for ShopOwner
        owner_name = request.POST[ 'uname']
        owner_mail = request.POST[ 'email']
        owner_password = request.POST[ 'pass']
        owner_dob = request.POST[ 'dob']
        owner_phonenumber = request.POST[ 'num']
        owner_address = request.POST['address']
        en_password=encode_password(owner_password)
        

        # Check if a user with the same email already exists
        if ShopOwner.objects.filter(o_mail=owner_mail).exists():
            error_message = "A user with this email already exists. Please use a different email."

            # User with this email already exists, print a message or handle it as needed
            # print("A user with this email already exists.")
            # You can redirect to another page or render a template with an error message
            return render(request, 'shopowner_reg.html', {'error_message': error_message})

        # Create a new ShopOwner instance
        owner = ShopOwner(
            o_name=owner_name,
            o_mail=owner_mail,
            # o_password=owner_password,
            o_password=en_password,
            o_dob=owner_dob,
            o_phonenumber=owner_phonenumber,
            o_address=owner_address
        )

        # Save the new ShopOwner instance to the database
        owner.save()

        # Redirect to welcome page with owner email as parameter
        # return redirect('welcome_page_to_owner', email=owner_mail)
        return redirect('shopowner_login')

    return render(request, 'shopowner_reg.html')




def shopowner_login_operation(request):
    error_message = None
    
    if request.method == 'POST':
        owner_email = request.POST.get('mail')
        owner_pass = request.POST.get('password')

        try:
            # Retrieve user based on email
            user = ShopOwner.objects.get(o_mail=owner_email)
            
            # Decode the stored password
            stored_password = base64.b64decode(user.o_password).decode('utf-8')
            # print(stored_password)
            # Check if the password matches
            # if check_password(owner_pass, stored_password):
            if owner_pass==stored_password:
                request.session['owner_id'] = user.o_id
                # Authentication succeeds, redirect to the home page
                request.session['shopownermail'] = owner_email
                return redirect('shopownerprofile_op')
            else:
                # Password does not match, render the login page with error message
                error_message = "Invalid email or password. Please try again."
          
        except ShopOwner.DoesNotExist:
            # User with provided email does not exist, render the login page with error message
            error_message = "User with this email does not exist."
    
    # Render the login page with error message if exists
    return render(request, 'shopowner_login.html', {'error_message': error_message})


# from .models import ShopOwner, SuperMarket
# from django.shortcuts import render, redirect

# def register_shop(request):
    
#     message_error=None
    
#     if request.method == 'POST':
#         # Get the form data for SuperMarket
#         shop_name = request.POST['uname']
#         shop_mail = request.POST['email']
#         shop_type = request.POST['type']
#         shop_opentime = request.POST['opentime']
#         shop_closetime = request.POST['closetime']
#         shop_phonenumber = request.POST['num']
#         shop_address = request.POST['address']
#         lat=request.POST['lat']
#         lng=request.POST['lan']
#         owner_email = request.POST['oemail']  # Add this line to get owner email from form
#         print("data taken")
#         # Check if the owner with the given email already exists
#         owner = ShopOwner.objects.filter(o_mail=owner_email).first()

#         if owner:
#             # Owner exists, proceed to register the shop
#             # Create a new SuperMarket instance and set its attributes
#             market = SuperMarket(
#                 s_name=shop_name,
#                 s_mail=shop_mail,
#                 s_phonenumber=shop_phonenumber,
#                 s_type=shop_type,
#                 s_address=shop_address,
#                 s_opentime=shop_opentime,
#                 s_closetime=shop_closetime,
#                 latitude=lat,
#                 longitude=lng,
                
#                 owner=owner  # Set the owner for the SuperMarket
               
#             )

#             # Save the SuperMarket instance to the database
#             market.save()
#             request.session['shop_id'] = market.s_id
#             # return redirect('success_page')  # Redirect to success page
#             return redirect('shopownerprofile_op')
#         else:
#             # Owner does not exist, redirect to a page indicating that the owner needs to register first
#            # return redirect('shopowner_reg')
#              message_error="owner is not exists"
#              return render(request, 'shopreg.html',{'message_error': message_error})
             
#             #  return redirect('shopowner_reg')  # Redirect to shopowner_reg page
#     return render(request, 'shopreg.html')

from django.shortcuts import render, redirect
from .models import ShopOwner, SuperMarket

def register_shop(request):
    message_error = None
    
    if request.method == 'POST':
        # Get the form data for SuperMarket
        shop_name = request.POST['uname']
        shop_mail = request.POST['email']
        shop_type = request.POST['type']
        shop_opentime = request.POST['opentime']
        shop_closetime = request.POST['closetime']
        shop_phonenumber = request.POST['num']
        shop_address = request.POST['address']
        lat = request.POST['lat']
        lng = request.POST['lan']
        owner_email = request.POST['oemail']  # Add this line to get owner email from form

        # Get the image file from the form
        image_file = request.FILES.get('image')
        print(image_file)
        # Check if the owner with the given email already exists
        owner = ShopOwner.objects.filter(o_mail=owner_email).first()

        if owner:
            # Owner exists, proceed to register the shop
            # Create a new SuperMarket instance and set its attributes
            market = SuperMarket(
                s_name=shop_name,
                s_mail=shop_mail,
                s_phonenumber=shop_phonenumber,
                s_type=shop_type,
                s_address=shop_address,
                s_opentime=shop_opentime,
                s_closetime=shop_closetime,
                latitude=lat,
                longitude=lng,
                image=image_file,# Set the image field
                owner=owner  # Set the owner for the SuperMarket
               
            )

            # Save the SuperMarket instance to the database
            market.save()
            request.session['shop_id'] = market.s_id
            return redirect('shopownerprofile_op')  # Redirect to shopownerprofile_op page
        else:
            # Owner does not exist, redirect to a page indicating that the owner needs to register first
            message_error = "Owner does not exist. Please register as an owner first."
            return render(request, 'shopreg.html', {'message_error': message_error})

    return render(request, 'shopreg.html')


def shopowner_login(request):
    return render(request, 'shopowner_login.html')


def ownerwelcome(request):
    return render(request, 'welcome_page_to_owner.html')

def shop_owner_profile(request):
    return render(request,'shopownerprofile.html')
# def shopowner_login_operation(request):

# from django.shortcuts import render
# from .models import ShopOwner, SuperMarket

# def shopownerprofile_op(request):
#     owner_id = request.session.get('owner_id')
#     if owner_id:   
#         owner = ShopOwner.objects.get(pk=owner_id)
#         shops = SuperMarket.objects.filter(owner=owner)
        
#         return render(request, 'welcome_page_to_owner.html', {'owner': owner, 'shops': shops})
#     else:
#         return redirect('ownerwelcome')


# from django.shortcuts import render, redirect
# from .models import ShopOwner, SuperMarket, Order  # Ensure Order is imported

# def shopownerprofile_op(request):
#     owner_id = request.session.get('owner_id')
#     if owner_id:   
#         owner = ShopOwner.objects.get(pk=owner_id)
#         shops = SuperMarket.objects.filter(owner=owner)
        
#         shop_orders = []
#         for shop in shops:
#             new_orders_count = Order.objects.filter(shop=shop, is_new=True).count()  # Example condition
#             shop_orders.append({
#                 'shop': shop,
#                 'new_orders_count': new_orders_count
#             })
        
#         return render(request, 'welcome_page_to_owner.html', {'owner': owner, 'shop_orders': shop_orders})
#     else:
#         return redirect('ownerwelcome')


# from django.shortcuts import render, redirect
# from .models import ShopOwner, SuperMarket, Order

# def shopownerprofile_op(request):
#     owner_id = request.session.get('owner_id')
#     if owner_id:   
#         owner = ShopOwner.objects.get(pk=owner_id)
#         shops = SuperMarket.objects.filter(owner=owner)
        
#         shop_orders = []
#         for shop in shops:
#             new_orders_count = Order.objects.filter(supermarket=shop, is_new=True).count()
#             shop_orders.append({
#                 'shop': shop,
#                 'new_orders_count': new_orders_count
#             })
        
#         return render(request, 'welcome_page_to_owner.html', {'owner': owner, 'shop_orders': shop_orders})
#     else:
#         return redirect('ownerwelcome')


from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import ShopOwner, SuperMarket, Order

def shopownerprofile_op(request):
    owner_id = request.session.get('owner_id')
    if owner_id:   
        owner = ShopOwner.objects.get(pk=owner_id)
        shops = SuperMarket.objects.filter(owner=owner)
        
        shop_orders = []
        for shop in shops:
            recent_time = timezone.now() - timedelta(hours=3)  # Last 3 hours
            new_orders_count = Order.objects.filter(supermarket=shop, is_new=True, order_date__gte=recent_time).count()
            shop_orders.append({
                'shop': shop,
                'new_orders_count': new_orders_count
            })
        
        return render(request, 'welcome_page_to_owner.html', {'owner': owner, 'shop_orders': shop_orders})
    else:
        return redirect('ownerwelcome')
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Order, SuperMarket

def order_list_view(request, shop_id):
    shop = get_object_or_404(SuperMarket, pk=shop_id)
    request.session['shop_id']=shop_id
    
    recent_time = timezone.now() - timedelta(hours=3)  # Last 3 hours
    orders = Order.objects.filter(supermarket=shop, order_date__gte=recent_time)
    return render(request, 'order_listatshoptime.html', {'shop': shop, 'orders': orders})

# def update_order_view(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     status_sequence = ['PLACED', 'ORDERCOMMITTED', 'PACKED', 'DISPATCHED', 'DELIVERED', 'CANCELLED']
#     current_status_index = status_sequence.index(order.order_status)
    
#     # Move to the next status
#     if current_status_index < len(status_sequence) - 1:
#         order.order_status = status_sequence[current_status_index + 1]
        
#         # Mark the order as not new if status is cancelled or delivered
#         if order.order_status in ['CANCELLED', 'DELIVERED']:
#             order.is_new = False
        
#         order.save()
#     shop_id = request.session.get('shop_id')
#     return redirect('order_list_view', shop_id)


from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Order, SuperMarket

def update_order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    status_sequence = ['PLACED', 'ORDERCOMMITTED', 'PACKED', 'DISPATCHED', 'DELIVERED', 'CANCELLED']
    current_status_index = status_sequence.index(order.order_status)
    
    # Move to the next status
    if current_status_index < len(status_sequence) - 1:
        order.order_status = status_sequence[current_status_index + 1]
        
        # Mark the order as not new if status is cancelled or delivered
        if order.order_status in ['CANCELLED', 'DELIVERED']:
            order.is_new = False
        
        order.save()
    shop_id = request.session.get('shop_id')
    return redirect('order_list_view', shop_id)
    

def shopowner_onlyprofile(request):
    owner_id = request.session.get('owner_id')
    if owner_id:   
        owner = ShopOwner.objects.get(pk=owner_id)
        shops = SuperMarket.objects.filter(owner=owner)
        return render(request, 'shopownerprofile.html', {'owner': owner, 'shops': shops})
    else:
        return redirect('ownerwelcome')




def delivery_boy_profile(request):
    d_id = request.session.get('delivery_boy_id')
    if d_id:   
        owner = DeliveryBoy.objects.get(pk=d_id)
        # shops = SuperMarket.objects.filter(owner=owner)
        return render(request, 'delivery_boy_profile.html', {'owner': owner})
    else:
        return redirect('delivery_boy_home')




# def welcome_page_to_owner(request):--------------------------
#     email=request.session.get('shopownermail')
#     print(email)
#     owner = ShopOwner.objects.filter(o_mail=email).first()
#     return render(request, 'welcome_page_to_owner.html', {'owner': owner})

# def register_shop(request):
#     if request.method == 'POST':
#         # Get the form data for SuperMarket
#         shop_name = request.POST['uname']
#         shop_mail = request.POST['email']
#         shop_type = request.POST['type']
#         shop_opentime = request.POST['opentime']
#         shop_closetime = request.POST['closetime']
#         shop_phonenumber = request.POST['num']
#         shop_address = request.POST['address']
#         owner_email = request.POST['owner_email']  # Add this line to get owner email from form

#         # Check if the owner with the given email already exists
#         owner = ShopOwner.objects.filter(o_mail=owner_email).first()

#         if owner:
#             # Owner exists, proceed to register the shop
#             # Create a new SuperMarket instance, set the owner, and save it
#             market = SuperMarket.objects.create(
#                 s_name=shop_name,
#                 s_mail=shop_mail,
#                 s_phonenumber=shop_phonenumber,
#                 s_type=shop_type,
#                 s_address=shop_address,
#                 s_opentime=shop_opentime,
#                 s_closetime=shop_closetime,
#                 owner=owner  # Set the owner for the SuperMarket
#             )

#             return redirect('success_page')  # Redirect to success page
#         else:
#             # Owner does not exist, redirect to a page indicating that the owner needs to register first
#             return redirect('shopowner_reg')

#     return render(request, 'shopreg.html')

def success_page(request):
    return render(request, 'home.html')


#     error_message1 = None
#     error_message2=None
    
#     if request.method == 'POST':
#         owner_email = request.POST.get('mail')
#         owner_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = ShopOwner.objects.get(o_mail=owner_email)
#             de_password=decode_password(owner_pass)
#             print(de_password)
#             # # Check if the email and password match
#             # if check_password(owner_pass,de_password):
#             #     # Authentication succeeds, redirect to the home page
#             #     return redirect('ownerwelcome')
            
#             # Check if the email and password match
#             if check_password(de_password, user.o_password):
#                 # Authentication succeeds, redirect to the home page
#                 return redirect('ownerwelcome')
#             else:
#                 # Password does not match, render the login page with error message
#                 error_message1 = "Invalid password . so, please enter correct password!!"
#                 return render(request, 'shopowner_login.html', {'error_message1': error_message1})
          
#         except ShopOwner.DoesNotExist:
#             # User with provided email does not exist, render the login page with error message
#             error_message2 = "User with this email does not exist."
#             return render(request, 'shopowner_login.html', {'error_message2': error_message2})

#     else:
#         # GET request, render the login page
#         return render(request, 'shopowner_login..html')

# from django.contrib.auth.hashers import check_password

# def shopowner_login_operation(request):
#     error_message = None
    
#     if request.method == 'POST':
#         owner_email = request.POST.get('mail')
#         owner_pass = request.POST.get('password')

#         try:
#             # Retrieve user based on email
#             user = ShopOwner.objects.get(o_mail=owner_email)
            
#             # Check if the password matches
#             if c_password(owner_pass):
#                 # Authentication succeeds, redirect to the home page
#                 return redirect('ownerwelcome')
#             else:
#                 # Password does not match, render the login page with error message
#                 error_message = "Invalid email or password. Please try again."
          
#         except ShopOwner.DoesNotExist:
#             # User with provided email does not exist, render the login page with error message
#             error_message = "User with this email does not exist."
        
#     # Render the login page with error message if exists
#     return render(request, 'shopowner_login.html', {'error_message': error_message})


# this is also working  for forgot password to display ..
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import mainuser
# def fgpm(request,):
#     error_message=None
#     if request.method == 'POST':
#         entered_email= request.POST['forgotemail']
    
#         # Check if the email exists in the MainUser model
#         try:
#             user = mainuser.objects.get(user_mail=entered_email)
#             # Send email for password reset
#             # if user:
            
#             p=user.user_password
#             fp=decode_password(p)
#             # subject = 'Multiple Messages in One Email'
#             message = f"""\
#             <html>
#             <body>
#             <p>your password:</p>
#             <hr>
#             <h1>{fp}</h1>
#             </body>
#             </html>
#             """
#             # message = f"Your password is: {fp}"
#             send_mail('SmartMart',message,'settings.EMAIL_HOST_USER',[entered_email],fail_silently=False) 
#         #      send_mail(
#         # subject,
#         # '',
#         # from_email,
#         # recipient_list,
#         # html_message=message,
#         # fail_silently=False,
#     # )         
#               # You may want to redirect to a success page after sending the email
#             return render(request, 'forgotpasssucces.html')
#         except mainuser.DoesNotExist:
#             # If the email doesn't exist, display an error message
#             error_message = 'This email is not registered.'
#             return render(request, 'forgotoss.html', {'error_message': error_message})
#     else:
#         # Handle GET request if needed
#         return render(request, 'forgotoss.html')



from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from .models import mainuser, ShopOwner

def fgpm(request):
    error_message = None
    if request.method == 'POST':
        entered_email = request.POST['forgotemail']
    
        # Check if the email exists in the mainuser model
        try:
            user = mainuser.objects.get(user_mail=entered_email)
            # Decode the password (assuming decode_password is a function you've defined)
            fp = decode_password(user.user_password)
            
            # HTML message with the password
            message = f"""\
            <html>
            <body>
                <p>Your password:</p>
                <hr>
                <h1>{fp}</h1>
            </body>
            </html>
            """
            
            # Create and send the email
            email = EmailMessage(
                'SmartMart',
                message,
                settings.EMAIL_HOST_USER,
                [entered_email]
            )
            email.content_subtype = 'html'  # Set the content to HTML
            email.send(fail_silently=False)
            
            # Redirect to a success page after sending the email
            return render(request, 'forgotpasssucces.html')
        except mainuser.DoesNotExist:
            # If the email doesn't exist, display an error message
            error_message = 'This email is not registered.'
    
    # Render the form again with an error message if there's an error or for GET request
    return render(request, 'forgotoss.html', {'error_message': error_message})



def fgpmshopowner(request):
    error_message = None
    if request.method == 'POST':
        entered_email = request.POST['forgotemail']
    
        # Check if the email exists in the mainuser model
        try:
            user = ShopOwner.objects.get(o_mail=entered_email)
            # Decode the password (assuming decode_password is a function you've defined)
            fp = decode_password(user.o_password)
            
            # HTML message with the password
            message = f"""\
            <html>
            <body>
                <p>Your password:</p>
                <hr>
                <h1>{fp}</h1>
            </body>
            </html>
            """
            
            # Create and send the email
            email = EmailMessage(
                'SmartMart',
                message,
                settings.EMAIL_HOST_USER,
                [entered_email]
            )
            email.content_subtype = 'html'  # Set the content to HTML
            email.send(fail_silently=False)
            
            # Redirect to a success page after sending the email
            return render(request, 'forgotpasssuccesshopowner.html')
        except mainuser.DoesNotExist:
            # If the email doesn't exist, display an error message
            error_message = 'This email is not registered.'
    
    # Render the form again with an error message if there's an error or for GET request
    return render(request, 'forgotpassshopowner.html', {'error_message': error_message})




from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from .models import mainuser, ShopOwner, DeliveryBoy

def deliveryboyfgp(request):
    error_message = None
    if request.method == 'POST':
        entered_email = request.POST['forgotemail']
    
        # Check if the email exists in the mainuser model
        try:
            user = DeliveryBoy.objects.get(email=entered_email)
            # Decode the password (assuming decode_password is a function you've defined)
            fp = decode_password(user.password)
            
            # HTML message with the password
            message = f"""\
            <html>
            <body>
                <p>Your password:</p>
                <hr>
                <h1>{fp}</h1>
            </body>
            </html>
            """
            
            # Create and send the email
            email = EmailMessage(
                'SmartMart',
                message,
                settings.EMAIL_HOST_USER,
                [entered_email]
            )
            email.content_subtype = 'html'  # Set the content to HTML
            email.send(fail_silently=False)
            
            # Redirect to a success page after sending the email
            return render(request, 'fgpdeliverysuccess.html')
        except DeliveryBoy.DoesNotExist:
            # If the email doesn't exist, display an error message
            error_message = 'This email is not registered.'
            # return render(request, 'forgotpasssucces.html')
            return render(request, 'forgotossdeliery.html', {'error_message': error_message})
    
    # Render the form again with an error message if there's an error or for GET request
    return render(request, 'forgotossdeliery.html')


# myapp/views.py
from django.shortcuts import render

# def maps(request):
#     return render(request, 'maps.html')


def forgotpasssucces(request):
    return render(request, 'forgotpasssucces.html')


# views.py
from django.shortcuts import render
from django.conf import settings
import googlemaps

def nearby_shops(request):
    # Get user's current location (you may need to implement this)
    user_location = {'lat': 18.530411, 'lng': 79.627179}  # Default to a location (e.g., somewhere in India)

    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    # Search for nearby shops
    places_result = gmaps.places_nearby(location=user_location, radius=500, type='store')

    # Process the fetched data
    shops = [{'name': place['name'], 'lat': place['geometry']['location']['lat'], 'lng': place['geometry']['location']['lng']} for place in places_result['results']]

    # Render template with map and shops
    return render(request, 'maps.html', {'user_location': user_location, 'shops': shops})


# from django.shortcuts import render, redirect
# from .models import categories

# def category_checkbox_view(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             for category_id in selected_categories:
#                 # Assuming category_id is directly used as category_name
#                 categories.objects.create(shop_id=shop_id, category_name=category_id)
#             return redirect('success_page')  # Redirect to success page after storing categories
#     else:
#         return render(request, 'category_checkbox.html')


def checkboxcategory(request):
    return render(request, 'checkboxcategory.html')


# def checkboxproducts(request):
#     if request.method=="POST":
#         selected_category_id=request.POST.get('selected_category_id')
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         return render(request, 'checkboxproducts.html',{'category':category})

# from django.shortcuts import render, get_object_or_404
# from .models import SuperMarket, categories, Product

# def checkboxproducts(request):
#     if request.method == "POST":
#         selected_category_id = request.POST.get('selected_category_id')
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
#         products = Product.objects.filter(category=category, shop=shop)
        
#         return render(request, 'checkboxproducts.html', {'category': category, 'products': products})
#     return redirect('display_categoriesshopowner')  # Redirect if the request method is not POST



# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories, Product

def checkboxproducts(request):
    if request.method == "POST":
        selected_category_id = request.POST.get('selected_category_id')
        shop_id = request.session.get('shop_id')
        shop = get_object_or_404(SuperMarket, pk=shop_id)
        
        category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        products = Product.objects.filter(category=category, shop=shop)
        
        return render(request, category.extemplate_name, {'category': category, 'products': products})
    return redirect('display_categoriesshopowner')  # Redirect if the request method is not POST


def add_products_view(request, cid):
    # if request.method == "POST":
        # selected_category_id = request.POST.get('selected_category_id')
        selected_category_id=cid
        shop_id = request.session.get('shop_id')
        shop = get_object_or_404(SuperMarket, pk=shop_id)
        
        category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        products = Product.objects.filter(category=category, shop=shop)
        
        return render(request, category.template_name, {'category': category, 'products': products})
    # return redirect('display_categoriesshopowner')  # Redirect if the request method is not POST

    # return render(request, 'existing_products.html', {'category': category})
# # from django.shortcuts import render
# from .models import categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             for category_id in selected_categories:
#                 # Create an instance of Categories for the selected category and shop
#                 categories.objects.create(shop_id=shop_id, category_name=category_id)
#             # Redirect to success page after storing categories
#             return render(request, 'shopownerprofile.html')
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')


from django.shortcuts import render, get_object_or_404
from .models import categories, SuperMarket

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
#                 if not existing_category:
#                     categories.objects.create(shop=shop, category_name=category_name)
#                 else:
#                     # return render(request, 'welcome_page_to_owner.html')
#                     return render(request, 'shopownerprofile.html', {'error': f"Category '{category_name}' already exists in the shop."})
#             # Redirect to success page after storing categories
#             # return render(request, 'shopownerprofile.html', {'success': "Categories added successfully"})
#             return render(request, 'welcome_page_to_owner.html')
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')

from django.shortcuts import render, get_object_or_404
from .models import SuperMarket, categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop,category_name=category_name).exists()
#                 if not existing_category:
#                     categories.objects.create(shop=shop, category_name=category_name)
            
#             # Redirect to success page after storing categories
#             return redirect('display_categoriesshopowner')
#             # return render(request, 'welcome_page_to_owner.html', {'success': "Categories added successfully"})
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
#                 if not existing_category:
#                     # Retrieve the corresponding image file
#                     image_field_name = f"category_image_category{category_name[-1]}"  # Assuming last digit corresponds to ID
#                     category_image = request.FILES.get(image_field_name)
                    
#                     categories.objects.create(shop=shop, category_name=category_name, category_image=category_image)
            
#             # Redirect to success page after storing categories
#             return redirect('display_categoriesshopowner')
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
#                 if not existing_category:
#                     # Retrieve the corresponding image URL
#                     image_field_name = f"category_image_{category_name}"
#                     category_image_url = request.POST.get(image_field_name)
                    
#                     categories.objects.create(shop=shop, category_name=category_name, category_image=category_image_url)
            
#             # Redirect to success page after storing categories
#             return redirect('display_categoriesshopowner')
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
#                 if not existing_category:
#                     # Retrieve the corresponding image URL
#                     image_field_name = f"category_image_{category_name}"
#                     category_image_url = request.POST.get(image_field_name)
                    
#                     # Save the category with the image URL
#                     categories.objects.create(shop=shop, category_name=category_name, category_image=category_image_url)
#                     print("111111222")
#             # Redirect to success page after storing categories
#             return redirect('display_categoriesshopowner')
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories

# def store_categories(request):
#     if request.method == 'POST':
#         selected_categories = request.POST.getlist('categories')
#         if selected_categories:
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             for category_name in selected_categories:
#                 # Check if the category already exists for the shop
#                 existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
#                 if not existing_category:
#                     # Retrieve the corresponding image URL
#                     image_field_name = f"category_image_{category_name}"
#                     category_image_url = request.POST.get(image_field_name)
                    
#                     # Save the category with the image URL
#                     categories.objects.create(shop=shop, category_name=category_name, category_image=category_image_url)
            
#             # Redirect to success page after storing categories
#             return redirect('display_categoriesshopowner')
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxcategory.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories

def store_categories(request):
    if request.method == 'POST':
        selected_categories = request.POST.getlist('categories')
        if selected_categories:
            shop_id = request.session.get('shop_id')
            shop = get_object_or_404(SuperMarket, pk=shop_id)
            print(shop_id)
            for category_name in selected_categories:
                # Check if the category already exists for the shop
                existing_category = categories.objects.filter(shop=shop, category_name=category_name).exists()
                if not existing_category:
                    print("111111111")
                    # Retrieve the corresponding image URL and template name
                    extemplate_name=f"extemplate_name_{category_name}"
                    template_field_name = f"template_name_{category_name}"
                    image_field_name = f"category_image_{category_name}"
                    
                    
                    category_image_url = request.POST.get(image_field_name)
                    template_name_value = request.POST.get(template_field_name)
                    extemplate_name_value=request.POST.get(extemplate_name)
                    print(category_image_url)
                    print(template_name_value)
                    # Save the category with the image URL and template name
                    categories.objects.create(
                        shop=shop, 
                        category_name=category_name, 
                        category_image=category_image_url,
                        template_name=template_name_value,
                        extemplate_name=extemplate_name_value
                    )
            
            # Redirect to success page after storing categories
            return redirect('display_categoriesshopowner')
    
    # Handle invalid requests or render form again
    return render(request, 'checkboxcategory.html')

# from django.shortcuts import render
# from .models import Product, categories

# def store_products(request):
#     if request.method == 'POST':
#         selected_products = request.POST.getlist('products')
#         # qu=request.POST.get('quantity')
#         if selected_products:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
            
#             # Fetch all category IDs for the shop
#             category_ids = categories.objects.filter(shop_id=shop_id).values_list('category_id', flat=True)
            
#             for product_name in selected_products:
#                 # Create a Product instance for each product and each category ID
#                 for category_id in category_ids:
#                     Product.objects.create(
#                         product_name=product_name,
#                         # quntity=qu,  # Adjust this based on your form structure
#                         category_id=category_id,
#                         shop_id=shop_id
#                     )
#                     # You may need to handle other fields similarly
#             # Redirect to success page after storing products
#             return render(request, 'shopownerprofile.html')
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')
# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         selected_products = request.POST.getlist('products')
#         if selected_products:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Fetch all category IDs for the shop
#             category_ids = categories.objects.filter(shop=shop).values_list('category_id', flat=True)
            
#             for product_name in selected_products:
#                 # Check if the product already exists in the shop
#                 if not Product.objects.filter(product_name=product_name, shop=shop).exists():
#                     for category_id in category_ids:
#                         Product.objects.create(
#                             product_name=product_name,
#                             category_id=category_id,
#                             shop_id=shop_id
#                         )
#                 else:
#                     return render(request, 'shopownerprofile.html', {'error': f"Product '{product_name}' already exists in the shop."})
            
#             # Redirect to success page after storing products
#             return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')


# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket
# from django.db import IntegrityError

# def store_products(request):
#     if request.method == 'POST':
#         selected_products = request.POST.getlist('products')
#         if selected_products:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Fetch all category IDs for the shop
#             category_ids = categories.objects.filter(shop=shop).values_list('category_id', flat=True)
            
#             for product_name in selected_products:
#                 # Check if the product already exists in the shop for any category
#                 existing_product = Product.objects.filter(product_name=product_name, shop=shop).exists()
#                 if not existing_product:
#                     for category_id in category_ids:
#                         try:
#                             Product.objects.create(
#                                 product_name=product_name,
#                                 category_id=category_id,
#                                 shop_id=shop_id
#                             )
#                         except IntegrityError:
#                             return render(request, 'shopownerprofile.html', {'error': f"Product '{product_name}' already exists in the shop."})
#                 else:
#                     return render(request, 'shopownerprofile.html', {'error': f"Product '{product_name}' already exists in the shop."})
            
#             # Redirect to success page after storing products
#             return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')


# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket
# from django.db import IntegrityError

# def store_products(request):
#     if request.method == 'POST':
#         selected_products = request.POST.getlist('products')
#         if selected_products:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Fetch all category IDs for the shop
#             category_ids = categories.objects.filter(shop=shop).values_list('category_id', flat=True)
            
#             for product_name in selected_products:
#                 # Check if the product already exists in the shop for any category
#                 existing_product = Product.objects.filter(product_name=product_name, shop=shop).exists()
#                 if not existing_product:
#                     for category_id in category_ids:
#                         try:
#                             Product.objects.create(
#                                 product_name=product_name,
#                                 category_id=category_id,
#                                 shop_id=shop_id
#                             )
#                         except IntegrityError:
#                             # Skip if the product already exists for the current category
#                             pass
            
#             # Redirect to success page after storing products
#             return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')


# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket
# from django.db import IntegrityError

# def store_products(request):
#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category')
#         if selected_category_id:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Check if the selected category belongs to the shop
#             category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
            
#             # Get all selected products for this category from the form
#             selected_products = request.POST.getlist('products')
            
#             if selected_products:
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop for the selected category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category).exists()
#                     if not existing_product:
#                         try:
#                             Product.objects.create(
#                                 product_name=product_name,
#                                 category=category,
#                                 shop=shop
#                             )
#                         except IntegrityError:
#                             # Skip if the product already exists for the current category
#                             pass
            
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')

def showcataddproducts(request):
    return render(request, 'showcataddproducts.html')


# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category')
#         if selected_category_id:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Check if the selected category belongs to the shop
#             category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
            
#             # Get all selected products for this category from the form
#             selected_products = request.POST.getlist('products')
            
#             if selected_products:
#                 for product_name in selected_products:
#                     # Create Product instances for each selected product
#                     Product.objects.create(
#                         product_name=product_name,
#                         category=category,
#                         shop=shop
#                     )
                
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')



# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category')
#         print("11111111111111111")
#         if selected_category_id:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             print("2222222222222")
#             # Check if the selected category belongs to the shop
#             category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
            
#             # Get all selected products for this category from the form
#             selected_products = request.POST.getlist('products')
#             print("3333333333")
#             if selected_products:
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop and category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     print("44444444444")
#                     if not existing_product:
#                         # Create Product instance for the product if it doesn't exist
#                         Product.objects.create(
#                             product_name=product_name,
#                             category=category,
#                             shop=shop
#                         )
                
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     print("5555555555555")
#     return render(request, 'checkboxproducts.html')



# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category')
#         if selected_category_id:
#             # Assuming shop_id is stored in session
#             shop_id = request.session.get('shop_id')
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             print(shop_id)
#             print(shop)
#             # Check if the selected category belongs to the shop
#             category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
            
#             # Get all selected products for this category from the form
#             selected_products = request.POST.getlist('products')
            
#             if selected_products:
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop and category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     if not existing_product:
#                         # Create Product instance for the product if it doesn't exist
#                         Product.objects.create(
#                             product_name=product_name,
#                             category=category,
#                             shop=shop
#                         )
                
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')





# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         # Get the selected category name from the form
#         selected_category_name = request.POST['selected_category']
#         # Get the shop ID from the session
#         shop_id = request.session.get('shop_id')
#         print(shop_id)
#         if selected_category_name and shop_id:
#             # Get the category associated with the selected name and shop ID
#             category = get_object_or_404(categories, category_name=selected_category_name, shop_id=shop_id)
#             # Get all selected products for this category from the form
#             selected_products = request.POST.getlist('products')
#             print(selected_products)
#             if selected_products:
#                 # Assuming shop is already fetched from the session
#                 shop = get_object_or_404(SuperMarket, pk=shop_id)
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop and category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     if not existing_product:
#                         # Create Product instance for the product if it doesn't exist
#                         Product.objects.create(
#                             product_name=product_name,
#                             category=category,
#                             shop=shop
#                         )
#                         print(f"Product '{product_name}' added successfully")
#                     else:
#                         print(f"Product '{product_name}' already exists in the shop and category.")
                
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     # Render form again if request method is not POST or if there's missing data
#     return render(request, 'checkboxproducts.html')



# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         print("Request method is POST")
#         print("POST data:", request.POST)
#         shop_id = request.session.get('shop_id')
#         print("Shop ID:", shop_id)
        
#         # Check if 'selected_category' key exists in POST data
#         if 'selected_category' in request.POST:
#             selected_category_name = request.POST['selected_category']
#             print("Selected category name:", selected_category_name)
            
#             # Fetch the category ID associated with the selected category name and the current shop ID
#             category = get_object_or_404(categories, category_name=selected_category_name, shop_id=shop_id)
#             selected_category_id = category.category_id
#             print("Selected category ID:", selected_category_id)
            
#             if selected_category_id:
#                 shop = get_object_or_404(SuperMarket, pk=shop_id)
                
#                 # Check if the selected category belongs to the shop
#                 category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
#                 print("Selected category:", category)
                
#                 # Get all selected products for this category from the form
#                 selected_products = request.POST.getlist('products')
#                 print("Selected products:", selected_products)
                
#                 if selected_products:
#                     for product_name in selected_products:
#                         # Check if the product already exists in the shop and category
#                         existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                         if not existing_product:
#                             # Create Product instance for the product if it doesn't exist
#                             Product.objects.create(
#                                 product_name=product_name,
#                                 category=category,
#                                 shop=shop
#                             )
#                             print(f"Product '{product_name}' added successfully")
#                         else:
#                             print(f"Product '{product_name}' already exists in the shop and category.")
                    
#                     # Redirect to success page after storing products
#                     return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')



# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         print("Request method is POST")
#         print("POST data:", request.POST)
#         shop_id = request.session.get('shop_id')
#         print("Shop ID:", shop_id)
        
#         # Check if 'selected_category' key exists in POST data
#         if 'selected_category' in request.POST:
#             selected_category_name = request.POST['selected_category']
#             print("Selected category name:", selected_category_name)
            
#             # Fetch the category ID associated with the selected category name and the current shop ID
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             category = get_object_or_404(categories, category_name=selected_category_name, shop=shop)
#             selected_category_id = category.category_id
#             print("Selected category ID:", selected_category_id)
#             selected_products = request.POST.getlist('products')
#             if selected_category_id:
#                 # Proceed with storing products
#                 # Rest of your code goes here
#                 #  Assuming shop is already fetched from the session
#                 shop = get_object_or_404(SuperMarket, pk=shop_id)
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop and category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     if not existing_product:
#                         # Create Product instance for the product if it doesn't exist
#                         Product.objects.create(
#                             product_name=product_name,
#                             category=category,
#                             shop=shop
#                         )
#                         print(f"Product '{product_name}' added successfully")
#                     else:
#                         print(f"Product '{product_name}' already exists in the shop and category.")
                
#                 # Redirect to success page after storing products
#                 return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
                
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')
# def fetchdata(request,selected_products):
#     selected_products= request.POST.getlist('products')
#     return selected_products
      




# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     if request.method == 'POST':
#         print("Request method is POST")
#         print("POST data:", request.POST)
#         shop_id = request.session.get('shop_id')
#         print("Shop ID:", shop_id)
        
#         # Check if 'selected_category' key exists in POST data
#         if 'selected_category' in request.POST:
#             selected_category_name = request.POST['selected_category']
#             print("Selected category name:", selected_category_name)
            
#             # Fetch the category ID associated with the selected category name and the current shop ID
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             category = get_object_or_404(categories, category_name=selected_category_name, shop=shop)
#             selected_category_id = category.category_id
#             print("Selected category ID:", selected_category_id)
            
#             if selected_category_id:
#                 # Get all selected products for this category from the form
                                      
#                 # selected_products =  fetchdata(selected_products)
#                 selected_products = request.POST.getlist('products')
#                 print(selected_products)
#                 if selected_products:
#                     # Assuming shop is already fetched from the session
#                     for product_name in selected_products:
#                         # Check if the product already exists in the shop and category
#                         existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                         if not existing_product:
#                             # Create Product instance for the product if it doesn't exist
#                             Product.objects.create(
#                                 product_name=product_name,
#                                 category=category,
#                                 shop=shop
#                             )
#                             print(f"Product '{product_name}' added successfully")
#                         else:
#                             print(f"Product '{product_name}' already exists in the shop and category.")
                    
#                     # Redirect to success page after storing products
#                     return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     # Handle invalid requests or render form again
#     return render(request, 'checkboxproducts.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, categories, SuperMarket

def select_category(request):
    shop_id = request.session.get('shop_id')
    shop = get_object_or_404(SuperMarket, pk=shop_id)
    category_list = categories.objects.filter(shop=shop)
    
    return render(request, 'showcataddproducts.html', {'categories': category_list})

def select_products(request):
    if request.method == 'POST':
        selected_category_name = request.POST['selected_category']
        shop_id = request.session.get('shop_id')
        shop = get_object_or_404(SuperMarket, pk=shop_id)
        category = get_object_or_404(categories, category_name=selected_category_name, shop=shop)
        
        return render(request, 'checkboxproducts.html', {'category': category})
    return redirect('select_category')

# def store_products(request):
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         # print(shop_id)
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         selected_category_id = request.POST['selected_category_id']
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')
#         print(selected_products)  # Debugging line to check selected products
#         if selected_products:
#             for product_name in selected_products:
#                 existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                 if not existing_product:
#                     Product.objects.create(
#                         product_name=product_name,
#                         category=category,
#                         shop=shop
#                     )
#                     print(f"Product '{product_name}' added successfully")
#                 else:
#                     print(f"Product '{product_name}' already exists in the shop and category.")
            
#             return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     return redirect('select_category')



# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def store_products(request):
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         selected_category_id = request.POST['selected_category_id']
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')
#         product_prices = request.POST.getlist('prices')

#         if selected_products and product_prices:
#             for product_name, product_price in zip(selected_products, product_prices):
#                 existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                 if not existing_product:
#                     Product.objects.create(
#                         product_name=product_name,
#                         product_price=float(product_price),
#                         category=category,
#                         shop=shop
#                     )
#                     print(f"Product '{product_name}' added successfully with price {product_price}")
#                 else:
#                     print(f"Product '{product_name}' already exists in the shop and category.")
            
#             return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
    
#     return redirect('select_category')




# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def store_products(request):
#     error_message="somethig got error in it...."
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         selected_category_id = request.POST.get('selected_category_id')
#         print(selected_category_id)
#         if not selected_category_id:
#             # return redirect('select_category')  # or handle this error appropriately
#             return redirect('display_categoriesshopowner')

#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')
#         product_prices = request.POST.getlist('prices')

#         if selected_products and product_prices:
#             for product_name, product_price in zip(selected_products, product_prices):
#                 existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                 if not existing_product:
#                     Product.objects.create(
#                         product_name=product_name,
#                         product_price=float(product_price),
#                         # product_price=(product_price),
#                         category=category,
#                         shop=shop
#                     )
#                     print(f"Product '{product_name}' added successfully with price {product_price}")
#                 else:
#                     print(f"Product '{product_name}' already exists in the shop and category.")
            
#             # return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
#             # return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
#             return redirect('display_categoriesshopowner')
    
#     # return redirect('select_category')
#     return redirect('display_categoriesshopowner')


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def store_products(request):
#     error_message = "Something went wrong..."
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         selected_category_id = request.POST.get('selected_category_id')
#         print(selected_category_id)
#         if not selected_category_id:
#             return redirect('display_categoriesshopowner')

#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')
#         product_prices = request.POST.getlist('prices')

#         if selected_products and product_prices:
#             for product_name, product_price in zip(selected_products, product_prices):
#                 if product_name and product_price:  # Ensure both fields are not empty
#                     try:
#                         product_price_float = float(product_price)
#                     except ValueError:
#                         print(f"Invalid price for product '{product_name}': '{product_price}'")
#                         continue  # Skip this product and move to the next

#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     if not existing_product:
#                         Product.objects.create(
#                             product_name=product_name,
#                             product_price=product_price_float,
#                             category=category,
#                             shop=shop
#                         )
#                         print(f"Product '{product_name}' added successfully with price {product_price_float}")
#                     else:
#                         print(f"Product '{product_name}' already exists in the shop and category.")
#                 else:
#                     print(f"Product name or price missing for one of the entries: {product_name}, {product_price}")
            
#             return redirect('display_categoriesshopowner')
    
#     return redirect('display_categoriesshopowner')


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def store_products(request):
#     error_message = "Something went wrong..."
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
        
#         selected_category_id = request.POST.get('selected_category_id')
#         print(selected_category_id)
#         if not selected_category_id:
#             return redirect('display_categoriesshopowner')

#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')

#         for product_name in selected_products:
#             product_price_key = f'prices_{product_name.replace(" ", "").lower()}'
#             product_price = request.POST.get(product_price_key)
            
#             if product_name and product_price:  # Ensure both fields are not empty
#                 try:
#                     product_price_float = float(product_price)
#                 except ValueError:
#                     print(f"Invalid price for product '{product_name}': '{product_price}'")
#                     continue  # Skip this product and move to the next

#                 existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                 if not existing_product:
#                     Product.objects.create(
#                         product_name=product_name,
#                         product_price=product_price_float,
#                         category=category,
#                         shop=shop
#                     )
#                     print(f"Product '{product_name}' added successfully with price {product_price_float}")
#                 else:
#                     print(f"Product '{product_name}' already exists in the shop and category.")
#             else:
#                 print(f"Product name or price missing for one of the entries: {product_name}, {product_price}")
            
#         return redirect('display_categoriesshopowner')
    
#     return redirect('display_categoriesshopowner')



# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def store_products(request):
#     print("111111111")
#     if request.method == 'POST':
#         print("222222222")
#         shop_id = request.session.get('shop_id')
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         print(shop_id)
#         selected_category_id = request.POST.get('selected_category_id')
#         if not selected_category_id:
#             return redirect('display_categoriesshopowner')

#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         selected_products = request.POST.getlist('products')
#         print(select_products)
#         for product_name in selected_products:
#             product_price_key = f'prices_{product_name.replace(" ", "").lower()}'
#             product_price = request.POST.get(product_price_key)
            
#             if product_name and product_price:  # Ensure both fields are not empty
#                 try:
#                     product_price_float = float(product_price)
#                 except ValueError:
#                     print(f"Invalid price for product '{product_name}': '{product_price}'")
#                     continue  # Skip this product and move to the next

#                 existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                 if not existing_product:
#                     # Retrieve the corresponding image URL
#                     image_field_name = f"product_image_{product_name.replace(' ', '').lower()}"
#                     product_image_url = request.POST.get(image_field_name)
                    
#                     Product.objects.create(
#                         product_name=product_name,
#                         product_price=product_price_float,
#                         category=category,
#                         shop=shop,
#                         product_image=product_image_url
#                     )
#                     print(f"Product '{product_name}' added successfully with price {product_price_float}")
#                 else:
#                     print(f"Product '{product_name}' already exists in the shop and category.")
#             else:
#                 print(f"Product name or price missing for one of the entries: {product_name}, {product_price}")
            
#         return redirect('display_categoriesshopowner')
    
#     return redirect('display_categoriesshopowner')


from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperMarket, categories, Product

def store_products(request):
    if request.method == 'POST':
        shop_id = request.session.get('shop_id')
        shop = get_object_or_404(SuperMarket, pk=shop_id)
        
        selected_category_id = request.POST.get('selected_category_id')
        if not selected_category_id:
            return redirect('display_categoriesshopowner')

        category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
        selected_products = request.POST.getlist('products')
        
        for product_name in selected_products:
            product_price_key = f'prices_{product_name.replace(" ", "").lower()}'
            product_price = request.POST.get(product_price_key)
            
            if product_name and product_price:  # Ensure both fields are not empty
                try:
                    product_price_float = float(product_price)
                except ValueError:
                    print(f"Invalid price for product '{product_name}': '{product_price}'")
                    continue  # Skip this product and move to the next

                existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
                if not existing_product:
                    # Retrieve the corresponding image URL
                    image_field_name = f"product_image_{product_name.replace(' ', '').lower()}"
                    product_image_url = request.POST.get(image_field_name)
                    
                    Product.objects.create(
                        product_name=product_name,
                        product_price=product_price_float,
                        category=category,
                        shop=shop,
                        product_image=product_image_url
                    )
                    print(f"Product '{product_name}' added successfully with price {product_price_float}")
                else:
                    print(f"Product '{product_name}' already exists in the shop and category.")
            else:
                print(f"Product name or price missing for one of the entries: {product_name}, {product_price}")
            
        return redirect('display_categoriesshopowner')
    
    return redirect('display_categoriesshopowner')

# from django.shortcuts import render, get_object_or_404
# from .models import Product, categories, SuperMarket

# def store_products(request):
#     # if request.method == 'POST':
#     #     print("Request method is POST")
#     #     print("POST data:", request.POST)
#     #     selected_category_id = request.POST.get('selected_category')
#     #     print("Selected category ID:", selected_category_id)
#      if request.method == 'POST':
#         print("Request method is POST")
#         print("POST data:", request.POST)
#         shop_id = request.session.get('shop_id')
#         print("Shop ID:", shop_id)
#         if shop_id:
#             selected_category_name = request.POST['selected_category']
#             print("Selected category name:", selected_category_name)
            
#             # Fetch the category ID associated with the selected category name and the current shop ID
#             category = get_object_or_404(categories, category_name=selected_category_name, shop_id=shop_id)
#             selected_category_id = category.category_id
#             print("Selected category ID:", selected_category_id)
#             if selected_category_id:
#             # Assuming shop_id is stored in session
#                 shop_id = request.session.get('shop_id')
#                 print("Shop ID:", shop_id)
#                 shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # Check if the selected category belongs to the shop
#                 category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
#                 print("Selected category:", category)
            
#             # Get all selected products for this category from the form
#                 selected_products = request.POST.getlist('products')
#                 print("Selected products:", selected_products)
            
#             if selected_products:
#                 for product_name in selected_products:
#                     # Check if the product already exists in the shop and category
#                     existing_product = Product.objects.filter(product_name=product_name, category=category, shop=shop).exists()
#                     if not existing_product:
#                         # Create Product instance for the product if it doesn't exist
#                         Product.objects.create(
#                             product_name=product_name,
#                             category=category,
#                             shop=shop
#                         )
#                         print(f"Product '{product_name}' added successfully")
#                     else:
#                         print(f"Product '{product_name}' already exists in the shop and category.")
                
#                 # Redirect to success page after storing products
#                     return render(request, 'shopownerprofile.html', {'success': "Products added successfully"})
        
#     # Handle invalid requests or render form again
#     # print("Invalid request method or missing data.")
#         return render(request, 'checkboxproducts.html')

def shopcatalog(request):
    return render(request,'shopcatalog.html')

# from django.shortcuts import render
# from .models import categories

# def display_categories(request):
#     error_message=None
#     # Assuming shop_id is stored in session
#     # shop_id = request.session.get('shop_id')
#     shop_id=request.POST['shopid']
#     # if shop_id:
#     if not SuperMarket.objects.filter(pk=shop_id).exists():
#          error_message = "Invalid shop_id."
#          return render(request, 'maps.html', {'error_message1': error_message})
         
#             # return HttpResponse("Shop ID does not exist.") 
#         # Fetch all categories associated with the shop
#     shop_categories = categories.objects.filter(shop_id=shop_id)
    
#     # Pass the categories to the template for rendering
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})

# from django.shortcuts import render
# from .models import categories, SuperMarket

# def display_categories(request):
#     error_message = None
#     shop_id = request.POST['shopid']
#     request.session['shop_id'] = shop_id
#     # Get shop_id from POST data
#     # request.session['shop_id'] = shop_id
#     if not shop_id or not SuperMarket.objects.filter(pk=shop_id).exists():
#         error_message = "Invalid shop_id."
#         return render(request, 'maps.html', {'error_message1': error_message})
    
#     # Fetch all categories associated with the shop
#     shop_categories = categories.objects.filter(shop_id=shop_id)
    
#     # Pass the categories to the template for rendering
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})
# from django.shortcuts import render, get_object_or_404
# from .models import SuperMarket, categories

# def display_categories(request):
#     # request.session.flush() # clear all the data in sessions
#     error_message = None

#     if request.method == 'POST':
#         # shop_id = request.POST.get('shopid')
#         shop_id = request.POST['shopid']
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid shop_id."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []
#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
#     # request.session['selected_products'] = []
#     shop_categories = categories.objects.filter(shop_id=shop_id)
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})


from django.shortcuts import render, get_object_or_404
from .models import SuperMarket,categories # Updated import for Category model

# def display_categories(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST['shopid']
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []
#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})

    # shop = get_object_or_404(SuperMarket, pk=shop_id)
    # shop_categories = categories.objects.filter(shop=shop)
    
    # return render(request, 'shopcatalog.html', {'categories': shop_categories})


# def display_categories(request):
#     if request.method == 'POST':
#         shop_id = request.POST['shopid']
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []
        

#     elif request.method=="GET":
        
#         shop_id =  request.GET.get('shopid')
#         category_name = request.GET.get('name')
#         if category_name:
#             shop_categories = categories.objects.filter(shop=shop, name__icontains=category_name)
#         else:
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             shop_categories = categories.objects.filter(shop=shop)

#             return render(request, 'shopcatalog.html', {'categories': shop_categories})

#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
#     error_message = None

#     if not shop_id:
#         error_message = "Shop ID is required."
#         return render(request, 'maps.html', {'error_message1': error_message})
    
#     if not SuperMarket.objects.filter(pk=shop_id).exists():
#         error_message = "Invalid Shop ID."
#         return render(request, 'maps.html', {'error_message1': error_message})

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
    
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})

    
# from django.shortcuts import render, get_object_or_404
# from .models import SuperMarket, categories

# def display_categories(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST.get('shopid')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []

#     elif request.method == 'GET':
#         shop_id = request.GET.get('shopid')
#         category_name = request.GET.get('name')
        
#         if shop_id:
#             if not SuperMarket.objects.filter(pk=shop_id).exists():
#                 error_message = "Invalid Shop ID."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             request.session['shop_id'] = shop_id
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             # if category_name:
#             #     shop_categories = categories.objects.filter(shop=shop, name__icontains=category_name)
#             # else:
#             shop_categories = categories.objects.filter(shop=shop)

#             return render(request, 'shopcatalog.html', {'categories': shop_categories,'shop':shop})
        
#         else:
#             shop_id = request.session.get('shop_id')
#             if not shop_id:
#                 error_message = "Shop ID is required."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             shop_categories = categories.objects.filter(shop=shop)
#             return render(request, 'shopcatalog.html', {'categories': shop_categories,'shop':shop})

#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})

#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         shop_categories = categories.objects.filter(shop=shop)
#         return render(request, 'shopcatalog.html', {'categories': shop_categories,'shop':shop})

#     if error_message:
#         return render(request, 'maps.html', {'error_message1': error_message})
#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
#     return render(request, 'shopcatalog.html', {'categories': shop_categories,'shop':shop})




# def display_products(request):
#     print("display product method...")
#     shop_id = request.session.get('shop_id')
#     print(shop_id)
    
#     if request.method == 'POST':
#         # Check if 'selected_category_id' is in POST data, else use session value
#         selected_category_id = request.POST.get('selected_category_id') or request.session.get('selected_category_id')
        
#         # Update session with selected_category_id if it was in the POST data
#         if 'selected_category_id' in request.POST:
#             request.session['selected_category_id'] = request.POST['selected_category_id']
    
#     else:
#         selected_category_id = request.session.get('selected_category_id')
    
#     if not selected_category_id:
#         return redirect('display_categories')
    
#     print(selected_category_id)
#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
    
#     request.session['category_id'] = selected_category_id
    
#     products = Product.objects.filter(shop=shop, category=category)
    
#     return render(request, 'showproductsatuser.html', {'products': products, 'category': category})

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories, Product

# def display_categories(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST.get('shopid')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []

#     elif request.method == 'GET':
#         shop_id = request.GET.get('shopid')
#         category_name = request.GET.get('name')
#         print(shop_id)
#         print(category_name)
#         if shop_id:
#             if not SuperMarket.objects.filter(pk=shop_id).exists():
#                 error_message = "Invalid Shop ID."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             request.session['shop_id'] = shop_id
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             if category_name:
#                 shop_categories = categories.objects.filter(shop=shop, category_name=category_name)
#                 print(shop_categories)
                    
#             else:
#                 shop_categories = categories.objects.filter(shop=shop)

#             return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})
        
#         else:
#             shop_id = request.session.get('shop_id')
#             if not shop_id:
#                 error_message = "Shop ID is required."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             shop_categories = categories.objects.filter(shop=shop)
#             return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})

#     if error_message:
#         return render(request, 'maps.html', {'error_message1': error_message})

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
#     return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories, Product

# def display_categories(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST.get('shopid')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []

#     elif request.method == 'GET':
#         shop_id = request.GET.get('shopid')
#         category_name = request.GET.get('name')
#         if shop_id:
#             if not SuperMarket.objects.filter(pk=shop_id).exists():
#                 error_message = "Invalid Shop ID."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             request.session['shop_id'] = shop_id
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
            
#             if category_name:
#                 shop_categories = categories.objects.filter(shop=shop, category_name=category_name)
#                 if not shop_categories.exists():
#                     error_message = "Category is not in this shop, please speak correct name."
#                     return redirect('smart', error_message=error_message)
                    
#             else:
#                 shop_categories = categories.objects.filter(shop=shop)
#                 if not shop_categories.exists():
#                     error_message = "Category is not in this shop, please speak correct name."
#                     return redirect('smart', error_message=error_message)

#             return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})
        
#         else:
#             shop_id = request.session.get('shop_id')
#             if not shop_id:
#                 error_message = "Shop ID is required."
#                 return render(request, 'maps.html', {'error_message1': error_message})

#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             shop_categories = categories.objects.filter(shop=shop)
#             if not shop_categories.exists():
#                 error_message = "Category is not in this shop, please speak correct name."
#                 return redirect('smart', error_message=error_message)

#             return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})

#     if error_message:
#         return render(request, 'maps.html', {'error_message1': error_message})

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
#     return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})

from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories, Product
from urllib.parse import urlencode

def display_categories(request):
    error_message = None

    if request.method == 'POST':
        shop_id = request.POST.get('shopid')
        if not shop_id:
            error_message = "Shop ID is required."
            # return render(request, 'maps.html', {'error_message1': error_message})
            return redirect('maps')
        
        if not SuperMarket.objects.filter(pk=shop_id).exists():
            # error_message = "Invalid Shop ID."
            # return render(request, 'maps.html', {'error_message1': error_message})
            return redirect('maps')
        
        request.session['shop_id'] = shop_id
        request.session['selected_products'] = []

    elif request.method == 'GET':
        shop_id = request.GET.get('shopid')
        category_name = request.GET.get('name')
        if shop_id:
            if not SuperMarket.objects.filter(pk=shop_id).exists():
                error_message = "Invalid Shop ID."
                # return render(request, 'maps.html', {'error_message1': error_message})
                return redirect('maps')

            request.session['shop_id'] = shop_id
            shop = get_object_or_404(SuperMarket, pk=shop_id)
            
            if category_name:
                shop_categories = categories.objects.filter(shop=shop, category_name=category_name)
                if not shop_categories.exists():
                    error_message = "Category is not in this shop, please speak correct name."
                    query_params = urlencode({'error_message': error_message})
                    return redirect(f'/smart/?{query_params}')
                    
            else:
                shop_categories = categories.objects.filter(shop=shop)
                if not shop_categories.exists():
                    error_message = "Category is not in this shop, please speak correct name."
                    query_params = urlencode({'error_message': error_message})
                    return redirect(f'/smart/?{query_params}')

            return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})
        
        else:
            shop_id = request.session.get('shop_id')
            if not shop_id:
                error_message = "Shop ID is required."
                # return render(request, 'maps.html', {'error_message1': error_message})
                return redirect('maps')

            shop = get_object_or_404(SuperMarket, pk=shop_id)
            shop_categories = categories.objects.filter(shop=shop)
            if not shop_categories.exists():
                error_message = "Category is not in this shop, please speak correct name."
                query_params = urlencode({'error_message': error_message})
                return redirect(f'/smart/?{query_params}')

            return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})

    if error_message:
        # return render(request, 'maps.html', {'error_message1': error_message})
        return redirect('maps')

    shop = get_object_or_404(SuperMarket, pk=shop_id)
    shop_categories = categories.objects.filter(shop=shop)
    return render(request, 'shopcatalog.html', {'categories': shop_categories, 'shop': shop})


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories, Product

# def display_products(request):
#     shop_id = request.session.get('shop_id')

#     if not shop_id:
#         return redirect('display_categories')

#     selected_category_id = None

#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category_id') or request.session.get('selected_category_id')
#         if selected_category_id:
#             request.session['selected_category_id'] = selected_category_id
    
#     else:
#         product_name = request.GET.get('name')
#         if product_name:
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             products = Product.objects.filter(shop=shop, product_name=product_name)
#             print(products)
#             if products.exists():
#                 selected_category_id = products.first().category_id
#                 request.session['selected_category_id'] = selected_category_id
#             else:
#                 return render(request, 'showproductsatuser.html', {'products': [], 'error_message': 'No such product found'})
#         else:
#             selected_category_id = request.session.get('selected_category_id')

#     if not selected_category_id:
#         return redirect('display_categories')

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     category = get_object_or_404(categories, pk=selected_category_id, shop=shop)

#     request.session['category_id'] = selected_category_id

#     products = Product.objects.filter(shop=shop, category=category)

#     return render(request, 'showproductsatuser.html', {'products': products, 'category': category})


from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories, Product

# def display_products(request):
#     shop_id = request.session.get('shop_id')

#     if not shop_id:
#         return redirect('display_categories')

#     selected_category_id = None

#     if request.method == 'POST':
#         selected_category_id = request.POST.get('selected_category_id') or request.session.get('selected_category_id')
#         if selected_category_id:
#             request.session['selected_category_id'] = selected_category_id
    
#     else:
#         product_name = request.GET.get('name')
#         if product_name:
#             shop = get_object_or_404(SuperMarket, pk=shop_id)
#             products = Product.objects.filter(shop=shop, product_name=product_name)
#             print(products)
#             if products.exists():
#                 selected_category_id = products.first().category_id
#                 request.session['selected_category_id'] = selected_category_id
#             else:
#                 return render(request, 'index.html',{ 'error_message': 'No such product found'})
#         else:
#             selected_category_id = request.session.get('selected_category_id')

#     if not selected_category_id:
#         return redirect('display_categories')

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     category = get_object_or_404(categories, pk=selected_category_id, shop=shop)

#     request.session['category_id'] = selected_category_id

#     products = Product.objects.filter(shop=shop, category=category, product_staus=1)

#     return render(request, 'showproductsatuser.html', {'products': products, 'category': category})

from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories, Product

def display_products(request):
    shop_id = request.session.get('shop_id')

    if not shop_id:
        return redirect('display_categories')

    selected_category_id = None

    if request.method == 'POST':
        selected_category_id = request.POST.get('selected_category_id') or request.session.get('selected_category_id')
        if selected_category_id:
            request.session['selected_category_id'] = selected_category_id
    else:
        product_name = request.GET.get('name')
        if product_name:
            shop = get_object_or_404(SuperMarket, pk=shop_id)
            products = Product.objects.filter(shop=shop, product_name=product_name)
            if products.exists():
                selected_category_id = products.first().category_id
                request.session['selected_category_id'] = selected_category_id
            else:
                return render(request, 'index.html', {'error_message': 'No such product found'})
        else:
            selected_category_id = request.session.get('selected_category_id')

    if not selected_category_id:
        return redirect('display_categories')

    shop = get_object_or_404(SuperMarket, pk=shop_id)
    category = get_object_or_404(categories, pk=selected_category_id, shop=shop)

    request.session['category_id'] = selected_category_id

    products = Product.objects.filter(shop=shop, category=category, product_staus=1)

    return render(request, 'showproductsatuser.html', {'products': products, 'category': category})


from django.shortcuts import render, get_object_or_404
from .models import SuperMarket,categories # Updated import for Category model

# def display_categoriesshopowner(request):
#     # error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST['shopid']
#         request.session['shop_id'] = shop_id
#         if not shop_id:
            
#     #     if not shop_id:
#     #         error_message = "Shop ID is required."
#     #         return render(request, 'maps.html', {'error_message1': error_message})
        
#     #     if not SuperMarket.objects.filter(pk=shop_id).exists():
#     #         error_message = "Invalid Shop ID."
#     #         return render(request, 'maps.html', {'error_message1': error_message})
        
#     #     request.session['shop_id'] = shop_id
#     #     request.session['selected_products'] = []
#     # else:
    
#             shop_id = request.session.get('shop_id')
#     # print(shop_id)
#     # if not shop_id:
#     #     error_message = "Shop ID is required."
#     #     return render(request, 'maps.html', {'error_message1': error_message})

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
#     print(shop_categories)
    
#     return render(request, 'shopcatalogshopowner.html', {'categories': shop_categories})


from django.shortcuts import render, get_object_or_404
from .models import SuperMarket, categories

def display_categoriesshopowner(request):
    if request.method == 'POST':
        shop_id = request.POST['shopid']
        if shop_id:
            request.session['shop_id'] = shop_id
        else:
            shop_id = request.session.get('shop_id')
    else:
        shop_id = request.session.get('shop_id')

    # if not shop_id:
    #     error_message = "Shop ID is required."
    #     return render(request, 'maps.html', {'error_message1': error_message})

    shop = get_object_or_404(SuperMarket, pk=shop_id)
    shop_categories = categories.objects.filter(shop=shop)
    
    return render(request, 'shopcatalogshopowner.html', {'categories': shop_categories})




# from django.shortcuts import render, get_object_or_404
# from .models import SuperMarket,categories # Updated import for Category model

# def display_categoriesatshopowner(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST['shopid']
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid Shop ID."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         request.session['shop_id'] = shop_id
#         request.session['selected_products'] = []
#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})

#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     shop_categories = categories.objects.filter(shop=shop)
    
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})


# from django.shortcuts import render, get_object_or_404
# from .models import SuperMarket, categories, Product

# def display_categories(request):
#     error_message = None

#     if request.method == 'POST':
#         shop_id = request.POST.get('shopid')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         if not SuperMarket.objects.filter(pk=shop_id).exists():
#             error_message = "Invalid shop_id."
#             return render(request, 'maps.html', {'error_message1': error_message})
        
#         # Store the valid shop_id in the session
#         request.session['shop_id'] = shop_id
#         if 'selected_products' not in request.session:
#             request.session['selected_products'] = []

#     else:
#         shop_id = request.session.get('shop_id')
#         if not shop_id:
#             error_message = "Shop ID is required."
#             return render(request, 'maps.html', {'error_message1': error_message})
    
#     # Fetch the categories associated with the shop_id
#     shop_categories = categories.objects.filter(shop_id=shop_id)
#     return render(request, 'shopcatalog.html', {'categories': shop_categories})


def backdisplay_categories(request):
    # error_message = None
    # shop_id = request.POST['shopid']
    # request.session['shop_id'] = shop_id
    # Get shop_id from POST data
    # request.session['shop_id'] = shop_id
    shop_id = request.session.get('shop_id')
    # if not shop_id or not SuperMarket.objects.filter(pk=shop_id).exists():
    #     error_message = "Invalid shop_id."
    #     return render(request, 'maps.html', {'error_message1': error_message})
    
    # Fetch all categories associated with the shop
    shop_categories = categories.objects.filter(shop_id=shop_id)
    
    # Pass the categories to the template for rendering
    return render(request, 'shopcatalog.html', {'categories': shop_categories})




# def userselect_category(request):
#     shop_id = request.session.get('shop_id')
#     shop = get_object_or_404(SuperMarket, pk=shop_id)
#     category_list = categories.objects.filter(shop=shop)
    
#     return render(request, 'showproductsatuser.html', {'categories': category_list})



# def display_products(request):
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         print(shop_id)
#         # if not shop_id:
#         #     return redirect('set_shop_id')
        
#         selected_category_id = request.POST['selected_category_id']
        
#         print(selected_category_id)
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         request.session['category_id'] = selected_category_id
        
#         products = Product.objects.filter(shop=shop, category=category)
        
#         return render(request, 'showproductsatuser.html', {'products': products, 'category': category})
    
#     return redirect('display_categories')


# def display_products(request):
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         print("Shop ID from session:", shop_id)
        
#         # Print the entire POST data for debugging
#         print("POST data:", request.POST)
        
#         selected_category_id = request.POST['selected_category_id']
#         if not selected_category_id:
#             return redirect('select_category')
        
#         print("Selected category ID:", selected_category_id)
        
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         request.session['category_id'] = selected_category_id
        
#         products = Product.objects.filter(shop=shop, category=category)
        
#         return render(request, 'showproductsatuser.html', {'products': products, 'category': category})
    
#     return redirect('select_category')


from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperMarket, categories, Product

# def display_products(request):
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         selected_category_id = request.POST['selected_category_id']
#         if not selected_category_id:
#             selected_category_id=request.session.get('selected_category_id')
#         else:
#             request.session['selected_category_id'] = selected_category_id
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         request.session['category_id'] = selected_category_id
       
#         products = Product.objects.filter(shop=shop, category=category)
        
#         return render(request, 'showproductsatuser.html', {'products': products, 'category': category})
    
#     # return redirect('backdisplay_categories')
#     return redirect('display_categories')


# working code for display products after clicking add_to_list
# def display_products(request):
#     print("disply product method...")
#     if request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         print(shop_id)
#         # Check if 'selected_category_id' is in POST data, else use session value
#         selected_category_id = request.POST['selected_category_id'] or request.session.get('selected_category_id')
        
#         # Update session with selected_category_id if it was in the POST data
#         if 'selected_category_id' in request.POST:
#             request.session['selected_category_id'] = request.POST['selected_category_id']
        
#         print(selected_category_id)
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         request.session['category_id'] = selected_category_id
        
#         products = Product.objects.filter(shop=shop, category=category)
        
#         return render(request, 'showproductsatuser.html', {'products': products, 'category': category})
#     elif not request.method == 'POST':
#         shop_id = request.session.get('shop_id')
#         print(shop_id)
#         # Check if 'selected_category_id' is in POST data, else use session value
#         selected_category_id =request.session.get('selected_category_id')
        
#         # Update session with selected_category_id if it was in the POST data
#         # if 'selected_category_id' in request.POST:
#         #     request.session['selected_category_id'] = request.POST['selected_category_id']
        
#         print(selected_category_id)
#         shop = get_object_or_404(SuperMarket, pk=shop_id)
#         category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
        
#         request.session['category_id'] = selected_category_id
        
#         products = Product.objects.filter(shop=shop, category=category)
        
#         return render(request, 'showproductsatuser.html', {'products': products, 'category': category})
#     return redirect('display_categories')



from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, categories, Product

def display_productsatshopowner(request):
    print("display product method...")
    shop_id = request.session.get('shop_id')
    print(shop_id)
    
    if not shop_id:
        return redirect('shop_selection_view')  # Ensure you have a view for selecting the shop
    
    if request.method == 'POST' and 'selected_category_id' in request.POST:
        selected_category_id = request.POST['selected_category_id']
        request.session['selected_category_id'] = selected_category_id
    else:
        selected_category_id = request.session.get('selected_category_id')
    
    if not selected_category_id:
        return redirect('display_categories')
    
    print(selected_category_id)
    shop = get_object_or_404(SuperMarket, pk=shop_id)
    category = get_object_or_404(categories, pk=selected_category_id, shop=shop)
    
    products = Product.objects.filter(shop=shop, category=category)
    
    if request.method == 'POST' and 'add_product' in request.POST:
        product_name = request.POST.get('name')
        # product_description = request.POST.get('description')
        product_price = request.POST.get('price')
        # product_image = request.FILES.get('image')
        
        new_product = Product(
            name=product_name,
            # description=product_description,
            price=product_price,
            # image=product_image,
            shop=shop,
            category=category
        )
        new_product.save()
        return redirect(request.path_info)  # Refresh the page to show the new product
    
    return render(request, 'showproductsatshopowner.html', {'products': products, 'category': category})


# def add_to_list(request):
#     # total_price=0
#     if request.method == 'POST':
#         product_id = request.POST['product_id']
#         product = get_object_or_404(Product, pk=product_id)
        
#         selected_products = request.session.get('selected_products', [])
#         selected_products.append({
#             'product_id': product.product_id,
#             'product_name': product.product_name,
#             'product_price': product.product_price
#         })
#         # total_price+=product.product_price
#         # print(total_price)
#         request.session['selected_products'] = selected_products
#         print(selected_products)
#         print("*********************")
#         return redirect('display_products', )
#         # return render(request, 'showproductsatuser.html')
#     print("-------------------")
#     return redirect('display_categories')


# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import SuperMarket, categories, Product

# def add_to_list(request):
#     if request.method == 'POST':
#         product_id = request.POST['product_id']
#         selected_category_id = request.POST['selected_category_id']
        
#         product = get_object_or_404(Product, pk=product_id)
        
#         selected_products = request.session.get('selected_products', [])
#         found = False
        
#         for item in selected_products:
#             if item['product_id'] == product_id:
#                 item['quantity'] += 1
#                 found = True
#                 break
        
#         if not found:
#             selected_products.append({
#                 'product_id': product.product_id,
#                 'product_name': product.product_name,
#                 'product_price': product.product_price,
#                 'quantity': 1,
#             })
        
#         request.session['selected_products'] = selected_products
        
#     return redirect('display_categories')


# views.py

from django.shortcuts import render, redirect
from .models import Product

# def add_to_list(request):
#     if request.method == 'POST':
#         selected_category_id = request.POST['selected_category_id']
#         selected_products = request.session.get('selected_products', [])
        
#         for product in Product.objects.filter(pk__in=request.POST.getlist('product_id')):
#             quantity = int(request.POST.get(f'quantity_{product.pk}', 1))
#             product_dict = {
#                 'product_id': product.pk,
#                 'product_name': product.product_name,
#                 'product_price': float(product.product_price),
#                 'quantity': quantity
#             }
            
#             selected_products.append(product_dict)
        
#         request.session['selected_products'] = selected_products
    
#     return redirect('display_products')


def add_to_list(request):
    if request.method == 'POST':
        selected_category_id = request.POST.get('selected_category_id')
        product_id = request.POST.get('product_id')
        
        product = get_object_or_404(Product, pk=product_id)
        
        selected_products = request.session.get('selected_products', [])
        
        # Check if the product is already in the session
        product_in_list = False
        for item in selected_products:
            if item['product_id'] == product_id:
                item['quantity'] += 1
                product_in_list = True
                break
        
        if not product_in_list:
            selected_products.append({
                'product_id': product_id,
                'product_name': product.product_name,
                'product_price': product.product_price,
                'quantity': 1
            })
        
        request.session['selected_products'] = selected_products
        return redirect('display_products')


# def display_selected_products(request):
#     selected_products = request.session.get('selected_products', [])
#     # total_price += product['product_price']
#     total_price = 0
    
#     for product in selected_products:
#         total_price += product['product_price']
        
#     print(total_price)
#     # return render(request, 'selected_products.html', {'selected_products': selected_products})
#     return render(request, 'selected_products.html', {
#         'selected_products': selected_products,
#         'total_price': total_price
#     })

# def display_selected_products(request):
#     selected_products = request.session.get('selected_products', [])
#     shop_id=request.session.get('shop_id')
#     shop = get_object_or_404(SuperMarket, s_id=shop_id)
#     user_id=request.session.get('user_id')
#     user= get_object_or_404(mainuser, user_id=user_id)
#     total_price = sum(product['product_price'] * product['quantity'] for product in selected_products)
#     return render(request, 'selected_products.html', {'selected_products': selected_products, 'total_price': total_price, 'shop':shop , 'user':user})

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, mainuser, Product, Order, OrderItem

# def display_selected_products(request):
#     selected_products = request.session.get('selected_products', [])

#     shop_id = request.session.get('shop_id')
#     shop = get_object_or_404(SuperMarket, s_id=shop_id)
#     user_id = request.session.get('user_id')
#     user = get_object_or_404(mainuser, user_id=user_id)
#     total_price = sum(product['product_price'] * product['quantity'] for product in selected_products)
    
#     return render(request, 'selected_products.html', {
#         'selected_products': selected_products, 
#         'total_price': total_price, 
#         'shop': shop, 
#         'user': user
#     })

from django.shortcuts import render, get_object_or_404, redirect
from .models import SuperMarket, mainuser, Product, Order, OrderItem

def display_selected_products(request):
    selected_products = request.session.get('selected_products', [])
    
    if not selected_products:
        return render(request, 'selected_products.html', {'no_products': True})

    shop_id = request.session.get('shop_id')
    shop = get_object_or_404(SuperMarket, s_id=shop_id)
    user_id = request.session.get('user_id')
    user = get_object_or_404(mainuser, user_id=user_id)
    total_price = sum(product['product_price'] * product['quantity'] for product in selected_products)
    
    return render(request, 'selected_products.html', {
        'selected_products': selected_products, 
        'total_price': total_price, 
        'shop': shop, 
        'user': user,
        'no_products': False
    })


def create_order(request):
    print("1111111")
    if request.method == 'POST':
        selected_products = request.session.get('selected_products', [])
        shop_id = request.session.get('shop_id')
        user_id = request.session.get('user_id')
        # request.session['order_id'] = order.pk
        
        # request.session['user_id'] = request.user.id
        shop = get_object_or_404(SuperMarket, s_id=shop_id)
        user = get_object_or_404(mainuser, user_id=user_id)
        shop_owner = shop.owner
        print("hello......")
        # Create the order
        total_price = sum(product['product_price'] * product['quantity'] for product in selected_products)
        order = Order.objects.create(
            user=user,
            shop_owner=shop_owner,
            supermarket=shop,
            total_price=total_price
        )
        shopmail=shop.s_mail
        usermail=user.user_mail
        print(shopmail)
        
        request.session['amount'] = total_price
        request.session['order_id']=order.order_id
        request.session['user_mail']=user.user_mail
        print( request.session['user_mail'])
        order_id=request.session.get('order_id')
        print(order_id)
        # Create order items
        for item in selected_products:
            product = get_object_or_404(Product, product_id=item['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price=product.product_price * item['quantity']
            )
        
        # Clear the session
        request.session['selected_products'] = []
        # oid=order_id
        # return redirect('order_success', order_id=order.order_id ) *********************
        # return redirect('orderplace', )
        request.session['shopmail'] = shopmail
        request.session['usermail'] = usermail
        # return render(request, 'typesofpayments.html')   ********
        return render(request, 'orderplace.html', {'shopmail': shopmail, 'usermail':user.user_mail})
        # return redirect('')
    
    return redirect('display_selected_products')

# from django.shortcuts import render,redirect
# from sm_app.models import mainuser,Product,Order,Payment
# from django.contrib import messages
# from math import ceil
# from sm_app import keys
# from django.conf import settings
# MERCHANT_KEY=keys.MK
# import json
# from django.views.decorators.csrf import  csrf_exempt
# from PayTm import Checksum

# def checkout(request):
#     if request.method=="POST":
#         thank = True
# # # PAYMENT INTEGRATION
#         order_id = request.session.get('order_id')
#         amount = request.session.get('amount')
#         customer_id = request.session.get('user_id')

#         order = get_object_or_404(Order, pk=order_id)


#         id = order_id
#         oid=str(id)
#         param_dict = {

#             'MID':keys.MID,
#             'ORDER_ID': oid,
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': str(customer_id),
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

#         }
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         print("*************")
#         print(param_dict)
#         return render(request, 'paytm.html', {'param_dict': param_dict})
#     return render(request, 'home.html')


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]
#     print(response_dict)
#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#             a=response_dict['ORDERID']
#             b=response_dict['TXNAMOUNT']
#             rid=a
           
#             print(rid)
#             filter2= Order.objects.filter(order_id=rid)
#             print(filter2)
#             print(a,b)
#             for post1 in filter2:

#                 post1.oid=a
#                 post1.amountpaid=b
#                 post1.paymentstatus="PAID"
#                 post1.save()
#             print("run agede function")
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'paymentstatus.html', {'response': response_dict})

from django.shortcuts import render, redirect, get_object_or_404
from sm_app.models import mainuser, Product, Order, Payment
from django.contrib import messages
from sm_app import keys
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum
import json
from django.views.decorators.csrf import  csrf_exempt
# from PayTm import Checksum
# 
MERCHANT_KEY = keys.MK

# def checkout(request):
#     if request.method == "POST":
#         # Retrieve necessary session data
#         order_id = request.session.get('order_id')
#         amount = request.session.get('amount')
#         customer_id = request.session.get('user_id')

#         # Fetch the order object
#         order = get_object_or_404(Order, pk=order_id)

#         param_dict = {
#             'MID': keys.MID,
#             'ORDER_ID': str(order_id),
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': str(customer_id),
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
#         }

#         # Generate checksum
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

#         return render(request, 'paytm.html', {'param_dict': param_dict})
    
#     return render(request, 'home.html')


# # @csrf_exempt
# def handlerequest(request):
#     if request.method == 'POST':
#         response_dict = {}
#         form = request.POST

#         # Collect POST data and extract checksum
#         for key in form.keys():
#             response_dict[key] = form[key]
#             if key == 'CHECKSUMHASH':
#                 checksum = form[key]

#         # Verify checksum
#         verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)

#         if verify:
#             if response_dict['RESPCODE'] == '01':
#                 # Order was successful
#                 order_id = response_dict['ORDERID']
#                 txn_amount = response_dict['TXNAMOUNT']

#                 # Update order status
#                 order = get_object_or_404(Order, pk=order_id)
#                 order.oid = order_id
#                 order.amountpaid = txn_amount
#                 order.paymentstatus = "PAID"
#                 order.save()

#                 print("Order successful")
#             else:
#                 print('Order was not successful because ' + response_dict['RESPMSG'])
        
#         return render(request, 'paymentstatus.html', {'response': response_dict})

#     return redirect('home')


# @csrf_exempt
# def handlerequest(request):
#     if request.method == 'POST':
#         response_dict = {}
#         form = request.POST

#         # Collect POST data
#         for key in form.keys():
#             response_dict[key] = form[key]

#         # Set a default value for checksum
#         checksum = None

#         # Extract checksum if present
#         if 'CHECKSUMHASH' in response_dict:
#             checksum = response_dict['CHECKSUMHASH']

#         # Verify checksum if present
#         if checksum:
#             verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
            
#             if verify:
                
#                 if response_dict['RESPCODE'] == '01':
#                     print('order successful')
#                     a=response_dict['ORDERID']
#                     b=response_dict['TXNAMOUNT']
#                     rid=a
           
#                     print(rid)
#                     filter2= Order.objects.filter(order_id=rid)
#                     print(filter2)
#                     print(a,b)
#                     for post1 in filter2:

#                         post1.oid=a
#                         post1.amountpaid=b
#                         post1.paymentstatus="PAID"
#                         post1.save()
#                     print("run agede function")
#                 else:
#                     print('order was not successful because' + response_dict['RESPMSG'])
#             return render(request, 'paymentstatus.html', {'response': response_dict})

#     #         if verify:
#     #             if response_dict['RESPCODE'] == '01':
#     #                 # Order was successful
#     #                 order_id = response_dict['ORDERID']
#     #                 txn_amount = response_dict['TXNAMOUNT']

#     #                 # Update order status
#     #                 order = get_object_or_404(Order, pk=order_id)
#     #                 order.oid = order_id
#     #                 order.amountpaid = txn_amount
#     #                 order.paymentstatus = "PAID"
#     #                 order.save()

#     #                 print("Order successful")
#     #             else:
#     #                 print('Order was not successful because ' + response_dict['RESPMSG'])

#     #     return render(request, 'paymentstatus.html', {'response': response_dict})

#     # return redirect('home')

# @csrf_exempt
# def handlerequest(request):
#     if request.method == 'POST':
#         response_dict = {}
#         form = request.POST

#         # Collect POST data
#         for key in form.keys():
#             response_dict[key] = form[key]

#         # Set a default value for checksum
#         checksum = None

#         # Extract checksum if present
#         if 'CHECKSUMHASH' in response_dict:
#             checksum = response_dict['CHECKSUMHASH']

#         # Verify checksum if present
#         if checksum:
#             verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
            
#             if verify:
#                 if response_dict['RESPCODE'] == '01':
#                     print('order successful')
#                     a = response_dict['ORDERID']
#                     b = response_dict['TXNAMOUNT']
#                     rid = a
           
#                     print(rid)
#                     filter2 = Order.objects.filter(order_id=rid)
#                     print(filter2)
#                     print(a, b)
#                     for post1 in filter2:
#                         post1.oid = a
#                         post1.amountpaid = b
#                         post1.paymentstatus = "PAID"
#                         post1.save()
#                     print("run agede function")
#                 else:
#                     print('order was not successful because ' + response_dict['RESPMSG'])
                    
#         return render(request, 'paymentstatus.html', {'response': response_dict})

#     return redirect('home')


# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages
# from .models import Order, OrderUpdate
# # import Checksum
# from PayTm import Checksum
# from django.conf import settings

# def checkout(request):
#     if request.method == "POST":
#         # items_json = request.POST.get('itemsJson', '')
#         # name = request.POST.get('name', '')
#         # amount = request.POST.get('amt')
#         # email = request.POST.get('email', '')
#         # address1 = request.POST.get('address1', '')
#         # address2 = request.POST.get('address2', '')
#         # city = request.POST.get('city', '')
#         # state = request.POST.get('state', '')
#         # zip_code = request.POST.get('zip_code', '')
#         # phone = request.POST.get('phone', '')
        
#         # Create order in database
#         # order = Order.objects.create(
#         #     # items_json=items_json,
#         #     # name=name,
#         #     # amount=amount,
#         #     # email=email,
#         #     # address1=address1,
#         #     # address2=address2,
#         #     # city=city,
#         #     # state=state,
#         #     # zip_code=zip_code,
#         #     # phone=phone,
#         #     payment_status="PENDING"  # Initial payment status
#         # )
        
#         # Store order ID in session
#         # request.session['order_id'] = Order.order_id
#         amount = request.session.get('amount')
#         customer_id = request.session.get('user_id')
#         order_id=request.session.get('order_id')
# #         # Fetch the order object
#         order = get_object_or_404(Order, pk=order_id)

#         # Prepare parameters for Paytm payment
#         oid = str(order.order_id) + "ShopyCart"
#         param_dict = {
#             'MID':keys.MID, #settings.PAYTM_MERCHANT_ID,
#             'ORDER_ID': oid,
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': str(customer_id),
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING' ,#settings.PAYTM_WEBSITE,
#             'CHANNEL_ID': 'WEB', #,settings.PAYTM_CHANNEL_ID,
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',#settings.PAYTM_CALLBACK_URL,
#         }
        
#         # Generate checksum hash
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, settings.PAYTM_MERCHANT_KEY)
        
#         return render(request, 'paytm.html', {'param_dict': param_dict})
    
#     return render(request, 'checkout.html')

# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages
# from .models import Payment, Order

# @csrf_exempt
# def handlerequest(request):
#     # Verify if the request is POST
#     if request.method == 'POST':
#         # Extract response data from POST request
#         form = request.POST
#         response_dict = {}
#         for key in form.keys():
#             response_dict[key] = form[key]
#             if key == 'CHECKSUMHASH':
#                 checksum = form[key]
        
#         # Verify checksum
#         verify = Checksum.verify_checksum(response_dict, settings.PAYTM_MERCHANT_KEY, checksum)
        
#         if verify:
#             # Payment successful
#             if response_dict['RESPCODE'] == '01':
#                 order_id = response_dict['ORDERID']
#                 amount_paid = response_dict['TXNAMOUNT']
                
#                 # Update payment status in Payment model
#                 try:
#                     payment = Payment.objects.get(order_id=order_id)
#                     payment.payment_status = "PAID"
#                     payment.save()
                    
#                     # Update order payment status in Order model
#                     order = Order.objects.get(order_id=order_id)
#                     order.update_payment_status("PAID")
                    
#                     # Create order update
#                     OrderUpdate.objects.create(
#                         order_id=order.order_id,
#                         update_desc="The order has been paid."
#                     )
                    
#                     messages.success(request, 'Your order was successfully paid!')
                    
#                 except Payment.DoesNotExist:
#                     messages.error(request, 'Payment does not exist.')
                    
#                 except Order.DoesNotExist:
#                     messages.error(request, 'Order does not exist.')
                    
#             else:
#                 # Payment failed
#                 messages.error(request, 'Payment was not successful.')
        
#         else:
#             # Checksum verification failed
#             messages.error(request, 'Checksum verification failed.')
    
#     return render(request, 'paymentstatus.html')

# @csrf_exempt
# def handlerequest(request):
#     # Verify if the request is POST
#     if request.method == 'POST':
#         # Extract response data from POST request
#         form = request.POST
#         response_dict = {}
#         for key in form.keys():
#             response_dict[key] = form[key]
#             if key == 'CHECKSUMHASH':
#                 checksum = form[key]
        
#         # Verify checksum
#         verify = Checksum.verify_checksum(response_dict, settings.PAYTM_MERCHANT_KEY, checksum)
        
#         if verify:
#             # Payment successful
#             if response_dict['RESPCODE'] == '01':
#                 order_id = response_dict['ORDERID']
#                 amount_paid = response_dict['TXNAMOUNT']
                
#                 # Update order in database
#                 try:
#                     order = Order.objects.get(order_id=order_id)
#                     order.payment_status = "PAID"
#                     order.amount_paid = amount_paid
#                     order.save()
                    
#                     # Create order update
#                     OrderUpdate.objects.create(
#                         order_id=order.order_id,
#                         update_desc="The order has been placed."
#                     )
                    
#                     messages.success(request, 'Your order was successful!')
                    
#                 except Orders.DoesNotExist:
#                     messages.error(request, 'Order does not exist.')
                    
#             else:
#                 # Payment failed
#                 messages.error(request, 'Payment was not successful.')
        
#         else:
#             # Checksum verification failed
#             messages.error(request, 'Checksum verification failed.')
    
#     return render(request, 'paymentstatus.html')


# views.py

# from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages
# from .models import Order, OrderItem, Payment
# from PayTm import Checksum
# from django.conf import settings
# import uuid

# def checkout(request):
#     if not request.user.is_authenticated:
#         messages.warning(request, "Login & Try Again")
#         return redirect('/auth/login')

#     if request.method == "POST":
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amt')
#         email = request.POST.get('email', '')
#         address1 = request.POST.get('address1', '')
#         address2 = request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
        
#         # Create Order
#         order = Order.objects.create(
#             user=request.user,
#             shop_owner=request.user.shopowner,  # Assuming user has a shopowner attribute
#             supermarket=request.user.shopowner.supermarket,  # Assuming shopowner has a supermarket attribute
#             total_price=float(amount),
#         )
        
#         # Create Order Items
#         for item in items_json:
#             product_id = item['product_id']
#             quantity = item['quantity']
#             product = Product.objects.get(pk=product_id)
#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 quantity=quantity,
#                 price=product.product_price  # Assuming this is the price of the product
#             )
        
#         param_dict = {
#             'MID': settings.PAYTM_MERCHANT_ID,
#             'ORDER_ID': str(order.order_id) + str(uuid.uuid4().hex.upper()[0:6]),
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': email,
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/payment/callback/',
#         }

#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, settings.PAYTM_MERCHANT_KEY)
        
#         return render(request, 'paytm.html', {'param_dict': param_dict})
    
#     return render(request, 'checkout.html')


# @csrf_exempt
# def handlerequest(request):
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]
    
#     verify = Checksum.verify_checksum(response_dict, settings.PAYTM_MERCHANT_KEY, checksum)
    
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             order_id = response_dict['ORDERID']
#             amount = response_dict['TXNAMOUNT']
            
#             try:
#                 order = Order.objects.get(order_id=order_id)
                
#                 # Create Payment
#                 payment = Payment.objects.create(
#                     order=order,
#                     payment_method='Paytm',
#                     amount=float(amount),
#                     payment_status='SUCCESS'
#                 )
                
#                 # Update order payment status
#                 order.update_payment_status('PAID')
                
#                 messages.success(request, 'Your payment was successful!')
            
#             except Order.DoesNotExist:
#                 messages.error(request, 'Order does not exist.')
            
#         else:
#             messages.error(request, 'Payment was not successful.')
    
#     else:
#         messages.error(request, 'Checksum verification failed.')

#     return render(request, 'paymentstatus.html', {'response': response_dict})
# import razorpay
# from django.conf import settings
# razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))

# from .models import Order, Payment,mainuser
# from django.shortcuts import render, HttpResponse, redirect
# from django.http import JsonResponse
# # from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
# from django.core.exceptions import ValidationError
# # from .forms import ContactUsForm, RegistrationFormSeller, RegistrationForm, RegistrationFormSeller2, CartForm
# from django.urls import reverse_lazy, reverse
# from .models import SellerAdditional, CustomUser, Contact, Product, ProductInCart, Cart
# # from django.contrib.auth.views import LoginView, LogoutView
# # from django.contrib.auth.mixins import LoginRequiredMixin



# from django.core.mail import EmailMessage
# # from .tokens import account_activation_token
# from django.core.mail import send_mail
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt


# def payment(request):
#     if request.method == "POST":
#         # try:
#         #     cart = Cart.objects.get(user = request.user)
#         #     products_in_cart = ProductInCart.objects.filter(cart = cart)
#         # final_price = 0
#         #     if(len(products_in_cart)>0):
#         #         order = Order.objects.create(user = request.user, total_amount = 0)
#         #         # order.save()
#         #         for product in products_in_cart:
#         #             product_in_order = ProductInOrder.objects.create(order = order, product = product.product, quantity = product.quantity, price = product.product.price)
#         #             final_price = final_price + (product.product.price * product.quantity)
#         #     else:
#         #         return HttpResponse("No product in cart")
#         # except:
#         #     return HttpResponse("No product in cart")
#         amount = request.session.get('amount')
#         customer_id = request.session.get('user_id')
#         order_id=request.session.get('order_id')
#         # order.total_amount = final_price
#         # order.save()
#         order = get_object_or_404(Order, pk=order_id)
#         order_currency = 'INR'

#         callback_url = 'http://'+ str(get_current_site(request))+"/handlerequest/"
#         print(callback_url)
#         notes = {'order-type': "basic order from the website", 'key':'value'}
#         razorpay_order = razorpay_client.order.create(dict(amount=amount*100, currency=order_currency, notes = notes, receipt=order_id, payment_capture='0'))
#         print(razorpay_order['id'])
#         Payment.razorpay_order_id = razorpay_order['id']
#         Payment.save()
        
#         return render(request, 'firstapp/payment/paymentsummaryrazorpay.html', {'order':order, 'order_id': razorpay_order['id'], 'orderId':order.order_id, 'final_price':amount, 'razorpay_merchant_id':settings.razorpay_id, 'callback_url':callback_url})
#     else:
#         return HttpResponse("505 Not Found") 


# from django.core.mail import EmailMultiAlternatives
# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         try:
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             order_id = request.POST.get('razorpay_order_id','')
#             signature = request.POST.get('razorpay_signature','')
#             params_dict = { 
#             'razorpay_order_id': order_id, 
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#             }
#             try:
#                 order_db = Payment.objects.get(razorpay_order_id=order_id)
#             except:
#                 return HttpResponse("505 Not Found")
#             order_db.razorpay_payment_id = payment_id
#             order_db.razorpay_signature = signature
#             order_db.save()
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result==None:
#                 amount = order_db.amount * 100   #we have to pass in paisa
#                 try:
#                     razorpay_client.payment.capture(payment_id, amount)
#                     order_db.payment_status = 1
#                     order_db.save()

#                     ## For generating Invoice PDF
#                     # template = get_template('firstapp/payment/invoice.html')
#                     data = {
#                         'order_id': order_db.order_id,
#                         'transaction_id': order_db.razorpay_payment_id,
#                         # 'user_email': order_db.user.email,
#                         'date': str(order_db.payment_date),
#                         # 'name': order_db.user.name,
#                         'order': order_db,
#                         'amount': order_db.amount,
#                     }
#                     # html  = template.render(data)
#                     # result = BytesIO()
#                     # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
#                     pdf = result.getvalue()
#                     filename = 'Invoice_' + data['order_id'] + '.pdf'

#                     mail_subject = 'Recent Order Details'
#                     # message = render_to_string('firstapp/payment/emailinvoice.html', {
#                     #     'user': order_db.user,
#                     #     'order': order_db
#                     # })
#                     context_dict = {
#                         'user': order_db.order,
#                         'order': order_db
#                     }
#                     # template = get_template('firstapp/payment/emailinvoice.html')
#                     # message  = template.render(context_dict)
#                     # to_email = order_db.user.email
#                     # email = EmailMessage(
#                     #     mail_subject,
#                     #     message, 
#                     #     settings.EMAIL_HOST_USER,
#                     #     [to_email]
#                     # )

#                     # for including css(only inline css works) in mail and remove autoescape off
#                     # email = EmailMultiAlternatives(
#                     #     mail_subject,
#                     #     "hello",       # necessary to pass some message here
#                     #     settings.EMAIL_HOST_USER,
#                     #     [to_email]
#                     # )
#                     # email.attach_alternative(message, "text/html")
#                     # email.attach(filename, pdf, 'application/pdf')
#                     # email.send(fail_silently=False)

#                     return render(request, 'firstapp/payment/paymentsuccess.html',{'id':order_db.id})
#                 except:
#                     order_db.payment_status = 2
#                     order_db.save()
#                     return render(request, 'firstapp/payment/paymentfailed.html')
#             else:
#                 order_db.payment_status = 2
#                 order_db.save()
#                 return render(request, 'firstapp/payment/paymentfailed.html')
#         except:
#             return HttpResponse("505 not found")


# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.sites.shortcuts import get_current_site
# from .models import Order, Payment

# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID))

# def payment(request):
#     if request.method == "POST":
#         amount = request.session.get('amount')
#         user_id = request.session.get('user_id')
#         order_id = request.session.get('order_id')

#         order = get_object_or_404(Order, pk=order_id)
#         order_currency = 'INR'
#         callback_url = f"http://{get_current_site(request)}/handlerequest/"

#         notes = {'order-type': "basic order from the website", 'key': 'value'}
#         razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100, currency=order_currency, notes=notes, receipt=str(order_id), payment_capture='0'))

#         payment = Payment(order=order, amount=amount, razorpay_order_id=razorpay_order['id'])
#         payment.save()

#         return render(request, 'paymentsummaryrazorpay.html', {
#             'order': order,
#             'order_id': razorpay_order['id'],
#             'orderId': order.order_id,
#             'final_price': amount,
#             'razorpay_merchant_id': settings.RAZORPAY_ID,
#             'callback_url': callback_url
#         })
#     else:
#         return HttpResponse("505 Not Found")

# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         try:
#             order_db = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             return HttpResponse("505 Not Found")

#         order_db.razorpay_payment_id = payment_id
#         order_db.razorpay_signature = signature
#         order_db.save()

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is None:
#                 amount = int(order_db.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 order_db.update_order_payment_status('Completed')
#                 return render(request, 'paymentsuccess.html', {'id': order_db.order.order_id})
#             else:
#                 order_db.update_order_payment_status('Failed')
#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError:
#             order_db.update_order_payment_status('Failed')
#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")

# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.sites.shortcuts import get_current_site
# from .models import Order, Payment

# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID))

# def payment(request):
#     if request.method == "POST":
#         amount = request.session.get('amount')
#         user_id = request.session.get('user_id')
#         order_id = request.session.get('order_id')

#         order = get_object_or_404(Order, pk=order_id)
#         order_currency = 'INR'
#         callback_url = f"http://{get_current_site(request)}/handlerequest/"

#         notes = {'order-type': "basic order from the website", 'key': 'value'}
        
#         # Check if the Payment record already exists
#         payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': amount})

#         if not created:
#             # If the payment already exists, update its amount if needed
#             payment.amount = amount
#             payment.save()
        
#         razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100, currency=order_currency, notes=notes, receipt=str(order_id), payment_capture='0'))
#         payment.razorpay_order_id = razorpay_order['id']
#         payment.save()

#         return render(request, 'paymentsummaryrazorpay.html', {
#             'order': order,
#             'order_id': razorpay_order['id'],
#             'orderId': order.order_id,
#             'final_price': amount,
#             'razorpay_merchant_id': settings.RAZORPAY_ID,
#             'callback_url': callback_url
#         })
#     else:
#         return HttpResponse("505 Not Found")


# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.sites.shortcuts import get_current_site
# from .models import Order, Payment

# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID))

# def payment(request):
#     if request.method == "POST":
#         amount = request.session.get('amount')
#         user_id = request.session.get('user_id')
#         order_id = request.session.get('order_id')

#         order = get_object_or_404(Order, pk=order_id)
#         order_currency = 'INR'
#         callback_url = f"http://{get_current_site(request)}/handlerequest/"

#         notes = {'order-type': "basic order from the website", 'key': 'value'}
        
#         # Check if the Payment record already exists
#         payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': amount})

#         if not created:
#             # If the payment already exists, update its amount if needed
#             payment.amount = amount
#             payment.save()
        
#         razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100, currency=order_currency, notes=notes, receipt=str(order_id), payment_capture='0'))
#         payment.razorpay_order_id = razorpay_order['id']
#         payment.save()

#         return render(request, 'paymentsummaryrazorpay.html', {
#             'order': order,
#             'order_id': razorpay_order['id'],
#             'orderId': order.order_id,
#             'final_price': amount,
#             'razorpay_merchant_id': settings.RAZORPAY_ID,
#             'callback_url': callback_url
#         })
#     else:
#         return HttpResponse("505 Not Found")

# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         try:
#             order_db = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             return HttpResponse("505 Not Found")

#         order_db.razorpay_payment_id = payment_id
#         order_db.razorpay_signature = signature
#         order_db.save()

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is None:
#                 amount = int(order_db.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 order_db.update_order_payment_status('Completed')
#                 return render(request, 'paymentsuccess.html', {'id': order_db.order.order_id})
#             else:
#                 order_db.update_order_payment_status('Failed')
#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError:
#             order_db.update_order_payment_status('Failed')
#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")


# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         try:
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             return HttpResponse("505 Not Found")

#         payment.razorpay_payment_id = payment_id
#         payment.razorpay_signature = signature
#         payment.save()

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is None:
#                 amount = int(payment.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 payment.payment_status = 'Completed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.payment_status = 'Completed'
#                 order.save()

#                 return render(request, 'paymentsuccess.html', {'id': order.order_id})
#             else:
#                 payment.payment_status = 'Failed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.payment_status = 'Failed'
#                 order.save()

#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError:
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.payment_status = 'Failed'
#             order.save()

#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")


from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment, Order
import razorpay

# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         try:
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             return HttpResponse("505 Not Found")

#         payment.razorpay_payment_id = payment_id
#         payment.razorpay_signature = signature
#         payment.save()

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is None:
#                 amount = int(payment.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 payment.payment_status = 'Completed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.payment_status = 'Completed'
#                 order.save()

#                 return render(request, 'paymentsuccess.html', {'id': order.order_id})
#             else:
#                 payment.payment_status = 'Failed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.payment_status = 'Failed'
#                 order.save()

#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError:
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.payment_status = 'Failed'
#             order.save()

#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")



# import razorpay
# from django.conf import settings
# from django.shortcuts import render, get_object_or_404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.sites.shortcuts import get_current_site
# from .models import Order, Payment

# razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID))

# def payment(request):
#     if request.method == "POST":
#         amount = request.session.get('amount')
#         user_id = request.session.get('user_id')
#         order_id = request.session.get('order_id')

#         order = get_object_or_404(Order, pk=order_id)
#         order_currency = 'INR'
#         callback_url = f"http://{get_current_site(request)}/handlerequest/"

#         notes = {'order-type': "basic order from the website", 'key': 'value'}
        
#         # Check if the Payment record already exists
#         payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': amount})

#         if not created:
#             # If the payment already exists, update its amount if needed
#             payment.amount = amount
#             payment.save()
        
#         razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100, currency=order_currency, notes=notes, receipt=str(order_id), payment_capture='0'))
#         payment.razorpay_order_id = razorpay_order['id']
#         payment.save()

#         return render(request, 'paymentsummaryrazorpay.html', {
#             'order': order,
#             'order_id': razorpay_order['id'],
#             'orderId': order.order_id,
#             'final_price': amount,
#             'razorpay_merchant_id': settings.RAZORPAY_ID,
#             'callback_url': callback_url
#         })
#     else:
#         return HttpResponse("505 Not Found")

# @csrf_exempt
# def handlerequest(request):
#     print("11111111111")
#     if request.method == "POST":
#         print("222222")
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }
#         print(params_dict)
#         try:
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             return HttpResponse("505 Not Found")

#         payment.razorpay_payment_id = payment_id
#         payment.razorpay_signature = signature
#         payment.save()
#         print("3333333")
#         print(payment)
#         try:
#             print("try...block")
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is None:
#                 amount = int(payment.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 payment.payment_status = 'Completed'
#                 payment.save()
#                 print("444444444")
#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Completed')

#                 return render(request, 'paymentsuccess.html', {'id': order.order_id})
#             else:
#                 payment.payment_status = 'Failed'
#                 payment.save()
#                 print("555555555")
#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Failed')

#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError:
#             payment.payment_status = 'Failed'
#             payment.save()
#             print("666666666")
#             # Update the associated order's payment status
#             order = payment.order
#             order.update_payment_status('Failed')

#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")



import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site
from .models import Order, Payment

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID))

def payment(request):
    if request.method == "POST":
        amount = request.session.get('amount')
        user_id = request.session.get('user_id')
        order_id = request.session.get('order_id')

        order = get_object_or_404(Order, pk=order_id)
        order_currency = 'INR'
        callback_url = f"http://{get_current_site(request)}/handlerequest/"

        notes = {'order-type': "basic order from the website", 'key': 'value'}
        
        # Check if the Payment record already exists
        payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': amount, 'payment_method': 'Razorpay'})

        if not created:
            # If the payment already exists, update its amount if needed
            payment.amount = amount
            payment.save()
        
        razorpay_order = razorpay_client.order.create(dict(amount=int(amount) * 100, currency=order_currency, notes=notes, receipt=str(order_id), payment_capture='0'))
        payment.razorpay_order_id = razorpay_order['id']
        payment.save()

        return render(request, 'paymentsummaryrazorpay.html', {
            'order': order,
            'order_id': razorpay_order['id'],
            'orderId': order.order_id,
            'final_price': amount,
            'razorpay_merchant_id': settings.RAZORPAY_ID,
            'callback_url': callback_url
        })
    else:
        return HttpResponse("505 Not Found")

# @csrf_exempt
# def handlerequest(request):
#     print("Handle request received")
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         print(f"params_dict: {params_dict}")

#         try:
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             print("Payment record not found")
#             return HttpResponse("505 Not Found")

#         payment.razorpay_payment_id = payment_id
#         payment.razorpay_signature = signature
#         payment.save()

#         print(f"Payment: {payment}")

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             print(f"Verification result: {result}")
#             if result is True:
#                 amount = int(payment.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 payment.payment_status = 'Completed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Completed')

#                 return render(request, 'paymentsuccess.html', {'id': order.order_id})
#             else:
#                 payment.payment_status = 'Failed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Failed')

#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError as e:
#             print(f"Signature verification error: {str(e)}")
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.update_payment_status('Failed')

#             return render(request, 'paymentfailed.html')
#         except Exception as e:
#             print(f"Unexpected error: {str(e)}")
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.update_payment_status('Failed')

#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sm_app.models import Payment, Order
import razorpay

# razorpay_client = razorpay.Client(auth=(keys.RAZORPAY_KEY_ID, keys.RAZORPAY_SECRET_KEY))

# @csrf_exempt
# def handlerequest(request):
#     print("Handle request received")
#     if request.method == "POST":
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         params_dict = {
#             'razorpay_order_id': order_id,
#             'razorpay_payment_id': payment_id,
#             'razorpay_signature': signature
#         }

#         print(f"params_dict: {params_dict}")

#         try:
#             payment = Payment.objects.get(razorpay_order_id=order_id)
#         except Payment.DoesNotExist:
#             print("Payment record not found")
#             return HttpResponse("505 Not Found")

#         payment.razorpay_payment_id = payment_id
#         payment.razorpay_signature = signature
#         payment.save()

#         print(f"Payment: {payment}")

#         try:
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             print(f"Verification result: {result}")
#             if result:
#                 amount = int(payment.amount) * 100
#                 razorpay_client.payment.capture(payment_id, amount)
#                 payment.payment_status = 'Completed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Completed')

#                 return render(request, 'paymentsuccess.html', {'id': order.order_id})
#             else:
#                 payment.payment_status = 'Failed'
#                 payment.save()

#                 # Update the associated order's payment status
#                 order = payment.order
#                 order.update_payment_status('Failed')

#                 return render(request, 'paymentfailed.html')
#         except razorpay.errors.SignatureVerificationError as e:
#             print(f"Signature verification error: {str(e)}")
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.update_payment_status('Failed')

#             return render(request, 'paymentfailed.html')
#         except Exception as e:
#             print(f"Unexpected error: {str(e)}")
#             payment.payment_status = 'Failed'
#             payment.save()

#             # Update the associated order's payment status
#             order = payment.order
#             order.update_payment_status('Failed')

#             return render(request, 'paymentfailed.html')
#     else:
#         return HttpResponse("505 Not Found")


@csrf_exempt
def handlerequest(request):
    print("Handle request received")
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id', 'dummy_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature', 'dummy_signature')
        # payment_id = request.POST.get('razorpay_payment_id', '')
        # order_id = request.POST.get('razorpay_order_id', '')
        # signature = request.POST.get('razorpay_signature', '')
        print(order_id)
        # Check if order_id is empty
        if not order_id:
            print("Razorpay order ID is missing")
            
            return render(request, 'paymentfailed.html')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        print(f"params_dict: {params_dict}")

        try:
            payment = Payment.objects.get(razorpay_order_id=order_id)
        except Payment.DoesNotExist:
            print("Payment record not found")
            payment.payment_status = 'Failed'
            payment.save()

                # Update the associated order's payment status
            order = payment.order
            order.update_payment_status('Failed')

            return render(request, 'paymentfailed.html')
            # return render(request, 'paymentfailed.html')

        payment.razorpay_payment_id = payment_id
        payment.razorpay_signature = signature
        payment.save()

        print(f"Payment: {payment}")

        try:
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            print(f"Verification result: {result}")
            if result:
                amount = int(payment.amount) * 100
                razorpay_client.payment.capture(payment_id, amount)
                payment.payment_status = 'Completed'
                payment.save()

                # Update the associated order's payment status
                order = payment.order
                order.update_payment_status('Completed')

                return render(request, 'paymentsuccess.html', {'id': order.order_id})
            else:
                payment.payment_status = 'Failed'
                payment.save()

                # Update the associated order's payment status
                order = payment.order
                order.update_payment_status('Failed')

                return render(request, 'paymentfailed.html')
        except razorpay.errors.SignatureVerificationError as e:
            print(f"Signature verification error: {str(e)}")
            payment.payment_status = 'Failed'
            payment.save()

            # Update the associated order's payment status
            order = payment.order
            order.update_payment_status('Failed')

            return render(request, 'paymentfailed.html')
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            payment.payment_status = 'Failed'
            payment.save()

            # Update the associated order's payment status
            order = payment.order
            order.update_payment_status('Failed')

            return render(request, 'paymentfailed.html')
    else:
        return HttpResponse("505 Not Found")

def order_success(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    return render(request, 'order.html', {'order': order, 'order_id':order_id})


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import SuperMarket, categories, Product
# from weasyprint import HTML
# import tempfile
# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     p = canvas.Canvas(response, pagesize=letter)
#     width, height = letter
    
#     y = height - 50
#     p.drawString(100, y, "Invoice")
    
#     y -= 30
#     total_price = 0
#     for product in selected_products:
#         p.drawString(100, y, f"{product['product_name']} - ₹{product['product_price']}")
#         y -= 20
#         total_price += product['product_price']
    
#     y -= 20
#     p.drawString(100, y, f"Total Price: ₹{total_price}")
    
#     p.showPage()
#     p.save()
    
#     return response

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse

# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     p = canvas.Canvas(response, pagesize=letter)
#     width, height = letter
    
#     y = height - 50
#     p.setFont("Helvetica-Bold", 16)
#     p.drawString(100, y, "Invoice")
    
#     y -= 30
#     total_price = 0
    
#     p.setFont("Helvetica", 12)
#     for product in selected_products:
#         p.drawString(100, y, f"{product['product_name']} - ₹{product['product_price']}")
#         y -= 20
#         total_price += product['product_price']
    
#     y -= 20
#     p.drawString(100, y, f"Total Price: ₹{total_price}")
    
#     p.showPage()
#     p.save()
    
#     return response


# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse

# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     # Create a ReportLab canvas
#     p = canvas.Canvas(response, pagesize=letter)
    
#     # Define fonts and styles
#     p.setFont("Helvetica-Bold", 16)
    
#     # Header - Invoice
#     p.drawCentredString(300, 750, "Invoice")
    
#     # Line separator
#     p.line(30, 740, 560, 740)
    
#     # Product table headers
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(50, 720, "Product Name")
#     p.drawString(250, 720, "Price (₹)")
#     p.drawString(400, 720, "Quantity")
#     p.drawString(500, 720, "Subtotal (₹)")
    
#     # Line separator
#     p.line(30, 710, 560, 710)
    
#     # Set initial y position
#     y = 700
#     total_price = 0
    
#     # Products
#     p.setFont("Helvetica", 12)
#     for product in selected_products:
#         product_name = product['product_name']
#         product_price = product['product_price']
#         quantity = product['quantity']
#         subtotal = product_price * quantity
        
#         # Product details
#         p.drawString(50, y, product_name)
#         p.drawString(250, y, f"₹{product_price}")
#         p.drawString(400, y, str(quantity))
#         p.drawString(500, y, f"₹{subtotal}")
        
#         # Update total price
#         total_price += subtotal
        
#         # Move to the next line
#         y -= 20
    
#     # Line separator
#     p.line(30, y, 560, y)
    
#     # Total Price
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(400, y - 20, "Total Price:")
#     p.drawString(500, y - 20, f"₹{total_price}")
    
#     # Save the PDF file
#     p.showPage()
#     p.save()
    
#     return response

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     # Create a ReportLab canvas
#     p = canvas.Canvas(response, pagesize=letter)
    
#     # Set up fonts and styles
#     p.setFont("Helvetica-Bold", 16)
#     p.setStrokeColorRGB(0, 0, 0)
    
#     # Title - Invoice
#     p.drawCentredString(300, 750, "Invoice")
    
#     # Line separator
#     p.line(30, 740, 560, 740)
    
#     # Table headers
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(50, 720, "Product Name")
#     p.drawString(250, 720, "Price (₹)")
#     p.drawString(400, 720, "Quantity")
#     p.drawString(500, 720, "Subtotal (₹)")
    
#     # Line separator
#     p.line(30, 710, 560, 710)
    
#     # Set initial y position for product details
#     y = 700
#     total_price = 0
    
#     # Products
#     p.setFont("Helvetica", 12)
#     for product in selected_products:
#         product_name = product['product_name']
#         product_price = product['product_price']
#         quantity = product['quantity']
#         subtotal = product_price * quantity
        
#         # Product details
#         p.drawString(50, y, product_name)
#         p.drawString(250, y, f"₹ {product_price:.2f}")
#         p.drawString(400, y, str(quantity))
#         p.drawString(500, y, f"₹ {subtotal:.2f}")
        
#         # Update total price
#         total_price += subtotal
        
#         # Move to the next line
#         y -= 20
    
#     # Line separator
#     p.line(30, y, 560, y)
    
#     # Total Price
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(400, y - 20, "Total Price:")
#     p.drawString(500, y - 20, f"₹ {total_price:.2f}")
    
#     # Save the PDF file
#     p.showPage()
#     p.save()
    
#     # return response
#     return redirect('order')

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from django.shortcuts import redirect

# def generate_invoice(request):
#     print("1111")
#     selected_products = request.session.get('selected_products', [])
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     # Create a ReportLab canvas
#     p = canvas.Canvas(response, pagesize=letter)
    
#     # Set up fonts and styles
#     p.setFont("Helvetica-Bold", 16)
#     p.setStrokeColorRGB(0, 0, 0)
    
#     # Title - Invoice
#     p.drawCentredString(300, 750, "Invoice")
    
#     # Line separator
#     p.line(30, 740, 560, 740)
    
#     # Table headers
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(50, 720, "Product Name")
#     p.drawString(250, 720, "Price (₹)")
#     p.drawString(400, 720, "Quantity")
#     p.drawString(500, 720, "Subtotal (₹)")
    
#     # Line separator
#     p.line(30, 710, 560, 710)
    
#     # Set initial y position for product details
#     y = 700
#     total_price = 0
    
#     # Products
#     p.setFont("Helvetica", 12)
#     for product in selected_products:
#         product_name = product['product_name']
#         product_price = product['product_price']
#         quantity = product['quantity']
#         subtotal = product_price * quantity
        
#         # Product details
#         p.drawString(50, y, product_name)
#         p.drawString(250, y, f"₹ {product_price:.2f}")
#         p.drawString(400, y, str(quantity))
#         p.drawString(500, y, f"₹ {subtotal:.2f}")
        
#         # Update total price
#         total_price += subtotal
        
#         # Move to the next line
#         y -= 20
    
#     # Line separator
#     p.line(30, y, 560, y)
    
#     # Total Price
#     p.setFont("Helvetica-Bold", 12)
#     p.drawString(400, y - 20, "Total Price:")
#     p.drawString(500, y - 20, f"₹ {total_price:.2f}")
    
#     # Save the PDF file
#     p.showPage()
#     p.save()
    
#     # Save the response before redirection
#     response.flush()
    
#     # Redirect to the order page
#     return response  # Note that we should return response first for the PDF to be downloadable

# def generate_invoice_and_redirect(request):
#     response = generate_invoice(request)
#     if response.status_code == 200:
#         return redirect('order')
#     return response



# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from .models import mainuser, SuperMarket

# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
#     user_id = request.session.get('user_id')  # Assume you store the user ID in the session
#     supermarket_id = request.session.get('shop_id')  # Assume you store the supermarket ID in the session

#     # Fetch user and shop details
#     user = mainuser.objects.get(pk=user_id)
#     shop = SuperMarket.objects.get(pk=supermarket_id)
    
#     user_details = {
#         'name': f'{user.user_fname} {user.user_lname}',
#         'email': user.user_mail,
#         'address': 'User Address Here'  # Replace with actual user address if available
#     }
    
#     shop_details = {
#         'name': shop.s_name,
#         'email': shop.s_mail,
#         'address': shop.s_address
#     }
    
#     # Prepare context for the template
#     context = {
#         'selected_products': selected_products,
#         'total_price': sum(product['product_price'] * product['quantity'] for product in selected_products),
#         'user_details': user_details,
#         'shop_details': shop_details
#     }
    
#     # Load the template
#     template = get_template('invoice_template.html')
#     html = template.render(context)
    
#     # Create a PDF from the HTML
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     pisa_status = pisa.CreatePDF(html, dest=response)
    
#     if pisa_status.err:
#         return HttpResponse('We had some errors with code %s' % pisa_status.err)
    
#     return response

# def generate_invoice_and_redirect(request):
#     response = generate_invoice(request)
#     if response.status_code == 200:
#         return redirect('order')
#     return response


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import mainuser, SuperMarket

def generate_invoice(request):
    selected_products = request.session.get('selected_products', [])
    user_id = request.session.get('user_id')  # Assume you store the user ID in the session
    supermarket_id = request.session.get('shop_id')  # Assume you store the supermarket ID in the session

    # Fetch user and shop details
    user = mainuser.objects.get(pk=user_id)
    shop = SuperMarket.objects.get(pk=supermarket_id)
    
    user_details = {
        'name': f'{user.user_fname} {user.user_lname}',
        'email': user.user_mail,
        'phone_number':user.user_phonenumber
      # Replace with actual user address if available
    }
    
    shop_details = {
        'name': shop.s_name,
        'email': shop.s_mail,
        'address': shop.s_address
    }
    
    # Calculate subtotal and total price
    total_price = 0
    for product in selected_products:
        product['subtotal'] = product['product_price'] * product['quantity']
        total_price += product['subtotal']

    # Prepare context for the template
    context = {
        'selected_products': selected_products,
        'total_price': total_price,
        'user_details': user_details,
        'shop_details': shop_details
    }
    
    # Load the template
    template = get_template('invoice_template.html')
    html = template.render(context)
    
    # Create a PDF from the HTML
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors with code %s' % pisa_status.err)
    
    return response

def generate_invoice_and_redirect(request):
    response = generate_invoice(request)
    if response.status_code == 200:
        return redirect('order')
    return response


# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
#     total_price = sum(product['product_price'] for product in selected_products)

#     html_string = ('selected_products.html', {'selected_products': selected_products, 'total_price': total_price})
    
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
#     response.write(result)
    
#     return response
# from django.template.loader import render_to_string
# from .models import SuperMarket, categories, Product
# from xhtml2pdf import pisa
# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
#     total_price = sum(product['product_price'] for product in selected_products)

#     context = {
#         'selected_products': selected_products,
#         'total_price': total_price,
#     }

#     template_path = 'selected_products.html'
#     # Create a Django response object
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

#     # Render html content through template with context
#     template = render_to_string(template_path, context)

#     # Create a pdf
#     pisa_status = pisa.CreatePDF(template, dest=response)
    
#     # Return pdf file
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html_escape(template) + '</pre>')
#     return response
# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import SuperMarket, categories, Product
# import pdfkit

# def generate_invoice(request):
#     selected_products = request.session.get('selected_products', [])
#     total_price = sum(product['product_price'] for product in selected_products)
    
#     # Render the template
#     template = get_template('selected_products.html')
#     html_content = template.render({'selected_products': selected_products, 'total_price': total_price})
    
#     # Convert HTML to PDF
#     options = {
#         'page-size': 'A4',
#         'encoding': "UTF-8",
#     }
#     pdf = pdfkit.from_string(html_content, False, options=options)
    
#     # Prepare response
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
#     return response


# views.py

# from django.shortcuts import render, redirect, get_object_or_404
# from .models import SuperMarket, categories, Product

# def remove_product_from_selection(request):
#     if request.method == 'POST':
#         product_id = int(request.POST['product_id'])
#         selected_products = request.session.get('selected_products', [])
#         updated_products = [product for product in selected_products if product['product_id'] != product_id]
#         request.session['selected_products'] = updated_products
#     return redirect('display_selected_products')


# views.py

# def remove_product_from_selection(request):
#     if request.method == 'POST':
#         product_id = int(request.POST['product_id'])
#         quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not specified
#         selected_products = request.session.get('selected_products', [])

#         for product in selected_products:
#             if product['product_id'] == product_id:
#                 if product['quantity'] > quantity:
#                     product['quantity'] -= quantity
#                 else:
#                     selected_products.remove(product)
#                 break
        
#         request.session['selected_products'] = selected_products
    
#     return redirect('display_selected_products')


def remove_product_from_selection(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        selected_products = request.session.get('selected_products', [])
        
        updated_products = []
        for item in selected_products:
            if item['product_id'] == product_id:
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                    updated_products.append(item)
                # If quantity is 1, remove the item from the list
            elif item['product_id'] != product_id:
                updated_products.append(item)
        
        request.session['selected_products'] = updated_products
        return redirect('display_selected_products')
    
    
    
def order(request):
    # generate_invoice(request)
    return render(request, 'order.html')




from django.shortcuts import render, get_object_or_404
from .models import Order, mainuser

# def user_orders(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         # Redirect to login page if user is not logged in
#         return redirect('login')  # Assuming you have a login view

#     user = get_object_or_404(mainuser, user_id=user_id)
#     orders = Order.objects.filter(user=user).order_by('-order_date')
    
#     return render(request, 'my_orders.html', {'orders': orders, 'user': user})



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Order, mainuser, OrderItem

def user_orders(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Assuming you have a login view

    user = get_object_or_404(mainuser, user_id=user_id)
    orders = Order.objects.filter(user=user).order_by('-order_date')
    
    return render(request, 'my_orders.html', {'orders': orders, 'user': user})

# def order_items(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     items = OrderItem.objects.filter(order=order)
#     items_data = [
#         {
#             'product_image': item.product.product_image,
#             'product_name': item.product.product_name,
#             'quantity': item.product.quantity,
#             'price': item.product.product_price,
#             'total_price': item.quantity * item.price
#         }
#         for item in items
#     ]
#     print(items_data)
#     return JsonResponse({'items': items_data})

from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem

def order_items(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = OrderItem.objects.filter(order=order)
    items_data = []
    for item in items:
        total_price = item.price
        print(total_price)
        items_data.append({
            'product_image': item.product.product_image,
            'product_name': item.product.product_name,
            'quantity': item.quantity,
            'price': item.product.product_price,
            'total_price': total_price
        })
    return render(request, 'order_items.html', {'order': order, 'items': items_data})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, mainuser, OrderUpdate

def track_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        user_id = request.session.get('user_id')
        order = get_object_or_404(Order, pk=order_id,user=user_id)
        updates = OrderUpdate.objects.filter(order=order).order_by('update_timestamp')
        
        return render(request, 'track_order.html', {'order': order, 'updates': updates})
    elif request.method=='GET':
        order_id = request.POST.get('order_id')
        user_id = request.session.get('user_id')
        order = get_object_or_404(Order, pk=order_id,user=user_id)
        updates = OrderUpdate.objects.filter(order=order).order_by('update_timestamp')
        
        return render(request, 'track_order.html', {'order': order, 'updates': updates})
    else:
        return redirect('user_orders')
    
    
# 9999999999999999999999


# def cancel_order(request):
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')
#         user_id = request.session.get('user_id')
#         order = get_object_or_404(Order, order_id=order_id, user=user_id)
#         if order.cancel_order():
#             return redirect('user_orders')
#         else:
#             return HttpResponse("Order cannot be canceled.", status=400)
        
        
def update_order_status(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        order.update_status_to_next()
        # return redirect('track_order')
        shop_id = request.session.get('shop_id')
        return redirect('order_list_view', shop_id)
    else:
        return redirect('user_orders')
    
    
    
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string
from .models import Order

def send_otp_email(email, otp):
    subject = 'Order Cancellation OTP'
    message = f'Your OTP for order cancellation is {otp}. It is valid for 10 minutes.'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email], fail_silently=False)

def cancleorder(request):
    if request.method =='POST':
        order_id=request.POST['order_id']
        print(order_id)
        return render(request,'order_cancle.html',{'order_id':order_id})
    

def cancel_order(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        order_id = request.POST['order_id']
        print(user_email)
        print(order_id)
        order = Order.objects.get(pk=order_id)

        if not order:
            return render(request, 'order_cancel_otp.html', {'error_message': 'Order not found'})

        # Generate OTP
        otp = ''.join(random.choices(string.digits, k=6))
        request.session['otp'] = otp
        request.session['email'] = user_email
        request.session['order_id'] = order_id

        # Send OTP to user's email
        send_otp_email(user_email, otp)

        return redirect('verify_otp')  # Redirect to OTP verification page

    return render(request, 'order_cancel.html')


from django.shortcuts import render, redirect

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST['otp']
        if otp_entered == request.session.get('otp'):
            # OTP is correct, proceed with order cancellation
            order_id = request.session.get('order_id')
            # order = Order.objects.get(pk=order_id)
            # order.status = 'Canceled'
            # order.save()
            user_id = request.session.get('user_id')
            order = get_object_or_404(Order, order_id=order_id, user=user_id)
            if order.cancel_order():
                
                       # Send confirmation email
            # user_email = request.session.get('email')
            # send_confirmation_email(user_email)

                del request.session['otp']
                del request.session['email']
                del request.session['order_id']
                return redirect('user_orders')
            # return redirect('user_orders')  # Redirect to orders page

        else:
            return render(request, 'order_cancel_otp.html', {'error_message': 'Invalid OTP'})

    return render(request, 'order_cancle_otp.html')

# # import razorpay
# # from django.conf import settings
# # from django.shortcuts import render, redirect, get_object_or_404
# # from .models import Order, Payment

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# # def checkout(request, order_id):
# #     order = get_object_or_404(Order, order_id=order_id)
# #     if request.method == 'POST':
# #         payment_id = request.POST.get('razorpay_payment_id')
# #         try:
# #             razorpay_client.payment.capture(payment_id, int(order.total_price * 100))  # Amount in paise

# #             # Create payment record
# #             Payment.objects.create(
# #                 order=order,
# #                 payment_method='Razorpay',
# #                 amount=order.total_price,
# #                 payment_status='Completed'
# #             )

# #             # Update order status or any other post-payment logic
# #             return redirect('order_success', order_id=order_id)

# #         except razorpay.errors.RazorpayError as e:
# #             # Handle error
# #             return render(request, 'checkout.html', {'order': order, 'error': str(e)})

# #     # Create Razorpay order
# #     razorpay_order = razorpay_client.order.create(dict(amount=int(order.total_price * 100), currency='INR', payment_capture='0'))

# #     return render(request, 'checkout.html', {
# #         'order': order,
# #         'razorpay_order_id': razorpay_order['id'],
# #         'razorpay_key_id': settings.RAZORPAY_KEY_ID,
# #         'amount': int(order.total_price * 100)
# #     })


# # import razorpay
# # from django.conf import settings
# # from django.shortcuts import render, redirect, get_object_or_404
# # from .models import Order, Payment

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# # def checkout(request, order_id):
# #     order = get_object_or_404(Order, order_id=order_id)
# #     if request.method == 'POST':
# #         payment_id = request.POST.get('razorpay_payment_id')
# #         try:
# #             razorpay_client.payment.capture(payment_id, int(order.total_price * 100))  # Amount in paise

# #             # Create payment record
# #             Payment.objects.create(
# #                 order=order,
# #                 payment_method='Razorpay',
# #                 amount=order.total_price,
# #                 payment_status='Completed'
# #             )

# #             # Update order status or any other post-payment logic
# #             return redirect('order_success', order_id=order_id)

# #         except razorpay.errors.RazorpayError as e:
# #             # Handle error
# #             return render(request, 'checkout.html', {'order': order, 'error': str(e)})

# #     # Create Razorpay order
# #     razorpay_order = razorpay_client.order.create(dict(amount=int(order.total_price * 100), currency='INR', payment_capture='0'))

# #     return render(request, 'checkout.html', {
# #         'order': order,
# #         'razorpay_order_id': razorpay_order['id'],
# #         'razorpay_key_id': settings.RAZORPAY_KEY_ID,
# #         'amount': int(order.total_price * 100)
# #     })


# # from django.shortcuts import render, get_object_or_404
# # from django.http import JsonResponse
# # from .models import Order, Payment
# # import razorpay
# # from django.conf import settings

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# # def create_payment(request, order_id):
# #     order = get_object_or_404(Order, pk=order_id)
# #     currency = 'INR'
# #     amount = int(order.total_price * 100)  # Amount in paise

# #     razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
# #     order_id = razorpay_order['id']

# #     # Save order_id in the Payment model
# #     payment = Payment(
# #         order=order,
# #         amount=order.total_price,
# #         payment_status='Pending'
# #     )
# #     payment.save()

# #     context = {
# #         'order_id': order_id,
# #         'razorpay_key': settings.RAZORPAY_KEY_ID,
# #         'amount': amount,
# #         'currency': currency,
# #         'callback_url': 'paymenthandler/',  # Define the callback URL for handling the response
# #     }

# #     return render(request, 'payment.html', context)

# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.conf import settings
# # from .models import Order, Payment
# # import razorpay

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
# # from django.views.decorators.csrf import csrf_exempt

# # @csrf_exempt
# # def create_payment(request):
# #     if request.method == 'POST':
# #         order_idf = request.POST['order_id']
        
# #         # order_id = request.session.get('order_id')
# #         print(order_idf)
# #         order = get_object_or_404(Order, pk=order_idf)
# #         currency = 'INR'
# #         amount = int(order.total_price * 100)  # Amount in paise

# #         razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
# #         razorpay_order_id = razorpay_order['id']

# #         # Save razorpay_order_id in the Payment model
# #         payment = Payment(
# #             order=order,
# #             amount=order.total_price,
# #             payment_status='Pending'
# #         )
# #         payment.save()

# #         context = {
# #             'order_id': razorpay_order_id,
# #             'razorpay_key': settings.RAZORPAY_KEY_ID,
# #             'amount': amount,
# #             'currency': currency,
# #             'callback_url': 'paymenthandler/',  # Define the callback URL for handling the response
# #         }

# #         return render(request, 'payment.html', context)

# #     return redirect('home')  # Redirect to the order summary or appropriate page if not a POST request


# # # from django.views.decorators.csrf import csrf_exempt
# # # from django.http import HttpResponseBadRequest
# # # from .models import Order, Payment
# # # import razorpay
# # # from django.conf import settings
# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import JsonResponse, HttpResponseBadRequest
# # import razorpay
# # from .models import Payment
# # from django.conf import settings



# # @csrf_exempt
# # def payment_handler(request):
# #     if request.method == "POST":
# #         try:
# #             payment_id = request.POST.get('razorpay_payment_id', '')
# #             orderid = request.POST.get('razorpay_order_id', '')
# #             signature = request.POST.get('razorpay_signature', '')

# #             params_dict = {
# #                 'razorpay_order_id': orderid,
# #                 'razorpay_payment_id': payment_id,
# #                 'razorpay_signature': signature
# #             }

# #             # Verify the payment signature
# #             result = razorpay_client.utility.verify_payment_signature(params_dict)
# #             if result:
# #                 amount = request.POST.get('amount', '')  # Amount in paise
# #                 try:
# #                     razorpay_client.payment.capture(payment_id, amount)
                    
# #                     # Update payment status
# #                     payment = Payment.objects.get(order__order_id=orderid)
# #                     payment.payment_status = 'Completed'
# #                     payment.payment_method = 'UPI'
# #                     payment.save()

# #                     return JsonResponse({'status': 'Payment successful'})
# #                 except:
# #                     # If there is an error in capturing the payment
# #                     return JsonResponse({'status': 'Payment failed'})

# #             else:
# #                 return JsonResponse({'status': 'Payment verification failed'})

# #         except:
# #             return HttpResponseBadRequest()
# #     else:
# #         return HttpResponseBadRequest()


# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.conf import settings
# # from .models import Order, Payment
# # import razorpay

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# # def create_payment(request):
# #     if request.method == 'POST':
# #         order_id = request.POST.get('order_id')
# #         if not order_id:
# #             return redirect('order_summary', order_id=order_id)  # Redirect if order_id is not present

# #         # Store the order_id in the session
# #         request.session['order_id'] = order_id

# #         order = get_object_or_404(Order, pk=order_id)
# #         currency = 'INR'
# #         amount = int(order.total_price * 100)  # Amount in paise

# #         razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
# #         razorpay_order_id = razorpay_order['id']

# #         # Save razorpay_order_id in the Payment model
# #         payment = Payment(
# #             order=order,
# #             amount=order.total_price,
# #             payment_status='Pending'
# #         )
# #         payment.save()

# #         context = {
# #             'order_id': razorpay_order_id,
# #             'razorpay_key': settings.RAZORPAY_KEY_ID,
# #             'amount': amount,
# #             'currency': currency,
# #             'callback_url': 'paymenthandler/',  # Define the callback URL for handling the response
# #         }

# #         return render(request, 'payment.html', context)

# #     return redirect('home')  # Redirect to the order summary or appropriate page if not a POST request

# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import JsonResponse, HttpResponseBadRequest
# # from .models import Payment
# # import razorpay
# # from django.conf import settings

# # razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# # @csrf_exempt
# # def payment_handler(request):
# #     if request.method == "POST":
# #         try:
# #             payment_id = request.POST.get('razorpay_payment_id', '')
# #             razorpay_order_id = request.POST.get('razorpay_order_id', '')
# #             signature = request.POST.get('razorpay_signature', '')

# #             params_dict = {
# #                 'razorpay_order_id': razorpay_order_id,
# #                 'razorpay_payment_id': payment_id,
# #                 'razorpay_signature': signature
# #             }

# #             # Verify the payment signature
# #             result = razorpay_client.utility.verify_payment_signature(params_dict)
# #             if result:
# #                 amount = request.POST.get('amount', '')  # Amount in paise
# #                 try:
# #                     razorpay_client.payment.capture(payment_id, amount)
                    
# #                     # Retrieve the order_id from the session
# #                     order_id = request.session.get('order_id')
# #                     if not order_id:
# #                         return JsonResponse({'status': 'Order ID not found in session'})

# #                     # Update payment status
# #                     payment = Payment.objects.get(order__id=order_id)
# #                     payment.payment_status = 'Completed'
# #                     payment.payment_method = 'UPI'
# #                     payment.save()

# #                     return JsonResponse({'status': 'Payment successful'})
# #                 except Exception as e:
# #                     # If there is an error in capturing the payment
# #                     return JsonResponse({'status': 'Payment failed', 'error': str(e)})

# #             else:
# #                 return JsonResponse({'status': 'Payment verification failed'})

# #         except Exception as e:
# #             return HttpResponseBadRequest(f"Error: {str(e)}")
# #     else:
# #         return HttpResponseBadRequest()
# # from PayTm import Checksum
# from sm_app import keys
# from django.conf import settings
# MERCHANT_KEY=keys.MK

# # def paymentprocess(request):
# #         order_id=request.session.get('order_id')
# #         id = order_id
# #         oid=str(id)+"ShopyCart"
# #         param_dict = {

# #             'MID':keys.MID,
# #             'ORDER_ID': oid,
# #             'TXN_AMOUNT': str(amount),
# #             'CUST_ID': email,
# #             'INDUSTRY_TYPE_ID': 'Retail',
# #             'WEBSITE': 'WEBSTAGING',
# #             'CHANNEL_ID': 'WEB',
# #             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

# #         }
# #         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
# #         return render(request, 'paytm.html', {'param_dict': param_dict})

# #     return render(request, 'checkout.html')


# # @csrf_exempt
# # def handlerequest(request):
# #     # paytm will send you post request here
# #     form = request.POST
# #     response_dict = {}
# #     for i in form.keys():
# #         response_dict[i] = form[i]
# #         if i == 'CHECKSUMHASH':
# #             checksum = form[i]

# #     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
# #     if verify:
# #         if response_dict['RESPCODE'] == '01':
# #             print('order successful')
# #             a=response_dict['ORDERID']
# #             b=response_dict['TXNAMOUNT']
# #             rid=a.replace("ShopyCart","")
           
# #             print(rid)
# #             filter2= Orders.objects.filter(order_id=rid)
# #             print(filter2)
# #             print(a,b)
# #             for post1 in filter2:

# #                 post1.oid=a
# #                 post1.amountpaid=b
# #                 post1.paymentstatus="PAID"
# #                 post1.save()
# #             print("run agede function")
# #         else:
# #             print('order was not successful because' + response_dict['RESPMSG'])
# #     return render(request, 'paymentstatus.html', {'response': response_dict})


# # views.py

# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from .models import Payment, Order
# from .paytm import initiate_transaction, verify_checksum
# from django.conf import settings
# from django.contrib.auth.decorators import login_required

# # @login_required
# # def place_order(request):
# #     # Assuming you have a function to create an order
# #     order = Order.objects.create(order_id='ORDER12345', total_price=100.0)
    
# #     # Set the order details in session
# #     request.session['order_id'] = order.pk
# #     request.session['amount'] = order.total_price
# #     request.session['user_id'] = request.user.id

# #     return redirect('initiate_payment')

# # def initiate_payment(request):
# #     if request.method == 'POST':
# #         order_id = request.session.get('order_id')
# #         amount = request.session.get('amount')
# #         customer_id = request.session.get('user_id')

# #         # Get the Order object
# #         order = get_object_or_404(Order, pk=order_id)
        
# #         # Create Payment object
# #         payment = Payment(order=order, amount=amount, payment_status='Pending')
# #         payment.save()

# #         paytm_params = initiate_transaction(order_id, amount, customer_id)
# #         context = {
# #             'paytm_params': paytm_params,
# #             'paytm_url': 'https://securegw-stage.paytm.in/order/process'
# #         }

# #         return render(request, 'paytm_payment.html', context)
# #     return render(request, 'initiate_payment.html')

# # @csrf_exempt
# # def payment_response(request):
# #     if request.method == 'POST':
# #         paytm_response = request.POST.dict()
# #         paytm_checksum = paytm_response.pop('CHECKSUMHASH', None)
# #         is_valid_checksum = verify_checksum(paytm_response, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

# #         if is_valid_checksum:
# #             if paytm_response['RESPCODE'] == '01':
# #                 payment = get_object_or_404(Payment, order__order_id=paytm_response['ORDERID'])
# #                 payment.payment_status = 'Completed'
# #                 payment.payment_method = 'Paytm'
# #                 payment.save()
# #                 return render(request, 'payment_success.html', {'response': paytm_response})
# #             else:
# #                 return render(request, 'payment_failed.html', {'response': paytm_response})
# #         else:
# #             return JsonResponse({'status': 'Checksum Mismatch'}, status=400)
# #     return JsonResponse({'status': 'Bad Request'}, status=400)


# # # views.py
# # from django.shortcuts import render, get_object_or_404, redirect
# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import JsonResponse, HttpResponseBadRequest
# # from .models import Payment, Order
# # from .paytm import initiate_transaction, verify_checksum
# # from django.conf import settings
# # from django.contrib.auth.decorators import login_required

# # @login_required
# # def place_order(request):
# #     order = Order.objects.create(order_id='ORDER12345', total_price=100.0)
# #     request.session['order_id'] = order.pk
# #     request.session['amount'] = order.total_price
# #     request.session['user_id'] = request.user.id
# #     return redirect('initiate_payment')

# # def initiate_payment(request):
# #     if request.method == 'POST':
# #         order_id = request.session.get('order_id')
# #         amount = request.session.get('amount')
# #         customer_id = request.session.get('user_id')

# #         order = get_object_or_404(Order, pk=order_id)

# #         payment, created = Payment.objects.get_or_create(
# #             order=order,
# #             defaults={'amount': amount, 'payment_status': 'Pending'}
# #         )

# #         if not created:
# #             payment.amount = amount
# #             payment.save()

# #         paytm_params = initiate_transaction(order_id, amount, customer_id)
# #         context = {
# #             'paytm_params': paytm_params,
# #             'paytm_url': 'https://securegw-stage.paytm.in/order/process'  # Use 'https://securegw.paytm.in/order/process' for production
# #         }

# #         return render(request, 'paytm_payment.html', context)
# #     return render(request, 'initiate_payment.html')

# # # @csrf_exempt
# # # def payment_response(request):
# # #     if request.method == 'POST':
# # #         paytm_response = request.POST.dict()
# # #         paytm_checksum = paytm_response.pop('CHECKSUMHASH', None)
# # #         is_valid_checksum = verify_checksum(paytm_response, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

# # #         if is_valid_checksum:
# # #             if paytm_response['RESPCODE'] == '01':
# # #                 payment = get_object_or_404(Payment, order__order_id=paytm_response['ORDERID'])
# # #                 payment.payment_status = 'Completed'
# # #                 payment.payment_method = 'Paytm'
# # #                 payment.save()
# # #                 return render(request, 'payment_success.html', {'response': paytm_response})
# # #             else:
# # #                 return render(request, 'payment_failed.html', {'response': paytm_response})
# # #         else:
# # #             return JsonResponse({'status': 'Checksum Mismatch'}, status=400)
# # #     return JsonResponse({'status': 'Bad Request'}, status=400)
# # # # views.py
# # # @csrf_exempt
# # # def payment_response(request):
# # #     if request.method == 'POST':
# # #         paytm_response = request.POST.dict()
# # #         paytm_checksum = paytm_response.get('CHECKSUMHASH', None)
# # #         is_valid_checksum = verify_checksum(paytm_response, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

# # #         if is_valid_checksum:
# # #             if paytm_response['RESPCODE'] == '01':
# # #                 payment = get_object_or_404(Payment, order__order_id=paytm_response['ORDERID'])
# # #                 payment.payment_status = 'Completed'
# # #                 payment.payment_method = 'Paytm'
# # #                 payment.save()
# # #                 return render(request, 'payment_success.html', {'response': paytm_response})
# # #             else:
# # #                 return render(request, 'payment_failed.html', {'response': paytm_response})
# # #         else:
# # #             return JsonResponse({'status': 'Checksum Mismatch'}, status=400)
# # #     return JsonResponse({'status': 'Bad Request'}, status=400)

# # @csrf_exempt
# # def payment_response(request):
# #     if request.method == 'POST':
# #         paytm_response = request.POST.dict()
# #         paytm_checksum = paytm_response.get('CHECKSUMHASH', None)

# #         if paytm_checksum is None:
# #             return JsonResponse({'status': 'Checksum is missing'}, status=400)

# #         is_valid_checksum = verify_checksum(paytm_response, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

# #         if is_valid_checksum:
# #             if paytm_response['RESPCODE'] == '01':
# #                 payment = get_object_or_404(Payment, order__order_id=paytm_response['ORDERID'])
# #                 payment.payment_status = 'Completed'
# #                 payment.payment_method = 'Paytm'
# #                 payment.save()
# #                 return render(request, 'payment_success.html', {'response': paytm_response})
# #             else:
# #                 return render(request, 'payment_failed.html', {'response': paytm_response})
# #         else:
# #             return JsonResponse({'status': 'Checksum Mismatch'}, status=400)
# #     return JsonResponse({'status': 'Bad Request'}, status=400)
# from sm_app import keys
# from django.conf import settings
# # MERCHANT_KEY=keys.MK
# import json
# from django.views.decorators.csrf import  csrf_exempt
# from PayTm import Checksum

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from .models import Order, Payment
# import paytmchecksum
# # import keys  # Ensure you have a keys.py file with your MID and MERCHANT_KEY

# def initiate_payment(request):
#     if request.method != 'post':
#         # Assume 'order_id' and 'amount' are passed via POST or from session
#         # order_id = request.POST.get('order_id')
#         # amount = request.POST.get('amount')
#         # email = request.POST.get('email')  # Assume email is available
#         order_id = request.session.get('order_id')
#         amount = request.session.get('amount')
#         email = request.session.get('user_mail')

#         # order = get_object_or_404(Order, pk=order_id)


#         # Get the order object
#         order = get_object_or_404(Order, pk=order_id)

#         oid = str(order.order_id) + "ShopyCart"
#         param_dict = {
#             'MID': keys.MID,
#             'ORDER_ID': oid,
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': email,
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
#         }
#         # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,keys.MK)
#         # Save the payment initiation
#         # payment = Payment(
#         #     order=order,
#         #     amount=amount,
#         #     payment_status='Pending'
#         # )
#         # payment.save()

#         return render(request, 'paytm.html', {'param_dict': param_dict})

#     return render(request, 'home.html')


# # @csrf_exempt
# # def handlerequest(request):
# #     # Paytm will send a POST request here
# #     form = request.POST
# #     response_dict = {}
# #     checksum = ""

# #     for i in form.keys():
# #         response_dict[i] = form[i]
# #         if i == 'CHECKSUMHASH':
# #             checksum = form[i]

# #     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
# #     if verify:
# #         if response_dict['RESPCODE'] == '01':
# #             print('Order successful')
# #             oid = response_dict['ORDERID']
# #             rid = oid.replace("ShopyCart", "")
# #             amount = response_dict['TXNAMOUNT']

# #             # Get the order and update payment status
# #             order = get_object_or_404(Order, order_id=rid)
# #             payment = get_object_or_404(Payment, order=order)

# #             payment.payment_status = 'Completed'
# #             payment.payment_method = 'Paytm'
# #             payment.save()

# #             order.payment_status = 'PAID'
# #             order.save()

# #         else:
# #             print('Order was not successful because: ' + response_dict['RESPMSG'])
# #             oid = response_dict['ORDERID']
# #             rid = oid.replace("ShopyCart", "")

# #             order = get_object_or_404(Order, order_id=rid)
# #             payment = get_object_or_404(Payment, order=order)

# #             payment.payment_status = 'Failed'
# #             payment.payment_method = 'Paytm'
# #             payment.save()
# #     else:
# #         print('Checksum Mismatch')

# #     return render(request, 'paymentstatus.html', {'response': response_dict})
# @csrf_exempt
# def handlerequest(request):
#     form = request.POST
#     response_dict = {}
#     checksum = "CHECKSUMHASH"
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]
#     # if request.method == 'POST':
#     #     form = request.POST
#     #     response_dict = {}
#     #     checksum = ""

#     #     for key, value in form.items():
#     #         response_dict[key] = value
#     #         if key == 'CHECKSUMHASH':
#     #             checksum = value

#         verify =Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#         if verify:
#             if response_dict.get('RESPCODE') == '01':
#                 print('Order successful')
#                 order_id = response_dict.get('ORDERID')
#                 # Extract the actual order ID from the Paytm format
#                 actual_order_id = order_id.replace("ShopyCart", "")

#                 amount = response_dict.get('TXNAMOUNT')

#                 # Handle the rest of the processing based on retrieved parameters
#                 # Ensure that ORDERID and TXNAMOUNT are properly retrieved before using them further

#             else:
#                 print('Order was not successful because: ' + response_dict.get('RESPMSG'))
#         else:
#             print('Checksum Mismatch')

#     return render(request, 'paymentstatus.html', {'response': response_dict})

# from sm_app.models import mainuser,Product,Order,OrderItem,Payment
# from django.shortcuts import render, redirect
# from django.conf import settings
# from paytmchecksum import generateSignature
# import json

# def initiate_payment(request):
#     order_id = request.session.get('order_id')
#     amount = request.session.get('amount')
#     # customer_id = request.session.get('user_id')

#     order = Order.objects.get(pk=order_id)
#     payment = Payment.objects.create(
#         order=order,
#         payment_method='Paytm',
#         amount=order.total_price,
#         payment_status='Pending'
#     )
    
#     paytm_params = {
#         'MID': settings.PAYTM_MERCHANT_ID,
#         'ORDER_ID': str(payment.payment_id),
#         'CUST_ID': str(order.user.user_id),
#         'TXN_AMOUNT': str(payment.amount),
#         'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
#         'WEBSITE': settings.PAYTM_WEBSITE,
#         'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
#         'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
#     }
    
#     paytm_params['CHECKSUMHASH'] = generateSignature(json.dumps(paytm_params), settings.PAYTM_MERCHANT_KEY)

#     context = {
#         'paytm_params': paytm_params,
#         'paytm_url': 'https://securegw.paytm.in/theia/processTransaction'
#     }
    
#     return render(request, 'paytm_redirect.html', context)


# # from django.views.decorators.csrf import csrf_exempt
# # from django.http import HttpResponse
# # from paytmchecksum import verifySignature

# # @csrf_exempt
# # def payment_callback(request):
# #     received_data = dict(request.POST)
# #     paytm_params = {}
# #     paytm_checksum = received_data.pop('CHECKSUMHASH')[0]

# #     for key, value in received_data.items():
# #         paytm_params[key] = value[0]

# #     is_valid_checksum = verifySignature(paytm_params, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

# #     if is_valid_checksum:
# #         order_id = paytm_params['ORDERID']
# #         payment = Payment.objects.get(pk=order_id)
# #         payment.transaction_id = paytm_params['TXNID']
# #         payment.payment_status = paytm_params['STATUS']
# #         payment.save()

# #         if paytm_params['STATUS'] == 'TXN_SUCCESS':
# #             # Payment successful
# #             return HttpResponse("Payment Successful")
# #         else:
# #             # Payment failed
# #             return HttpResponse("Payment Failed")
# #     else:
# #         # Checksum verification failed
# #         return HttpResponse("Checksum Verification Failed")
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# from django.conf import settings
# from paytmchecksum import verifySignature
# import logging

# # Set up logging
# logger = logging.getLogger(__name__)

# @csrf_exempt
# def payment_callback(request):
#     received_data = dict(request.POST)
#     paytm_params = {}
#     paytm_checksum = received_data.get('CHECKSUMHASH', [None])[0]

#     for key, value in received_data.items():
#         paytm_params[key] = value[0]

#     if not paytm_checksum:
#         logger.error("CHECKSUMHASH is missing in the callback data")
#         return HttpResponse("Checksum Hash Missing", status=400)

#     is_valid_checksum = verifySignature(paytm_params, settings.PAYTM_MERCHANT_KEY, paytm_checksum)

#     if is_valid_checksum:
#         order_id = paytm_params['ORDERID']
#         payment = Payment.objects.get(pk=order_id)
#         payment.transaction_id = paytm_params['TXNID']
#         payment.payment_status = paytm_params['STATUS']
#         payment.save()

#         if paytm_params['STATUS'] == 'TXN_SUCCESS':
#             # Payment successful
#             return HttpResponse("Payment Successful")
#         else:
#             # Payment failed
#             return HttpResponse("Payment Failed")
#     else:
#         # Checksum verification failed
#         logger.error("Checksum verification failed for data: %s", received_data)
#         return HttpResponse("Checksum Verification Failed", status=400)

# def typesofpayments(request):
#     if request.method=="POST":
#         shopemail=request.POST['shopmail']
#         useremail=request.POST['usermail']
#         address=request.POST['address']
#         invoice=request.POST['invoice']
        
#         request.session['shopemail'] = shopemail
#         request.session['usermail']=useremail
#         request.session['address']=address
#         request.session['invoice']=invoice
        
#         return render(request,'typesofpayments.html')
#     return render(request,'orderplace.html')

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST['shopmail']
#         useremail = request.POST['usermail']
#         address = request.POST['address']
#         invoice = request.FILES['invoice']

#         fs = FileSystemStorage()
#         filename = fs.save(invoice.name, invoice)
#         invoice_url = fs.url(filename)

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice'] = invoice_url

#         # return redirect('typesofpayments')
#         return render(request,'typesofpayments.html')
#     return render(request, 'orderplace.html')


# from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render, redirect

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         if invoice:
#             fs = FileSystemStorage()
#             filename = fs.save(invoice.name, invoice)
#             invoice_url = fs.url(filename)
#         else:
#             invoice_url = None

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice'] = invoice_url
        
#         return render(request,'typesofpayments.html')

#         # return redirect('typesofpayments')
#     return render(request, 'orderplace.html')


# from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render, redirect

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         if invoice:
#             fs = FileSystemStorage()
#             filename = fs.save(invoice.name, invoice)
#             invoice_url = fs.url(filename)
#         else:
#             invoice_url = None

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice'] = invoice_url

#         # return redirect('typesofpayments')  # Adjust this URL as needed
#         return render(request,'typesofpayments.html')
#     return render(request, 'orderplace.html')


# from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render, redirect

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         print(useremail)
#         invoice = request.FILES.get('invoice')
#         print(invoice)
#         # if invoice:
#         #     fs = FileSystemStorage()
#         #     filename = fs.save(invoice.name, invoice)
#         #     invoice_url = fs.url(filename)
#         # else:
#         #     invoice_url = None

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice'] = invoice  # Store filename instead of URL

#         # return redirect('typesofpayments')  # Adjust this URL as needed
#         return render(request,'typesofpayments.html')

#     return render(request, 'orderplace.html')


# def cashondelivery(request):
#     if request.method=="POST":
#         shopmail= request.session.get('shopmail')
#         usermail= request.session.get('usermail')
#         address= request.session.get('address')
#         invoice= request.session.get('invoice')
        
from django.core.mail import send_mail
from django.conf import settings

# def cashondelivery(request):
#     if request.method == "POST":
#         shopmail = request.session.get('shopmail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice = request.session.get('invoice')
        
#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})
#     return redirect('typesofpayments')


# from django.core.mail import send_mail
# from django.shortcuts import render

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice = request.session.get('invoice')

#         email_from = settings.EMAIL_HOST_USER
#         # Send email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         send_mail(shop_subject, shop_message, email_from, [shopmail])

#         # Send email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         send_mail(user_subject, user_message, email_from, [usermail])

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'orderplaced.html')  # Assuming you have an orderplaced.html template

#     return render(request, 'typesofpayments.html')  # Render the same page if method is not POST


# from django.core.mail import EmailMessage
# from django.conf import settings

# def cashondelivery(request):
#     if request.method == "POST":
#         shopmail = request.session.get('shopmail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice = request.session.get('invoice')

#         subject = 'Order Confirmation'
#         message = f'Your order has been placed successfully. Delivery address: {address}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [shopmail, usermail]

#         email = EmailMessage(subject, message, email_from, recipient_list)

#         # Attach the invoice file
#         invoice_path = settings.MEDIA_ROOT + invoice
#         email.attach_file(invoice_path)

#         email.send(fail_silently=False)

#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})
#     return redirect('typesofpayments')

# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.shortcuts import render
# import os

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_url = request.session.get('invoice')

#         invoice_path = os.path.join(settings.MEDIA_ROOT, invoice_url.strip("/"))

#         email_from = settings.EMAIL_HOST_USER

#         # Send email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])
#         shop_email.attach_file(invoice_path)
#         shop_email.send()

#         # Send email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])
#         user_email.attach_file(invoice_path)
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.shortcuts import render, redirect
# import os

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_url = request.session.get('invoice')

#         email_from = settings.EMAIL_HOST_USER

#         # Send email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Attach the invoice if it exists
#         if invoice_url:
#             invoice_path = os.path.join(settings.MEDIA_ROOT, invoice_url.strip("/"))
#             shop_email.attach_file(invoice_path)
        
#         shop_email.send()

#         # Send email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_url:
#             user_email.attach_file(invoice_path)

#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.shortcuts import render, redirect
# import os

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_url = request.session.get('invoice')

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_url:
#             invoice_path = os.path.join(settings.MEDIA_ROOT, invoice_url.strip("/"))
#             shop_email.attach_file(invoice_path)
#             user_email.attach_file(invoice_path)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.shortcuts import render, redirect
# import os

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice = request.session.get('invoice')
#         print(invoice)
#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         # if invoice_filename:
#         #     invoice_path = os.path.join(settings.MEDIA_ROOT, invoice_filename)
#         #     shop_email.attach_file(invoice_path)
#         #     user_email.attach_file(invoice_path)
#         shop_email.attach(invoice.name,invoice.read(),invoice.content_type)

#         shop_email.send()
#         user_email.attach(invoice.name,invoice.read(),invoice.content_type)
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# views.py

# from django.shortcuts import render, redirect
# from django.core.mail import EmailMessage
# from django.conf import settings

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice'] = invoice  # Store file object in session

#         # return redirect('')  # Redirect to cashondelivery view
#         return render(request,'typesofpayments.html')

#     return render(request, 'orderplace.html')

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice = request.session.get('invoice')

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice:
#             shop_email.attach(invoice.name, invoice.read(), invoice.content_type)
#             user_email.attach(invoice.name, invoice.read(), invoice.content_type)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# views.py

# from django.shortcuts import render, redirect
# from django.core.mail import EmailMessage
# from django.conf import settings

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice_name'] = invoice.name if invoice else None  # Store filename instead of file object
#         print(invoice.name)
#         # return redirect('cashondelivery')  # Redirect to cashondelivery view
#         return render(request,'typesofpayments.html')


#     return render(request, 'orderplace.html')

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_name = request.session.get('invoice_name')
#         print(invoice_name)
#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_name:
#             # Create the invoice content to attach
#             invoice_content = request.FILES['invoice'].read()
#             shop_email.attach(invoice_name, invoice_content, request.FILES['invoice'].content_type)
#             user_email.attach(invoice_name, invoice_content, request.FILES['invoice'].content_type)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice_name']

#         # Return a response
#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')
# views.py

# from django.shortcuts import render, redirect
# from django.core.mail import EmailMessage
# from django.conf import settings

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice_name'] = invoice.name if invoice else None  # Store filename instead of file object

#         # return redirect('cashondelivery')  # Redirect to cashondelivery view
#         return render(request,'typesofpayments.html')
#     return render(request, 'orderplace.html')

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_name = request.session.get('invoice_name')
#         invoice_content = None

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_name:
#             print("11111111")
#             print(invoice_name)
#             invoice_file = request.FILES.get('invoice')
#             print(invoice_file)
#             invoice_content = invoice_file.read()
#             shop_email.attach(invoice_name, invoice_content, invoice_file.content_type)
#             user_email.attach(invoice_name, invoice_content, invoice_file.content_type)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice_name']

#         # Return a response
#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')

# views.py

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address
#         request.session['invoice_name'] = invoice.name if invoice else None  # Store filename instead of file object
#         request.session['invoice']=invoice
#         # return redirect('cashondelivery')  # Redirect to cashondelivery view
#         return render(request,'typesofpayments.html')

#     return render(request, 'orderplace.html')

# def cashondelivery(request):
    # if request.method == "POST":
    #     # Retrieve session data
    #     shopmail = request.session.get('shopemail')
    #     usermail = request.session.get('usermail')
    #     address = request.session.get('address')
    #     invoice_name = request.session.get('invoice_name')
    #     print("1111111")
    #     print(invoice_name)
    #     email_from = settings.EMAIL_HOST_USER

    #     # Prepare email to shop
    #     shop_subject = 'New Cash on Delivery Order'
    #     shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
    #     shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

    #     # Prepare email to user
    #     user_subject = 'Order Confirmation'
    #     user_message = 'Your order has been received and will be delivered soon. Thank you!'
    #     user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

    #     # Attach the invoice if it exists in the session
    #     if invoice_name:
    #         invoice_content = request.session.get('invoice')
    #         if invoice_content:
    #             shop_email.attach(invoice_name, invoice_content, 'application/pdf')  # Adjust content type if needed
    #             user_email.attach(invoice_name, invoice_content, 'application/pdf')  # Adjust content type if needed

    #     shop_email.send()
    #     user_email.send()

    #     # Clear session data
    #     del request.session['shopemail']
    #     del request.session['usermail']
    #     del request.session['address']
    #     del request.session['invoice_name']
    #     # del request.session['invoice_content']

    #     # Return a response
    #     return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

    # return render(request, 'typesofpayments.html')

# def cashondelivery(request):
#     shopmail = request.session.get('shopmail')
#     usermail = request.session.get('usermail')
#     return render(request, 'orderplace.html', {'shopmail': shopmail, 'usermail':usermail})
#     # return redirect('typesofpayments')

# def orderdone(request):
#     if request.method == "POST":
#         shopmail = request.POST.get('shopmail')
#         usermail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice1 = request.FILES.get('invoice')
#         invoice2=invoice1
        
#         email_from = settings.EMAIL_HOST_USER

# #         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         shop_email.attach(invoice1.name,invoice1.read(),invoice1.content_type)
#         shop_email.send()
# #         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])
        
#         user_email.attach(invoice2.name,invoice2.read(),invoice2.content_type)
#         user_email.send()
        
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})
#     return render(request, 'orderplace.html')

# views.py *******************working code **************

# from django.shortcuts import render, redirect
# from django.core.mail import EmailMessage
# from django.conf import settings

# def cashondelivery(request):
#     shopmail = request.session.get('shopmail')
#     usermail = request.session.get('usermail')
#     return render(request, 'orderplace.html', {'shopmail': shopmail, 'usermail': usermail})

# def orderdone(request):
#     if request.method == "POST":
#         shopmail = request.POST.get('shopmail')
#         usermail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         if invoice:
#             invoice_content = invoice.read()
#             invoice_name = invoice.name
#             shop_email.attach(invoice_name, invoice_content, invoice.content_type)

#         shop_email.send()

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         if invoice:
#             user_email.attach(invoice_name, invoice_content, invoice.content_type)

#         user_email.send()

#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'orderplace.html')



from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         # Store the invoice file in memory
#         if invoice and isinstance(invoice, InMemoryUploadedFile):
#             request.session['invoice_name'] = invoice.name
#             request.session['invoice_content'] = invoice.read()

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address

#         return redirect('typesofpayments.html')  # URL name of the typesofpayments view

#     return render(request, 'orderplace.html')

from django.shortcuts import render, redirect

# def typesofpayments(request):
#     if request.method == "POST":
#         shopemail = request.POST.get('shopmail')
#         useremail = request.POST.get('usermail')
#         address = request.POST.get('address')
#         invoice = request.FILES.get('invoice')

#         # Save file temporarily in memory
#         if invoice:
#             request.session['invoice_name'] = invoice.name
#             request.session['invoice_content_type'] = invoice.content_type
#             request.session['invoice'] = invoice.read().decode('latin1')  # Decode bytes to string

#         request.session['shopemail'] = shopemail
#         request.session['usermail'] = useremail
#         request.session['address'] = address

#         # return redirect('typesofpayments.htm')  # URL name of the typesofpayments view
#         return render(request, 'typesofpayments.html')

#     return render(request, 'orderplace.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Order

def typesofpayments(request):
    if request.method == "POST":
        shopemail = request.POST.get('shopmail')
        useremail = request.POST.get('usermail')
        address = request.POST.get('address')
        invoice = request.FILES.get('invoice')

        # Save file temporarily in memory
        if invoice:
            request.session['invoice_name'] = invoice.name
            request.session['invoice_content_type'] = invoice.content_type
            request.session['invoice'] = invoice.read().decode('latin1')  # Decode bytes to string

        request.session['shopemail'] = shopemail
        request.session['usermail'] = useremail
        request.session['address'] = address

        # Retrieve order ID from session
        order_id = request.session.get('order_id')
        if order_id:
            order = get_object_or_404(Order, pk=order_id)
            # sup=get_object_or_404(SuperMarket,pk=order.supermarket)
            sup = order.supermarket
            print(sup)
            order.order_deliverysoc = sup.s_address
            order.order_deliverydec = address
            order.save()

        return render(request, 'typesofpayments.html')

    return render(request, 'orderplace.html')


from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_name = request.session.get('invoice_name')
#         invoice_content = request.session.get('invoice_content')

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_content:
#             invoice_file = ContentFile(invoice_content, invoice_name)
#             shop_email.attach(invoice_file.name, invoice_file.read(), invoice_file.content_type)
#             user_email.attach(invoice_file.name, invoice_file.read(), invoice_file.content_type)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice_name']
#         del request.session['invoice_content']

#         # Return a response
#         return render(request, 'orderplaced.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.core.files.base import ContentFile

# def cashondelivery(request):
#     if request.method == "POST":
#         # Retrieve session data
#         shopmail = request.session.get('shopemail')
#         usermail = request.session.get('usermail')
#         address = request.session.get('address')
#         invoice_name = request.session.get('invoice_name')
#         invoice_content_type = request.session.get('invoice_content_type')
#         invoice_content = request.session.get('invoice').encode('latin1')  # Encode string back to bytes

#         email_from = settings.EMAIL_HOST_USER

#         # Prepare email to shop
#         shop_subject = 'New Cash on Delivery Order'
#         shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
#         shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

#         # Prepare email to user
#         user_subject = 'Order Confirmation'
#         user_message = 'Your order has been received and will be delivered soon. Thank you!'
#         user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

#         # Attach the invoice if it exists
#         if invoice_content:
#             invoice_file = ContentFile(invoice_content, invoice_name)
#             shop_email.attach(invoice_name, invoice_content, invoice_content_type)
#             user_email.attach(invoice_name, invoice_content, invoice_content_type)

#         shop_email.send()
#         user_email.send()

#         # Clear session data
#         del request.session['shopemail']
#         del request.session['usermail']
#         del request.session['address']
#         del request.session['invoice_name']
#         del request.session['invoice_content_type']
#         del request.session['invoice']

#         # Return a response
#         return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully'})

#     return render(request, 'typesofpayments.html')


from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.base import ContentFile
from .models import Payment, Order

def cashondelivery(request):
    if request.method == "POST":
        # Retrieve session data
        shopmail = request.session.get('shopemail')
        usermail = request.session.get('usermail')
        address = request.session.get('address')
        invoice_name = request.session.get('invoice_name')
        invoice_content_type = request.session.get('invoice_content_type')
        invoice_content = request.session.get('invoice').encode('latin1')  # Encode string back to bytes

        email_from = settings.EMAIL_HOST_USER

        # Prepare email to shop
        shop_subject = 'New Cash on Delivery Order'
        shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
        shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

        # Prepare email to user
        user_subject = 'Order Confirmation'
        user_message = 'Your order has been received and will be delivered soon. Thank you!'
        user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

        # Attach the invoice if it exists
        if invoice_content:
            invoice_file = ContentFile(invoice_content, invoice_name)
            shop_email.attach(invoice_name, invoice_content, invoice_content_type)
            user_email.attach(invoice_name, invoice_content, invoice_content_type)

        shop_email.send()
        user_email.send()

        # Create payment entry
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        payment = Payment.objects.create(
            order=order,
            payment_method='Cash on Delivery',
            amount=order.total_price,  # Assuming you have a total_amount field in your Order model
            payment_status='PENDING'
        )

        # Clear session data
        del request.session['shopemail']
        del request.session['usermail']
        del request.session['address']
        del request.session['invoice_name']
        del request.session['invoice_content_type']
        del request.session['invoice']
        del request.session['order_id']

        # Return a response
        return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully with cash on delivery payment method'})

    return render(request, 'typesofpayments.html')



def onlinepayment(request):
    if request.method == "POST":
        # Retrieve session data
        shopmail = request.session.get('shopemail')
        usermail = request.session.get('usermail')
        address = request.session.get('address')
        invoice_name = request.session.get('invoice_name')
        invoice_content_type = request.session.get('invoice_content_type')
        invoice_content = request.session.get('invoice').encode('latin1')  # Encode string back to bytes

        email_from = settings.EMAIL_HOST_USER

        # Prepare email to shop
        shop_subject = 'New Cash on Delivery Order'
        shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
        shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

        # Prepare email to user
        user_subject = 'Order Confirmation'
        user_message = 'Your order has been received and will be delivered soon. Thank you!'
        user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

        # Attach the invoice if it exists
        if invoice_content:
            invoice_file = ContentFile(invoice_content, invoice_name)
            shop_email.attach(invoice_name, invoice_content, invoice_content_type)
            user_email.attach(invoice_name, invoice_content, invoice_content_type)

        shop_email.send()
        user_email.send()

        # Create payment entry
        # order_id = request.session.get('order_id')
        # order = get_object_or_404(Order, pk=order_id)
        # payment = Payment.objects.create(
        #     order=order,
        #     payment_method='Online Payment Done',
        #     amount=order.total_price,  # Assuming you have a total_amount field in your Order model
        #     payment_status='COMPLETED'
        # )

        # Clear session data
        del request.session['shopemail']
        del request.session['usermail']
        del request.session['address']
        del request.session['invoice_name']
        del request.session['invoice_content_type']
        del request.session['invoice']
        del request.session['order_id']

        # Return a response
        return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully with online payment metod'})

    return render(request, 'typesofpayments.html')


def cashoncollect(request):
    if request.method == "POST":
        # Retrieve session data
        shopmail = request.session.get('shopemail')
        usermail = request.session.get('usermail')
        address = request.session.get('address')
        invoice_name = request.session.get('invoice_name')
        invoice_content_type = request.session.get('invoice_content_type')
        invoice_content = request.session.get('invoice').encode('latin1')  # Encode string back to bytes

        email_from = settings.EMAIL_HOST_USER

        # Prepare email to shop
        shop_subject = 'New Cash on Delivery Order'
        shop_message = f'New order received:\nUser Email: {usermail}\nDelivery Address: {address}'
        shop_email = EmailMessage(shop_subject, shop_message, email_from, [shopmail])

        # Prepare email to user
        user_subject = 'Order Confirmation'
        user_message = 'Your order has been received and will be delivered soon. Thank you!'
        user_email = EmailMessage(user_subject, user_message, email_from, [usermail])

        # Attach the invoice if it exists
        if invoice_content:
            invoice_file = ContentFile(invoice_content, invoice_name)
            shop_email.attach(invoice_name, invoice_content, invoice_content_type)
            user_email.attach(invoice_name, invoice_content, invoice_content_type)

        shop_email.send()
        user_email.send()

        # Create payment entry
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        payment = Payment.objects.create(
            order=order,
            payment_method='Cash on Collect',
            amount=order.total_price,  # Assuming you have a total_amount field in your Order model
            payment_status='PENDING'
        )

        # Clear session data
        del request.session['shopemail']
        del request.session['usermail']
        del request.session['address']
        del request.session['invoice_name']
        del request.session['invoice_content_type']
        del request.session['invoice']
        del request.session['order_id']

        # Return a response
        return render(request, 'cashondeliveryordersuccces.html', {'message': 'Order placed successfully with cash on collect payment method'})

    return render(request, 'typesofpayments.html')






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from .models import DeliveryBoy, Order
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import DeliveryBoy, Order
from django.core.mail import send_mail
import random

def delivery_boy_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        
        # encrypted_password = make_password(password)
        en_password=encode_password(password)
        
        if DeliveryBoy.objects.filter(email=email).exists():
            error_message = "A user with this email already exists. Please use a different email."
            return render(request, 'deliveryboyregister.html', {'error_message': error_message})

        delivery_boy = DeliveryBoy.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=en_password,
            phone_number=phone_number,
            address=address
        )
        
        request.session['delivery_boy_id'] = delivery_boy.id
        return redirect('delivery_boy_home')
        # return redirect('packed_orders')
    else:
        # return render(request, 'signup.html')
        return render(request, 'deliveryboyregister.html')




def delivery_boy_login(request):
    error_message1 = None
    error_message2 = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            delivery_boy = DeliveryBoy.objects.get(email=email)
            print("1111111")
            stored_password= base64.b64decode(delivery_boy.password).decode('utf-8')
            print(stored_password)
            if password == stored_password:
                request.session['delivery_boy_id'] = delivery_boy.id
                # print(deli)
                # return redirect('packed_orders')
                return redirect('delivery_boy_home')
            else:
                 error_message1 = "Invalid password."
                 return render(request, 'deliveryboylogin.html', {'error_message1': error_message1})
                 
        except DeliveryBoy.DoesNotExist:
            # User with provided email does not exist, render the login page with error message
            error_message2 = "User with this email does not exist."
            return render(request, 'deliveryboylogin.html', {'error_message2': error_message2})

    else:
        # GET request, render the login page
        # return render(request, 'login.html')
    
        return render(request, 'deliveryboylogin.html')


def delivery_boy_logout(request):
    try:
        del request.session['delivery_boy_id']
        print("Aaaaaaaaaaaa")
    except KeyError:
        print("bbbbbbbbb")
        pass
        print("cccccccccc")
    return redirect('delivery_boy_login')
    # print("dddddddddd")
def get_logged_in_delivery_boy(request):
    delivery_boy_id = request.session.get('delivery_boy_id')
    if delivery_boy_id:
        return DeliveryBoy.objects.get(id=delivery_boy_id)
    return None

# def packed_orders(request):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     orders = Order.objects.filter(order_status='PACKED', delivery_boy__isnull=True)
#     return render(request, 'packed_orders.html', {'orders': orders})

# def pick_order(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, order_status='PACKED', delivery_boy__isnull=True)
    
#     if request.method == 'POST':
#         order.delivery_boy = delivery_boy
#         order.order_status = 'DISPATCHED'
#         order.save()
#         return redirect('packed_orders')
#     return render(request, 'pick_order.html', {'order': order})



from django.shortcuts import render, get_object_or_404, redirect
from .models import DeliveryBoy, Order

# def get_logged_in_delivery_boy(request):
    # delivery_boy_id = request.session.get('delivery_boy_id')
    # # Implement this function to return the logged-in delivery boy
    # return get_object_or_404(DeliveryBoy, email=request.user.email)
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Order

# def packed_orders(request):
    # delivery_boy = get_logged_in_delivery_boy(request)
    # if not delivery_boy:
    #     return redirect('delivery_boy_login')

#     orders = Order.objects.filter(order_status='PACKED', delivery_boy__isnull=True)

#     if not orders.exists():
#         messages.info(request, 'No packed orders are available at the moment.')
    
#     return render(request, 'packed_orders.html', {'orders': orders})
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from .models import Order, DeliveryBoy

def get_logged_in_delivery_boy(request):
    user = request.user
    if user.is_authenticated:
        try:
            return DeliveryBoy.objects.get(user=user)
        except DeliveryBoy.DoesNotExist:
            return None
    return None

# def get_coordinates(address):
#     geolocator = Nominatim(user_agent="myGeocoder")
#     try:
#         location = geolocator.geocode(address, timeout=30)
#         if location:
#             return (location.latitude, location.longitude)
#         else:
#             print(f"Geocoding failed for address: {address}")
#     except Exception as e:
#         print(f"Error during geocoding for address '{address}': {e}")
#     return None
import requests

# def get_coordinates(address, api_key):
#     base_url = "https://api.opencagedata.com/geocode/v1/json"
#     params = {
#         'q': address,
#         'key': api_key
#     }
#     try:
#         response = requests.get(base_url, params=params)
#         results = response.json()
#         if results['results']:
#             location = results['results'][0]['geometry']
#             return (location['lat'], location['lng'])
#         else:
#             print(f"Geocoding failed for address: {address}")
#     except Exception as e:
#         print(f"Error during geocoding for address '{address}': {e}")
#     return None


# def packed_orders(request):
#     delivery_boy_id = request.session.get('delivery_boy_id')
#     print(delivery_boy_id)
#     delivery_boy=get_object_or_404(DeliveryBoy,pk=delivery_boy_id)
#     # Implement this function to return the logged-in delivery boy
#         # return get_object_or_404(DeliveryBoy, email=request.user.email)
#     # delivery_boy = get_logged_in_delivery_boy(request)
#     # if not delivery_boy:
#     #     return redirect('delivery_boy_login')
#     # delivery_boy = get_logged_in_delivery_boy(request)
#     # if not delivery_boy:
#     #     return redirect('delivery_boy_login')
#     # delivery_boy = get_logged_in_delivery_boy(request)
#     # if not delivery_boy:
#     #     return redirect('delivery_boy_login')
#     api_key = 'b0aae460ad314b028321fc4176a4002f'
#     address = "mutharam 505184"
#     delivery_boy_location = get_coordinates(address, api_key)
#     print("*********************")
#     print(delivery_boy_location)
#     if not delivery_boy_location:
#         messages.error(request, 'Could not determine current location from address. Please check the address and try again.')
#         print("AAAAAAAAAAAAAAA")
#         return redirect('delivery_boy_login')

#     orders_within_10km = []

#     orders = Order.objects.filter(order_status='PACKED', delivery_boy__isnull=True)

#     for order in orders:
#         order_location = get_coordinates(order.order_deliverysoc,api_key)  # Assuming `address` is the field with the text address
#         print("!!!!!!!!!!!!!!!!")
#         print(order_location)
#         if order_location:
#             distance = geodesic(delivery_boy_location, order_location).km
#             if distance <= 10:
#                 orders_within_10km.append(order)

#     if not orders_within_10km:
#         messages.info(request, 'No packed orders are available within 10km at the moment.')
    
#     return render(request, 'packed_orders.html', {'orders': orders_within_10km})


from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import DeliveryBoy, Order  # Ensure you import your models correctly

def get_coordinates(address, api_key):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': address,
        'key': api_key,
        'format': 'json'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        if results['results']:
            location = results['results'][0]['geometry']
            print(location)
            return (location['lat'], location['lng'])
        else:
            print(f"No results found for address: {address}")
    except requests.RequestException as e:
        print(f"Error during geocoding for address '{address}': {e}")
    return None

def packed_orders(request):
    delivery_boy_id = request.session.get('delivery_boy_id')
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)
    api_key = 'b0aae460ad314b028321fc4176a4002f'
    address = delivery_boy.address
    print(address)
    delivery_boy_location = get_coordinates(address, api_key)

    if not delivery_boy_location:
        messages.error(request, 'Could not determine current location from address. Please check the address and try again.')
        return redirect('delivery_boy_login')

    orders_within_10km = []
    orders = Order.objects.filter(order_status='PACKED', delivery_boy__isnull=True)
    # user_id=request.session.get('user_id')
    # user=get_object_or_404(mainuser,pk=user_id)
    user_address1=request.session.get('address')
    print(user_address1)
    for order in orders:
        order_location = get_coordinates(order.order_deliverydec, api_key)
        # order_location = get_coordinates(user_address1, api_key)
        if order_location:
            distance = geodesic(delivery_boy_location, order_location).km
            if distance <= 100:  # Updated to use 10 instead of 100 for closer range
                orders_within_10km.append(order)

    if not orders_within_10km:
        messages.info(request, 'No packed orders are available within 10km at the moment.')

    return render(request, 'packed_orders.html', {'orders': orders_within_10km})


def pick_order(request, order_id):
    # delivery_boy = get_logged_in_delivery_boy(request)
    # if not delivery_boy:
    #     return redirect('delivery_boy_login')
    delivery_boy_id = request.session.get('delivery_boy_id')
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)

    order = get_object_or_404(Order, pk=order_id, order_status='PACKED', delivery_boy__isnull=True)
    
    if request.method == 'POST':
        order.delivery_boy = delivery_boy
        order.order_status = 'DISPATCHED'
        order.save()
        # return redirect('picked_order_route', order_id=order_id)
        # return redirect('packed_orders')
        return redirect('delivery_boy_home')
    return render(request, 'pick_order.html', {'order': order})

# def picked_order_route(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)
#     # s_id=order.supermarket
#     # print(s_id)
#     # shop=get_object_or_404(SuperMarket, pk=s_id)
#     # shop_address = shop.s_address
#     # user_id=order.user
#     # cust=get_object_or_404(mainuser,pk=user_id)
#     # user_address = cust.user_lname
#     supermarket = order.supermarket
#     shop_address = supermarket.s_address  # Assuming `s_address` field exists in SuperMarket

#     user = order.user
#     user_address = user.user_lname  # Assuming `user_lname` field exists in mainuser


#     return render(request, 'picked_order_route.html', {
#         'order': order,
#         'shop_address': shop_address,
#         'user_address': user_address
#     })


# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required

# # @login_required
# def picked_order_route(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)
#     # delivery_boy = request.user
#     # if not delivery_boy.is_authenticated or not delivery_boy.is_delivery_boy:
#     #     return redirect('delivery_boy_login')

#     # order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)

#     supermarket = order.supermarket
#     user = order.user

#     context = {
#         'order': order,
#         'shop_lat': supermarket.latitude,
#         'shop_lng': supermarket.longitude,
#         'user_lat': 12.11,  # Assuming `latitude` field exists in `mainuser`
#         'user_lng': 13.11  # Assuming `longitude` field exists in `mainuser`
#     }

#     return render(request, 'picked_order_route.html', context)



# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Order, SuperMarket, mainuser  # Adjust imports as needed

# def picked_order_route(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)
#     supermarket = order.supermarket
#     shop_address = supermarket.s_address  # Assuming `s_address` field exists in SuperMarket

#     user = order.user
#     user_address = user.user_lname  # Assuming `user_lname` field exists in mainuser

#     return render(request, 'picked_order_route.html', {
#         'order': order,
#         'shop_address': shop_address,
#         'user_address': user_address
#     })

# *********************
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Order, SuperMarket, mainuser  # Adjust imports as needed

# def picked_order_route(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)
#     supermarket = order.supermarket
#     shop_name = supermarket.s_name
#     shop_lat = supermarket.latitude  # Assuming `latitude` field exists in SuperMarket
#     shop_lng = supermarket.longitude  # Assuming `longitude` field exists in SuperMarket

#     user = order.user
#     user_lat ='18.483080' #user.latitude  # Assuming `latitude` field exists in mainuser
#     user_lng ='79.640740' #user.longitude  # Assuming `longitude` field exists in mainuser

#     return render(request, 'picked_order_route.html', {
#         'order': order,
#         'shop_name': shop_name,
#         'shop_lat': shop_lat,
#         'shop_lng': shop_lng,
#         'user_lat': user_lat,
#         'user_lng': user_lng
#     })
# ***********

from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, SuperMarket, mainuser  # Adjust imports as needed

def picked_order_route(request, order_id):
    delivery_boy_id = request.session.get('delivery_boy_id')
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)
    # delivery_boy = get_logged_in_delivery_boy(request)
    if not delivery_boy:
        return redirect('delivery_boy_login')

    order = get_object_or_404(Order, pk=order_id, order_status='DISPATCHED', delivery_boy=delivery_boy)
    supermarket = order.supermarket
    shop_address =order.order_deliverysoc # supermarket.s_address  # Assuming `s_address` field exists in SuperMarket
    shop_name = supermarket.s_name

    user = order.user
    # user_address = 'mutharam 505184'  # Assuming `user_lname` field exists in mainuser
    user_address1=request.session.get('address')
    print(user_address1)
    user_address=order.order_deliverydec
    
    return render(request, 'picked_order_route.html', {
        'order': order,
        'shop_address': shop_address,
        'shop_name': shop_name,
        'user_address': user_address
    })


def send_otp_emailorder(request,order):
    otp = random.randint(100000, 999999)
    request.session['otp'] = otp
    order.save()
    send_mail(
        'Your Delivery OTP',
        f'Your OTP for order delivery is {otp}.',
        settings.EMAIL_HOST_USER,
        [order.user.user_mail],
        fail_silently=False,
    )




def dispatched_orders(request):
    delivery_boy_id = request.session.get('delivery_boy_id')
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)
    # delivery_boy = get_logged_in_delivery_boy(request)
    if not delivery_boy:
        return redirect('delivery_boy_login')

    orders = Order.objects.filter(order_status='DISPATCHED', delivery_boy=delivery_boy).select_related('user', 'shop_owner', 'supermarket')
    return render(request, 'dispatched_orders.html', {'orders': orders})


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoy

# @login_required
def delivery_boy_home(request):
    delivery_boy = get_object_or_404(DeliveryBoy, id=request.session.get('delivery_boy_id'))
    return render(request, 'delivery_boy_home.html', {'delivery_boy': delivery_boy})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeliveryBoy, Order

# # @login_required
# def delivery_boy_profile(request):
#     delivery_boy = get_object_or_404(DeliveryBoy,  id=request.session.get('delivery_boy_id'))
#     return render(request, 'delivery_boy_profile.html', {'delivery_boy': delivery_boy})

# @login_required
# def delivery_boy_orders(request):
#     delivery_boy = get_object_or_404(DeliveryBoy,  id=request.session.get('delivery_boy_id'))
#     orders = Order.objects.filter(delivery_boy=delivery_boy, order_status='DELIVERED',deliveryed_date=nowdate).select_related('user', 'shop_owner', 'supermarket')
#     return render(request, 'delivery_boy_orders.html', {'orders': orders})



from django.db.models import Max

def delivery_boy_orders(request):
    delivery_boy = get_object_or_404(DeliveryBoy, id=request.session.get('delivery_boy_id'))

    # Get the most recent delivery date for the delivery boy
    latest_delivery_date = Order.objects.filter(delivery_boy=delivery_boy, order_status='DELIVERED').aggregate(latest_date=Max('delivered_date'))['latest_date']

    # Filter the orders by the most recent delivery date
    orders = Order.objects.filter(delivery_boy=delivery_boy, order_status='DELIVERED', delivered_date=latest_delivery_date).select_related('user', 'shop_owner', 'supermarket')

    return render(request, 'delivery_boy_orders.html', {'orders': orders})

# def deliver_order(request, order_id):
#     delivery_boy = get_logged_in_delivery_boy(request)
#     if not delivery_boy:
#         return redirect('delivery_boy_login')

#     order = get_object_or_404(Order, pk=order_id, delivery_boy=delivery_boy, order_status='DISPATCHED')
#     # send_otp_emailorder(order)
#     print("11111111111")
#     if request.method == 'POST':
        
#         print("222222222")
#         otp = request.POST['otp']
#         sotp=request.session.get('otp')
#         if str(sotp) == otp:
#             print("333333333")
#             order.order_status = 'DELIVERED'
#             order.payment_status='Completed'
#             order.save()
#             pay=get_object_or_404(Payment,order_id=order_id)
#             pay.payment_status='Completed'
#             pay.save()
#             return HttpResponse('Order delivered successfully')
#         else:
#             return HttpResponse('Invalid OTP')
#     else:
#         print("444444444")
#         send_otp_emailorder(request,order)
    
#     return render(request, 'delivery_order.html', {'order': order})

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Order, Payment

def deliver_order(request, order_id):
    delivery_boy_id = request.session.get('delivery_boy_id')
    delivery_boy = get_object_or_404(DeliveryBoy, pk=delivery_boy_id)

    # delivery_boy = get_logged_in_delivery_boy(request)
    if not delivery_boy:
        return redirect('delivery_boy_login')

    order = get_object_or_404(Order, pk=order_id, delivery_boy=delivery_boy, order_status='DISPATCHED')

    if request.method == 'POST':
        otp = request.POST['otp']
        sotp = request.session.get('otp')
        if str(sotp) == otp:
            order.order_status = 'DELIVERED'
            order.payment_status = 'Completed'
            order.save()
            pay = get_object_or_404(Payment, order_id=order_id)
            pay.payment_status = 'Completed'
            pay.save()
            return render(request, 'orderdelivered_success.html', {'order': order, 'total_price': pay.amount})
        else:
            return render(request, 'delivery_order.html', {'order': order, 'error_message': 'Invalid OTP. Please enter it correctly.'})
    else:
        send_otp_emailorder(request, order)
    
    return render(request, 'delivery_order.html', {'order': order})


def payment_success(request):
    return render(request,'paymentsuccess.html')





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sm_app.models import Product

@csrf_exempt
def update_price(request, product_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_price = data['price']
            product = Product.objects.get(pk=product_id)
            product.product_price = new_price
            product.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from sm_app.models import mainuser
# from django.contrib import messages

# # @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         user.user_fname = request.POST.get('user_fname')
#         user.user_lname = request.POST.get('user_lname')
#         user.user_mail = request.POST.get('user_mail')
#         user.user_dob = request.POST.get('user_dob')
#         user.user_phonenumber = request.POST.get('user_phonenumber')

#         user.save()
#         messages.success(request, 'Profile updated successfully!')
#         return redirect('profile')  # Redirect to the profile view after saving

#     return render(request, 'edit_userprofile.html', {'user': user})


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from sm_app.models import mainuser
# from django.contrib import messages

# # @login_required
# def edit_profile(request):
    
#     try:
#         user = mainuser.objects.get(user_id=request.session.get('user_id'))
#     except mainuser.DoesNotExist:
#         return redirect('profile')  # Redirect if the mainuser profile does not exist

#     if request.method == 'POST':
#         user.user_fname = request.POST.get('user_fname')
#         user.user_lname = request.POST.get('user_lname')
#         user.user_mail = request.POST.get('user_mail')
#         user.user_dob = request.POST.get('user_dob')
#         user.user_phonenumber = request.POST.get('user_phonenumber')
        
#         user.save()
#         messages.success(request, 'Profile updated successfully!')
#         return redirect('profile')  # Redirect to the profile view after saving

#     return render(request, 'edit_userprofile.html', {'user': user})

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from sm_app.models import mainuser
# from django.contrib import messages

# # @login_required
# def edit_profile(request):
#     try:
#         user = mainuser.objects.get(user_id=request.session.get('user_id'))
#     except mainuser.DoesNotExist:
#         return redirect('profile')  # Redirect if the mainuser profile does not exist

#     if request.method == 'POST':
#         new_email = request.POST.get('user_mail')
#         # Check if the new email is already taken by another user
#         if mainuser.objects.filter(user_mail=new_email).exclude(user_id=user.user_id).exists():
#             messages.error(request, 'Email already exists. Please choose a different email.')
#         else:
#             user.user_fname = request.POST.get('user_fname')
#             user.user_lname = request.POST.get('user_lname')
#             user.user_mail = new_email
#             user.user_dob = request.POST.get('user_dob')
#             user.user_phonenumber = request.POST.get('user_phonenumber')

#             user.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('profile')  # Redirect to the profile view after saving

#     return render(request, 'edit_userprofile.html', {'user': user})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sm_app.models import mainuser
from django.contrib import messages

# @login_required
def edit_profile(request):
    try:
        user = mainuser.objects.get(user_id=request.session.get('user_id'))
    except mainuser.DoesNotExist:
        return redirect('profile')  # Redirect if the mainuser profile does not exist

    if request.method == 'POST':
        user.user_fname = request.POST.get('user_fname')
        user.user_lname = request.POST.get('user_lname')
        user.user_dob = request.POST.get('user_dob')
        user.user_phonenumber = request.POST.get('user_phonenumber')

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  # Redirect to the profile view after saving

    return render(request, 'edit_userprofile.html', {'user': user})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

# def feedback_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         if name and email and message:
#             feedback = Feedback(name=name, email=email, message=message)
#             feedback.save()
#             messages.success(request, 'Thank you for your feedback!')
#             email_from = settings.EMAIL_HOST_USER
#             subject = 'FEEDBACK FORM USER'
#             message = f'User name: {name}\nUser Email: {email}\n<h1>Message:</h1>\n <b>{message}</b>'
#             sendemail = EmailMessage(subject, message, email_from, [email])
            
#             sendemail.send()
            
#             return redirect('feedback_view')
#         else:
#             messages.error(request, 'Please fill out all fields.')

#     return render(request, 'feedback.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Feedback

def feedback_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        # Redirect to login page if user is not logged in
        return redirect('login')
    if request.method == 'POST':
        
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            feedback = Feedback(name=name, email=email, message=message)
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')

            email_from = settings.EMAIL_HOST_USER
            subject = 'Feedback from User'
            html_message = f"""
            <p><strong>User Name:</strong> {name}</p>
            <p><strong>User Email:</strong> {email}</p>
            <h1>Message:</h1>
            <h3>{message}</h3>
            """
            sendemail = EmailMessage(subject, html_message, email_from, [email])
            sendemail.content_subtype = 'html'  # Set the content type to HTML
            sendemail.send()

            return redirect('feedback_view')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'feedback.html')


from django.shortcuts import render

def services_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
       
        # Redirect to login page if user is not logged in
        return redirect('login')
    return render(request, 'services.html')


# def smart(request):
#     user_id=request.session.get('user_id')
#     if user_id:
#         error_message = request.GET.get('error_message')
#         # return render(request, 'smartmart.html', {'error_message': error_message})
#         user=get_object_or_404(mainuser,pk=user_id)
#         username=user.user_fname+ user.user_lname
#         print(username)
#         return render(request, 'index.html',{'username': username,'error_message': error_message})
#     else:
#         return render(request, 'index.html')
    
def smart(request):
    user_id = request.session.get('user_id')
    if user_id:
        error_message = request.GET.get('error_message')
        welcome_spoken = request.session.get('welcome_spoken', True)
        user = get_object_or_404(mainuser, pk=user_id)
        username = user.user_fname + " " + user.user_lname
        print(username)
        return render(request, 'index.html', {
            'username': username,
            'error_message': error_message,
            'welcome_spoken': welcome_spoken
        })
    else:
        return render(request, 'index.html')

    
    
    

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Feedback

def feedback_owner(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            feedback = Feedback(name=name, email=email, message=message)
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')

            email_from = settings.EMAIL_HOST_USER
            subject = 'Feedback from User'
            html_message = f"""
            <p><strong>User Name:</strong> {name}</p>
            <p><strong>User Email:</strong> {email}</p>
            <h1>Message:</h1>
            <h3>{message}</h3>
            """
            sendemail = EmailMessage(subject, html_message, email_from, [email])
            sendemail.content_subtype = 'html'  # Set the content type to HTML
            sendemail.send()

            return redirect('feedback_view')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'feedbackshop.html')




def shopownerlogout(request):
    try:
        del request.session['owner_id']
        print("Aaaaaaaaaaaa")
    except KeyError:
        print("bbbbbbbbb")
        pass
        print("cccccccccc")
    return redirect('shopowner_login_operation')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sm_app.models import mainuser
from django.contrib import messages

# @login_required
def edit_ownerprofile(request):
    try:
        user = ShopOwner.objects.get(o_id=request.session.get('owner_id'))
    except ShopOwner.DoesNotExist:
        return redirect('shopowneronly_profile')  # Redirect if the mainuser profile does not exist

    if request.method == 'POST':
        new_email = request.POST.get('user_mail')
        # Check if the new email is already taken by another user
        if ShopOwner.objects.filter(o_mail=new_email).exclude(o_id=user.o_id).exists():
            messages.error(request, 'Email already exists. Please choose a different email.')
        else:
            user.o_name = request.POST.get('user_name')
            # user.user_lname = request.POST.get('user_lname')
            user.o_mail = new_email
            user.o_dob = request.POST.get('user_dob')
            user.o_phonenumber = request.POST.get('user_phonenumber')
            user.o_address = request.POST.get('address')

            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('shopowner_onlyprofile')  # Redirect to the profile view after saving

    return render(request, 'edit_ownerprofile.html', {'user': user})





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sm_app.models import mainuser
from django.contrib import messages

# @login_required
def edit_deliveryprofile(request):
    try:
        user = DeliveryBoy.objects.get(id=request.session.get('delivery_boy_id'))
    except DeliveryBoy.DoesNotExist:
        return redirect('delivery_boy_profile')  # Redirect if the mainuser profile does not exist

    if request.method == 'POST':
        new_email = request.POST.get('user_mail')
        # Check if the new email is already taken by another user
        if DeliveryBoy.objects.filter(email=new_email).exclude(id=user.id).exists():
            messages.error(request, 'Email already exists. Please choose a different email.')
        else:
            user.first_name = request.POST.get('user_fname')
            user.last_name = request.POST.get('user_lname')
            user.email = new_email
            # user.o_dob = request.POST.get('user_dob')
            user.phone_number = request.POST.get('user_phonenumber')
            user.address = request.POST.get('address')

            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('delivery_boy_profile')  # Redirect to the profile view after saving

    return render(request, 'edit_deliveryprofile.html', {'user': user})



# # views.py
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.template.loader import render_to_string
# from django.urls import reverse
# from .models import mainuser
# from .tokens import account_activation_token

# def password_reset_request(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         print(email)
#         try:
#             user = mainuser.objects.get(user_mail=email)
#             token = account_activation_token.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
#             mail_subject = 'Reset your password'
#             # message = render_to_string('password_reset_email.html', {
#             #     'user': user,
#             #     'reset_link': reset_link,
#             # })
#              # HTML message with the password
#             message = f"""\
#             <html>
#             <body>
#             <p>Hi { user.user_fname }</p>
#             <p>Click the link below to reset your password:</p>
#             <p><a href="{reset_link }">{ reset_link }</a></p>

#             </body>
#             </html>
#             """
#             # send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [email])
#             emailm = EmailMessage(
#                  mail_subject,
#                 message,
#                 settings.EMAIL_HOST_USER,
#                 [email]
#             )
#             emailm.content_subtype = 'html'  # Set the content to HTML
#             emailm.send(fail_silently=False)
#             return redirect('password_reset_done')
#         except mainuser.DoesNotExist:
#             return render(request, "password_reset_form.html", {'error': 'Email does not exist'})
#     return render(request, "password_reset_form.html")

# def password_reset_done(request):
#     return render(request, "password_reset_done.html")

# def password_reset_confirm(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = mainuser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
#         user = None
    
#     if user is not None and account_activation_token.check_token(user, token):
#         if request.method == "POST":
#             new_password = request.POST.get("new_password")
#             en_password = encode_password(new_password)
#             user.user_password = en_password  # You should hash the password before saving
#             user.save()
#             return redirect('password_reset_complete')
#         return render(request, 'password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
#     else:
#         return redirect('password_reset_invalid')

# def password_reset_complete(request):
#     return render(request, "password_reset_complete.html")

# def password_reset_invalid(request):
#     return render(request, "password_reset_invalid.html")
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .models import mainuser
from .tokens import account_activation_token
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = mainuser.objects.get(user_mail=email)
            signer = TimestampSigner()
            token = signer.sign(account_activation_token.make_token(user))
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
            mail_subject = 'Reset your password'
            message = f"""\
            <html>
            <body>
            <p>Hi { user.user_fname }</p>
            <p>Click the link below to reset your password:</p>
            <p><a href="{reset_link }">{ reset_link }</a></p>
            </body>
            </html>
            """
            emailm = EmailMessage(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            emailm.content_subtype = 'html'
            emailm.send(fail_silently=False)
            return redirect('password_reset_done')
        except mainuser.DoesNotExist:
            return render(request, "password_reset_form.html", {'error': 'Email does not exist'})
    return render(request, "password_reset_form.html")

def password_reset_done(request):
    return render(request, "password_reset_done.html")

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = mainuser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
        user = None
    
    if user is not None:
        signer = TimestampSigner()
        try:
            # Check if token is valid and not expired (2-minute limit)
            original_token = signer.unsign(token, max_age=300)  # 120 seconds = 2 minutes
            if account_activation_token.check_token(user, original_token):
                if request.method == "POST":
                    new_password = request.POST.get("new_password")
                    user.user_password = new_password  # Hash the password before saving
                    user.save()
                    return redirect('password_reset_complete')
                return render(request, 'password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
        except (SignatureExpired, BadSignature):
            return redirect('password_reset_invalid')
    return redirect('password_reset_invalid')

def password_reset_complete(request):
    return render(request, "password_reset_complete.html")

def password_reset_invalid(request):
    return render(request, "password_reset_invalid.html")




# def toggle_product_status(request):
#     if request.method == 'POST':
#         product_id=request.POST['product_id']
#         product = get_object_or_404(Product, pk=product_id)
#         product.product_status = not product.product_status
#         product.save()
#         return JsonResponse({'success': True, 'new_status': product.product_status})
#     return JsonResponse({'success': False}, status=400)
# views.py
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Product

def toggle_product_status(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.product_staus = not product.product_staus
    product.save()
    return redirect('checkboxproducts')
    # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


    