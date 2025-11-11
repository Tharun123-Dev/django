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
        result=tuple(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
    #updating purpose
    elif request.method=="PUT":
         data=json.loads(request.body)
         ref_id=data.get("id")#getting email
         new_email=data.get("email")#getting email
         exsiting_student=Student.objects.get(id=ref_id)#fetched the object as per the id
        #  print(exsiting_student)
         exsiting_student.email=new_email#updating the new email
         exsiting_student.save()#commit changes

        #getting updating value
         updated_data=Student.objects.filter(id=ref_id).values().first()
        #  print(updated_data)
         
         return JsonResponse({"status":"data updated succesfully","uploaded_data":updated_data},status=200)
    elif request.method=="DELETE":
           data=json.loads(request.body) #getting objects
           ref_id=data.get("id")#getting id
           to_be_delete=Student.objects.get(id=ref_id)
         

           #shown in terminal before deleting
           get_del_data=Student.objects.filter(id=ref_id).values().first()

           to_be_delete.delete()

         
           return JsonResponse({"status":"success","message":"student record delete successfully","deleted_data":get_del_data},status=200)
    return JsonResponse({"error": "use POST method"}, status=400)

