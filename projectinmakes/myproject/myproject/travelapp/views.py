from django.shortcuts import render
from django.http import HttpResponse

from travelapp.models import place, person


# Create your views here.
def demo(request):
   obj=place.objects.all()
   per=person.objects.all()

   return render(request,'index.html',{'result':obj,'persons':per})

def about(request):
   return render(request,template_name='about.html')
# def addition(request):
#    a=int(request.GET('num1'))
#    b=int(request.GET('num2'))
#    res=a+b
#    return render(request,'addition.html',{'result':res})