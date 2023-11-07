from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jampandu(request):
    return HttpResponse('hii how r u')
def virat(request):
    return HttpResponse('<h1 style=color:red;background-color:yellow;,width=200px><marquee>king</h1></marquee>')
def king(request):
    return HttpResponse('<h1 style= color:blue;background-color:yellow;<marquee> happy birthday king kohli</h1></marquee>')