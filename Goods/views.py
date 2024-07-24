from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.forms import UserCreationForm

def main(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    navbar_info = models.NavbarInfo.objects.get()
    footer_info = models.FooterInfo.objects.get()

    context = {}
    context['banners'] = banners
    context['navbar_info'] = navbar_info
    context['footer_info'] = footer_info

    return render(request, 'index.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})
