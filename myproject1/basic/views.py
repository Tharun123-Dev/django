from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json


# Create your views here.
def sample(request):
    return  HttpResponse("hello world")
def sample1(request):
    return HttpResponse("hello nani")

def sampleinfo(request):
    data={'name':'shannu','age':23,'city':'hyd'}
    # data=['resul':[1,2,3,4]]
    return JsonResponse(data)

def dynamicResponse(request):
    name=request.GET.get("name",'tharun')
    city=request.GET.get("city",'hyd')
    return HttpResponse(f"hello {name} from {city}")
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})  


# Add student view // creating using
@csrf_exempt
def addStudent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student.objects.create(
                name=data.get('name'),
                age=data.get('age'),
                email=data.get('email')
            )
            return JsonResponse({"status": "success", 'id': student.id}, status=200)
        
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    #crud operations
    elif request.method=="GET":
        return JsonResponse({"req0":"get method requested"},status=200)
    elif request.method=="PUT":
         return JsonResponse({"req0":"put method requested"},status=200)
    elif request.method=="DELETE":
         return JsonResponse({"req0":"delete method requested"},status=200)
    return JsonResponse({"error": "use POST method"}, status=400)


    
