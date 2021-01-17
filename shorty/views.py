from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import  UrlLink

from .tokenGenerator import  Shortner

s = Shortner()

def index(request):
    token = ""
    if request.method == 'POST':
        longUrl = request.POST['longUrl']
        newLink = UrlLink(short_url=s.generate(),long_url=longUrl)
        newLink.save()
        token = newLink.short_url

    return render(request,"shorty/index.html",{'token':token})

def urlRedirect(request,token):
    longUrl = UrlLink.objects.get(short_url=token)
    return redirect(longUrl.long_url)
