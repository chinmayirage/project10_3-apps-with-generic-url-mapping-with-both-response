from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app3_string(request):
    return HttpResponse('This is my app3_string')
def app3_htmlpage(request):
    return render(request,'app3_htmlpage.html')