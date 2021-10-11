from django.shortcuts import render,redirect
from .models import Urls
from django.http import HttpResponse
import uuid

def homepage(request):
    return render(request,'index.html')


def create(request):
    if request.method=='POST':
        link = request.POST['link']
        nuid = str(uuid.uuid4())[:5]
        new_url = Urls(link=link,uid=nuid)
        new_url.save()
        return HttpResponse(nuid)
        
def go(request, pk):
    url_details = Urls.objects.get(uid=pk)
    return redirect(url_details.link)


    