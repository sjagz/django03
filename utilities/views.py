from django.shortcuts import render

# Create your views here.
def catch(request):
    message =request.GET.get('message')
    context ={"message":message}
    return render(request, 'utilities/catch_utilities.html' , context)

def utilities(request):

    return render(request, 'utilities/index.html')