from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): 
    return render(request, 'home/home.html')
    # return HttpResponse('This is home ')

def contact(request):
    # return HttpResponse("This is contact")
    return render(request, 'home/contact.html')

def about(request): 
    # return HttpResponse('This is about')
    return render(request, 'home/about.html')