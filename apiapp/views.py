from django.shortcuts import render
from rest_framework.views import APIView
from . models import Student
from . serilizers import Studentserilizer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
def insert(request):
    if request.method == "GET":
        return render(request,'input.html')
    elif request.method == "POST":
        n = request.POST['t1']
        c = request.POST['t2']
        m = request.POST['t3']
        obj = Student(name=n,course=c,marks=m)
        obj.save()
        return HttpResponse('data submitted successfully')

class Studentview(APIView):
    def get(self,request):
        student = Student.objects.all()
        serilizer = Studentserilizer(student,many=True)
        return Response(serilizer.data)
