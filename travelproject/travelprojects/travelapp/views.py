from django.shortcuts import render
from .models import Place

# Create your views here
from django.http import HttpResponse


def demo(request):
    # return HttpResponse("Hello World")
    # name = "India"
    obj=Place.objects.all()
    return render(request, 'index.html',{'result':obj})




    # return render(request, 'index.html', {'obj': name})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
# # def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse("print hello")
