from django.shortcuts import render,HttpResponse

# Create your views here.
def Portfolio(request):
    return render(request,'home1/p.html')



def DjangoProjects(request):
    
    return render(request,'home1/django.html')


def Contact(request):
    
    return render(request,'home1/contact.html')