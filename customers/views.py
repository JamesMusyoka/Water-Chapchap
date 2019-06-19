from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.views import generic
from .models import customer
from notification.models import Notification
from sendsms import api


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
    api.send_sms(body='I can haz txt', from_phone='+254774100224', to=['+254776500221'])


def loggedin(request):
    n = notification.objects.filter(user=request.user, viewed=False)
    return render('login.html', {'full_name': request.user.username, 'notifications':n})

def faqs(request):
    return render(request, 'faqs.html')