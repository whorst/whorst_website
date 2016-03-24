from django.shortcuts import render


'''
A view is a place where we put the "logic" of our application.
It will request information from the model you created before and pass it to a template.
'''
# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})
    #The above code will look for an html file called home.html
    #A Template will next be created

def projects(request):
    return render(request, 'website/projects.html', {})

def coursework(request):
    return render(request, 'website/coursework.html', {})

def hobbies(request):
    return render(request, 'website/hobbies.html', {})

def contact(request):
    return render(request, 'website/contact.html', {})


