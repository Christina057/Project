from django.shortcuts import render

def hello_world(request):
    return render(request, 'myapp/hello_world.html')

def greet(request):
    return render(request, 'myapp/greet.html')
