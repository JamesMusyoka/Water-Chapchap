from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.views import generic
from .models import customer
from djexmo import send_message
from django.contrib.messages.views import SuccessMessageMixin
# import package
import africastalking

import nexmo

client = nexmo.Client(key='04893f7a', secret='qpiRMW4Elv3AChe2')


responseData = client.send_message(
    {
        "from": "Water-chapchap",
        "to": '254708608180',
        "text": "You have successfully ordered your product, we will deliver it into your door step",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# Initialize SDK
username = "Water-chapchap"    # use 'sandbox' for development in the test environment
api_key = "fed884a8601206cd3bdb451518dafa9f1ac1e551c3a7dc7e70e0827c3303f0ca"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS
   


def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method =='POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                send_activation_email(user, current_site, to_email)
                return HttpResponse('Confirm your email address to complete registration')
        else:
            form = SignupForm()
            return render(request,'registration/signup.html',{'form':form})

# Create your views here.
def home(request):
    return render(request,'home.html')



class Customer_Create(SuccessMessageMixin,generic.CreateView):
    model=customer
    fields=['name', 'Street_address', 'Litres', 'phone']
    success_url = '/order/'
    def get_success_message(self, cleaned_data):
        return "Thank you for your order, we are connecting you with our supplier who will be contacting you shortly..."



def faqs(request):
    return render(request, 'faqs.html')