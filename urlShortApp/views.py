from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import ShortUrl
import random, string

# Create your views here.


def generateUrl():
    while(True):
        short_url =''.join(random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(10))
        if(not (ShortUrl.objects.filter(shortUrl=short_url).exists())):
           return short_url

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("urlInput")
        short_url = generateUrl()
        ShortUrl.objects.create(mainUrl=long_url,shortUrl=short_url)
        messages.success(request, short_url)
        return redirect("/")

    return render(request,"home.html") #need to be in templates folder 

def redirectShortUrl(request,code):
    check = get_object_or_404(ShortUrl,shortUrl=code)
    check.accessed += 1
    check.save()
    return redirect(check.mainUrl)




    
