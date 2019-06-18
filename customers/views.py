from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.user.is_authenticated():
        return redirect('index.html')
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
