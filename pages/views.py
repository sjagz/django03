from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    return render(request, 'dinner.html')

def greeting(request, name):
    return render (request , 'greeting.html', {'name':name})


def template_language(request):
    menus = ['짜장면','짬뽕','볶음밥','양장피']
    message = ['사과','파인에플','망고','딸기']
    my_sentence='life is short, you need python'
    datetimenow=datetime.now()
    empty_list=[]

    context = {
        'menus':menus,
        'message':message,
        'my_sentence':my_sentence,
        'datetimenow':datetimenow,
        'empty_list':empty_list,
    }
    return render (request , 'template_language.html',context)

def birth(request):
    datetimenow = datetime.now()
    birth='06-04'

    context ={
        'birth': birth,
        'datetimenow': datetimenow,

    }
    return render(request, 'birth.html', context)


def throw(request):
    return render(request, 'throw.html')


def throw_utilities(request):
    return render(request, 'throw_utilities.html')


def catch(request):
    message =request.GET.get('message')
    context ={"message":message}
    return render(request, 'catch.html' , context)

def static_example(request):


    return render(request, 'static_example.html')

