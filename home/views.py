from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
   
    peoples = [
       {'name' : 'Abhijeet', 'age' : 26},
       {'name' : 'Rohan Sharma', 'age' : 16},
       {'name' : 'Dev Athwnai', 'age' : 19},
       {'name' : 'Virat Kohli', 'age' : 32}
   ]
    context = {'page' : 'home'}
    vegetables = ['Pumpkin','Tomato','Potato']
   
    return render(request, "home\index.html",context ={'peoples' : peoples,'vegetables' : vegetables, 'page' : 'home'})

def about(request):
    context = {'page' : 'about'}

    return render(request, "home\\about.html",context=context)


def contact(request):
    context = {'page'  : 'contact'}

    return render(request,"home\contact.html",
    context=context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a Success Page.<h1>")