# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pyrebase

# Create your views here.
config = {
    'apiKey': "AIzaSyCeDQEeCXSO6EQr9mIRlhc6-BMeZPqOt_0",
    'authDomain': "protus-419b2.firebaseapp.com",
    'databaseURL': "https://protus-419b2.firebaseio.com",
    'projectId': "protus-419b2",
    'storageBucket': "protus-419b2.appspot.com",
    'messagingSenderId': "889330218657",
    'appId': "1:889330218657:web:96409da1ebc27303"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
def singIn(request):
    return render(request, "Signin.html")
def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"Signin.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})