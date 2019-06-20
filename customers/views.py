from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.views import generic
from .models import customer
from djexmo import send_message
# import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "fed884a8601206cd3bdb451518dafa9f1ac1e551c3a7dc7e70e0827c3303f0ca"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254774100224"])
print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+254774100224"], callback=on_finish)    


def signup(request):
    if request.user.is_authenticated():
        return redirect('customers.html')
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



class Customer_Create(generic.CreateView):
    model=customer
    fields=['name', 'Street_address', 'Litres', 'phone']
    success_url = '/order/'
def faqs(request):
    return render(request, 'faqs.html')