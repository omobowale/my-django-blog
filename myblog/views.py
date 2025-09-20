from django.shortcuts import render, redirect
from post.forms import RegistrationForm
from django.contrib.auth import login

def aboutus(request):
    return render(request, 'aboutus.html', {})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user) # auto login
            return redirect('posts_list')
        
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {"form": form})
        