from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from basic.models import Users

from django.forms.models import model_to_dict
import json
import traceback
from basic.models import Movie
from basic.models import Movie_review
from django.contrib.auth.hashers import make_password,check_password



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
# def health(request):
#     try:
#         with connection.cursor() as c:
#             c.execute("SELECT 1")
#         return JsonResponse({"status":"ok","db":"connected"})
#     except Exception as e:
#         return JsonResponse({"status":"error","db":str(e)})  

def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        print(" Database connected successfully")  # <-- prints in terminal
        return JsonResponse({"status": "ok", "db": "connected"})
    except Exception as e:
        print(f" Database connection error: {e}")  # <-- prints in terminal
        return JsonResponse({"status": "error", "db": str(e)})


# Add student view // creating using
@csrf_exempt
def addStudent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  #load and send the data through json format only
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
            #creating data into the table
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


def job1(request):
    return JsonResponse({"message":"u have successfully applied for job1"})
def job2(request):
    return JsonResponse({"message":"u have successfully applied for job2"})




#creating account view and implementing some rules for follow
#username---user name mandatory
# should be unique,
#  must 3-2- chars,
#  cannot starts with or end swith .,_,
# cannot have .. 0r__ and 
# no spaces ,  so follow middlewares
@csrf_exempt
def signUp(request):
    if request.method=="POST":#getting data
        data = json.loads(request.body) #send the data for loading data #whenever data getting it
        print(data)
        #insrt data into the table
        #users is the model name and import from models and set the data using by postman
        user = Users.objects.create(
                username=data.get('username'),
                email=data.get('email'),
                password=make_password(data.get('password')) #hashed and shown in a table
            )

    return JsonResponse({"status":"success"},status=200) #so its printing in terminals and set the data


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = request.POST
        print(data)

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse(
                {"status": "failure", "message": "username and password required"},
                status=400
            )

        try:
            user = Users.objects.get(username=username)

            if check_password(password, user.password):
                return JsonResponse({"status": "successfully logged in"}, status=200)
            else:
                return JsonResponse(
                    {
                        "status": "failure",
                        "suggestion": "password incorrect, want to reset?"
                    },
                    status=400
                )

        except Users.DoesNotExist:
            return JsonResponse(
                {"status": "failure", "message": "user not found"},
                status=400
            )

    return JsonResponse({"error": "POST method only"}, status=405)




# from django.http import JsonResponse, QueryDict
# from django.views.decorators.csrf import csrf_exempt
# from .models import Users

# @csrf_exempt
# def changepassword(request):
#     if request.method == "PUT":

#         # Parse form-data from PUT request
#         data = QueryDict(request.body)
#         print(data)

#         ref_id = data.get("id")
#         new_password = data.get("password")

#         existing_user = Users.objects.get(id=ref_id)
#         existing_user.password = new_password
#         existing_user.save()

#         updated_password = Users.objects.filter(id=ref_id).values().first()

#         return JsonResponse(
#             {
#                 "status": "password changed successfully",
#                 "updated password is": updated_password
#             },
#             status=200
#         )

@csrf_exempt
def changepassword(request):
    if request.method=="PUT":
        data=json.loads(request.body)
        print(data)
        ref_id=data.get("id")
        new_password=data.get("password")
        existing_user=Users.objects.get(id=ref_id)

        #convert to new password
        hashed_password=make_password(new_password)
        existing_user.password=hashed_password
        existing_user.save()
        updated_password=Users.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"password changes successfully","updated password is":updated_password},status=200)
























#movie purpose
@csrf_exempt
def movie(request):
    if request.method=="POST":#getting data
        # data = json.loads(request.body) #send the data for loading data #getting the data
        data=request.POST #when  send the data through form data
        print(data)
        #insrt data into the table
        #users is the model name and import from models and set the data using by postman
        user = Movie.objects.create(
                movie_name=data.get('movie_name'),
                date=data.get('date'),
                rating=data.get('rating')
            )

    return JsonResponse({"status":"success"},status=200 ) #so its printing in terminals and set the data
# @csrf_exempt
# def movie(request):
#     if request.method == "POST":
#         data = json.loads(request.body) #we getting the data
#         rating_number = int(data.get("rating"))
#         ratingg = "*" * rating_number
#         data["rating"] = ratingg

#         print("POST Data:", data)       

#         user = Movie.objects.create(
#             movie_name=data.get('movie_name'),
#             date=data.get('date'),
#             rating=rating_number     
#         )

#         return JsonResponse({
#             "status": "success",
#             "rating": ratingg          
#         }, status=200)

#     return JsonResponse({"error": "Invalid request method"}, status=400)



#all crud methods for movie_review
@csrf_exempt
def movies_review(request):
    if request.method=="POST":#getting data
        data = json.loads(request.body) #send the data for loading data
        
        #insrt data into the table
        #users is the model name and import from models and set the data using by postman
        user = Movie_review.objects.create(
                movie_name=data.get('movie_name'),
                date=data.get('date'),
                rating=data.get('rating'),
                budget=data.get('budget')
            )
        print({"movie_name": user.movie_name,"release_date":user.date,"rating":user.rating,"movie_budget":user.budget})
        return JsonResponse(
        {"status": "success", "data": data},
        status=200,
        safe=False
    )
    if request.method == "GET":
        result=tuple(Movie_review.objects.values())
        print(result)
        return JsonResponse(
        {"status": "success", "data": result},
        status=200,
        safe=False
    )
    # if request.method == "GET":
    #     result=tuple(Movie_review.objects.values())
    #     print(result)
    #     return JsonResponse(
    #     {"status": "success", "data": result},
    #     status=200,
    #     safe=False
    # )
    elif request.method=="DELETE":
           data=json.loads(request.body) #getting objects
           ref_id=data.get("id")#getting id
           to_be_delete=Movie_review.objects.get(id=ref_id)
         

           #shown in terminal before deleting
           get_del_data=Movie_review.objects.filter(id=ref_id).values().first()

           to_be_delete.delete() 
           return JsonResponse(
           {"status": "success", "data": get_del_data},
           status=200,
           safe=False
    )  

    elif request.method=="PUT":
         data=json.loads(request.body)
         ref_id=data.get("id")#getting email
         date=data.get("date")#getting email
         exsiting_movie=Movie_review.objects.get(id=ref_id)#fetched the object as per the id #checking
        #  print(exsiting_student)
         exsiting_movie.date=date#updating the new email
         exsiting_movie.save()#commit changes

        #getting updating value
         updated_data=Movie_review.objects.filter(id=ref_id).values().first()
        #  print(updated_data)
         return JsonResponse(
        {"status": "success", "data": updated_data},
        status=200,
        safe=False
         )

    return JsonResponse({"status":"success",},status=200)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Movie_review
# import json

# @csrf_exempt
# def movies_review(request):

#     # ------------------- CREATE (POST) -------------------
#     if request.method == "POST":
#         data = json.loads(request.body)

#         # Conditions
#         if not data.get("movie_name"):
#             return JsonResponse({"error": "Movie name is required"}, status=400)

#         if Movie_review.objects.filter(movie_name=data["movie_name"]).exists():
#             return JsonResponse({"error": "Movie already exists"}, status=400)

#         if data.get("rating", 0) > 5 or data.get("rating", 0) < 1:
#             return JsonResponse({"error": "Rating must be between 1 and 5"}, status=400)

#         if data.get("budget", 0) <= 0:
#             return JsonResponse({"error": "Budget must be positive"}, status=400)

#         movie = Movie_review.objects.create(
#             movie_name=data["movie_name"],
#             date=data.get("date"),
#             rating=data.get("rating"),
#             budget=data.get("budget")
#         )

#         return JsonResponse({"message": "Movie created", "id": movie.id}, status=201)

#     # ------------------- READ (GET) -------------------
#     if request.method == "GET":
#         movies = list(Movie_review.objects.values())
#         return JsonResponse({"data": movies}, status=200)

#     # For PUT, PATCH, DELETE → load body
#     try:
#         data = json.loads(request.body)
#     except:
#         data = {}

#     # ------------------- DELETE -------------------
#     if request.method == "DELETE":
#         movie_id = data.get("id")

#         if not movie_id:
#             return JsonResponse({"error": "ID is required"}, status=400)

#         try:
#             movie = Movie_review.objects.get(id=movie_id)
#         except Movie_review.DoesNotExist:
#             return JsonResponse({"error": "Movie not found"}, status=404)

#         movie.delete()
#         return JsonResponse({"message": "Movie deleted"}, status=200)

#     # ------------------- FULL UPDATE (PUT) -------------------
#     if request.method == "PUT":
#         movie_id = data.get("id")

#         try:
#             movie = Movie_review.objects.get(id=movie_id)
#         except Movie_review.DoesNotExist:
#             return JsonResponse({"error": "Movie not found"}, status=404)

#         movie.movie_name = data.get("movie_name", movie.movie_name)
#         movie.date = data.get("date", movie.date)
#         movie.rating = data.get("rating", movie.rating)
#         movie.budget = data.get("budget", movie.budget)
#         movie.save()

#         return JsonResponse({"message": "Movie updated"}, status=200)

#     # ------------------- PARTIAL UPDATE (PATCH) -------------------
#     if request.method == "PATCH":
#         movie_id = data.get("id")

#         try:
#             movie = Movie_review.objects.get(id=movie_id)
#         except Movie_review.DoesNotExist:
#             return JsonResponse({"error": "Movie not found"}, status=404)

#         # Update only provided fields
#         if "movie_name" in data:
#             movie.movie_name = data["movie_name"]

#         if "rating" in data:
#             if data["rating"] < 1 or data["rating"] > 5:
#                 return JsonResponse({"error": "Rating must be 1–5"}, status=400)
#             movie.rating = data["rating"]

#         if "budget" in data:
#             if data["budget"] <= 0:
#                 return JsonResponse({"error": "Budget must be positive"}, status=400)
#             movie.budget = data["budget"]

#         if "date" in data:
#             movie.date = data["date"]

#         movie.save()
#         return JsonResponse({"message": "Partial update done"}, status=200)

#     return JsonResponse({"error": "Method not allowed"}, status=405)




#hashing
@csrf_exempt
def check(request):
    hashed="pbkdf2_sha256$870000$XB2KlpxRJXJ7KmhhOU5FzN$hqFxqTHJaqHHMkkgiVxpPA78q23f6hOgc9r9p1eWy+4="
    ipdata=request.POST 
    print(ipdata)
    # hashed=make_password(ipdata.get("ip"))
    x=check_password(ipdata.get("ip"),hashed)
    print(x)
    return JsonResponse({"status":"success","data":x},status=200)









