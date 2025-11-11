from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.forms.models import model_to_dict
import json
import traceback


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
    
    
    if request.method == "GET":
        try:
            # Read query parameters (from Postman URL)
            student_id = request.GET.get("id")           # ?id=1
            min_age = request.GET.get("min_age")         # ?min_age=20
            max_age = request.GET.get("max_age")         # ?max_age=25
            unique_age = request.GET.get("unique_age")   # ?unique_age=true
            order_name = request.GET.get("order_name")   # ?order_name=true
            count = request.GET.get("count")             # ?count=true

            #  Specific record by ID
            if student_id:
                res = Student.objects.filter(id=student_id).values().first()
                print(" Specific record fetched:", res)
                return JsonResponse({"status": "ok", "data": res}, status=200)

            #  Filter by age >= value
            elif min_age:
                results = list(Student.objects.filter(age__gte=min_age).values())
                print(f" Students with age >= {min_age}:", results)
                return JsonResponse({"status": "ok", "data": results}, status=200)

            # Filter by age <= value
            elif max_age:
                results = list(Student.objects.filter(age__lte=max_age).values())
                print(f" Students with age <= {max_age}:", results)
                return JsonResponse({"status": "ok", "data": results}, status=200)

            #  Unique ages
            elif unique_age:
                results = list(Student.objects.values("age").distinct())
                print(" Unique ages:", results)
                return JsonResponse({"status": "ok", "data": results}, status=200)

            # Order by name
            elif order_name:
                results = list(Student.objects.order_by("name").values())
                print("Records ordered by name:", results)
                return JsonResponse({"status": "ok", "data": results}, status=200)

            #  Count total students
            elif count:
                total = Student.objects.count()
                print(" Total number of students:", total)
                return JsonResponse({"status": "ok", "data": total}, status=200)

            #  Default: Get all records
            else:
                results = list(Student.objects.values())
                print("All records:", results)
                return JsonResponse({"status": "ok", "data": results}, status=200)

        except Exception as e:
            print(" Error in GET method:", e)
            return JsonResponse({"status": "error", "message": str(e)}, status=400)


    #crud operations
    # #get all records
    # elif request.method=="GET":
    #     result=tuple(Student.objects.values())
    #     print(result)
    
    #     return JsonResponse({"status":"ok","data":result},status=200)
    
    # #get a specific record by id
    # elif request.method=="GET":
    #  res=Student.objects.get(id=1) 
    #  data=model_to_dict(res)
    #  #in terminal
    #  updated_data=Student.objects.filter(id=1).values().first()
    #  return JsonResponse({"status specific record ":"ok","data":updated_data},status=200)

        #filter by age >=20
    
    
    # elif request.method=="GET":
    #  data=json.loads(request.body)
    #  ref_age=data.get("age")
    #  results=list(Student.objects.filter(age__gte=ref_age).values())
    
    #  return JsonResponse({"status_specific_record": "ok", "data": results}, status=200)
    #  return JsonResponse({"status":"ok","data":results},status=200)
  
    
    # # #filter lte <25 age methods
    # elif request.method=="GET":
    #  data=json.loads(request.body)
    #  ref_age=data.get("age")
    #  results=list(Student.objects.filter(age__lte=ref_age).values())

    #  return JsonResponse({"status_specific_record": "ok", "data": results}, status=200)
    
    # #unique ages 
    # elif request.method=="GET":
     
     
    #  results=list(Student.objects.values('age').distinct())
    #  return JsonResponse({"status":"ok","data":results},status=200)
    

    # #order by name
    # elif request.method=="GET":
      
    #     results=list(Student.objects.order_by('name').values())
    #     return JsonResponse({"status":"ok","data":results},status=200)
    

        # get unique ages


     # count total students
    elif request.method=="GET":
        results=Student.objects.count()
        return JsonResponse({"status":"ok","data":results},status=200)


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











#get purpose all condition based function
#all recors
#specific record
#greater age by 25
#less than 25
#order by name
#count of all records


@csrf_exempt
def student_api(request):
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
    # if request.method == "GET":
    #     try:
    #         # Read query parameters (from Postman URL)
    #         student_id = request.GET.get("id")           # ?id=1
    #         min_age = request.GET.get("min_age")         # ?min_age=20
    #         max_age = request.GET.get("max_age")         # ?max_age=25
    #         unique_age = request.GET.get("unique_age")   # ?unique_age=true
    #         order_name = request.GET.get("order_name")   # ?order_name=true
    #         count = request.GET.get("count")             # ?count=true

    #         #  Specific record by ID
    #         if student_id:
    #             res = Student.objects.filter(id=student_id).values().first()
    #             print(" Specific record fetched:", res)
    #             return JsonResponse({"status": "ok", "data": res}, status=200)

    #         #  Filter by age >= value
    #         elif min_age:
    #             results = list(Student.objects.filter(age__gte=min_age).values())
    #             print(f" Students with age >= {min_age}:", results)
    #             return JsonResponse({"status": "ok", "data": results}, status=200)

    #         # Filter by age <= value
    #         elif max_age:
    #             results = list(Student.objects.filter(age__lte=max_age).values())
    #             print(f" Students with age <= {max_age}:", results)
    #             return JsonResponse({"status": "ok", "data": results}, status=200)

    #         #  Unique ages
    #         elif unique_age:
    #             results = list(Student.objects.values("age").distinct())
    #             print(" Unique ages:", results)
    #             return JsonResponse({"status": "ok", "data": results}, status=200)

    #         # Order by name
    #         elif order_name:
    #             results = list(Student.objects.order_by("name").values())
    #             print("Records ordered by name:", results)
    #             return JsonResponse({"status": "ok", "data": results}, status=200)

    #         #  Count total students
    #         elif count:
    #             total = Student.objects.count()
    #             print(" Total number of students:", total)
    #             return JsonResponse({"status": "ok", "data": total}, status=200)

    #         #  Default: Get all records
    #         else:
    #             results = list(Student.objects.values())
    #             print("All records:", results)
    #             return JsonResponse({"status": "ok", "data": results}, status=200)

    #     except Exception as e:
    #         print(" Error in GET method:", e)
    #         return JsonResponse({"status": "error", "message": str(e)}, status=400)



