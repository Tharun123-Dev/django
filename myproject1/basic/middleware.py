
# import json
from django.http import HttpResponse
from django.http import JsonResponse
import re,json
from basic.models import Users
class basicMiddleware: #class in camel case
    def __init__(self,get_response):
        self.get_response=get_response #automatically give the response #start the server then it is run

    def __call__(self, request): #call the make the request  #run at giving requests
        print(request,"hello")
        if(request.path=="/Student"): #for specific path for url
           print(request.method,"method") #after hello--then method shown
           print(request.path) #then path also aftrer giving the response
        elif(request.path=="/greet"):
            print(request.method,"greet")
            print(request.path)
        elif(request.path=="/hel"):
            print(request.method,"health")
            print(request.path)


        response=self.get_response(request)#after that hello goto view the give response
        return response                    
    
# class basicMiddleware: #class in camel case
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__   (self,request):
#         data=json.loads(request.body)
#         username=data.get("username") 
#         email=data.get("email")
#         dob=data.get("dob")
#         password=data.get("pswd")
        # check the username rules with regex
        # check the email rules with regex
        # check dob rules with regex
        # check the password with regex

# import json
# import re
# from django.http import JsonResponse

# class BasicMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Only validate for POST requests (to avoid errors on GET)
#         if request.method == "POST":
#             try:
#                 data = json.loads(request.body.decode("utf-8"))

#                 username = data.get("username")
#                 email = data.get("email")
#                 dob = data.get("dob")
#                 password = data.get("pswd")

#                 #  Username rule: only letters and numbers, 3–15 chars
#                 if not re.match(r'^[A-Za-z0-9]{3,15}$', username):
#                     print(" Invalid Username")
#                     return JsonResponse({"error": "Invalid username format"})

#                 #  Email rule: must follow basic email format
#                 if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
#                     print(" Invalid Email")
#                     return JsonResponse({"error": "Invalid email format"})

#                 #  DOB rule: YYYY-MM-DD format
#                 if not re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
#                     print("Invalid DOB")
#                     return JsonResponse({"error": "Invalid date of birth format (YYYY-MM-DD)"})

#                 # Password rule: at least 8 chars, 1 uppercase, 1 number, 1 special char
#                 if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
#                     print(" Weak Password")
#                     return JsonResponse({"error": "Password must be at least 8 chars with uppercase, number, and special char"})

#                 print(" All fields are valid!")

#             except json.JSONDecodeError:
#                 print("Invalid JSON data")
#                 return JsonResponse({"error": "Invalid JSON data"})

#         # Continue the request if all checks passed
#         response = self.get_response(request)
#         return response
    

#creating middle wares
class sscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            if( ssc_result != "True"):
                return JsonResponse({"error": "u should qualify atleast ssc for applying this job"},status=400)
        return self.get_response(request)



class MedicalFitMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=request.GET.get("medically_fit")
            if( medical_fit_result !='True'):
                return JsonResponse({"error": "u re not medically fit for applying this job"},status=400)
        return self.get_response(request)
    

class AgeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            Age_checker=int(request.GET.get("age",17))
            if ((Age_checker>=25 and Age_checker<18)):
                return JsonResponse({"error":"Age must in between 18 and 25"},status=400)
        return self.get_response(request)

#creating account for followed rules
  
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        if (request.path=="/signup/"):
            data=json.loads(request.body)
            username=data.get("username","") #check the empty or not
            if not username:
                return JsonResponse({"error":"user name is required"},status=400)
            #checks length
            if len(username)<3 or len(username)>20:
                return JsonResponse({"error":"user should contains 3 to 20 characters"},status=400)
            #checks start and end
            if username[0] in "._" or username[-1] in "._":
                    return JsonResponse({"error":"username should not starts or ends with . or _"},status=400)
            #checks username
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
             return JsonResponse({"error":"user name should contain letters,nums,dot,Underscores"},status=400)
            #checks .. and _ _ not in username
            if ".." in username or "__" in username:
                return JsonResponse({"error":"cannot have .. or __"},status=400)
        return self.get_response(request) #final views
#email not empty
#basic email pattern
#if duplicate email found --show email


# email should not empty
# basic email pattern
# if duplicate email found --->show  email already exists

class EmailMiddleware:
    def __init__(self,get_response):  
        self.get_response=get_response
    def __call__(self,request):
        if(request.path=="/signup/"):
            data=json.loads(request.body)
            Email=data.get("email","")
            if not Email:
                return JsonResponse({"error":"email should not empty"},status=400)
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', Email):
                return JsonResponse({"error":"invalid email format"},status=400)
            if Users.objects.filter(email=Email).exists():
                return JsonResponse({"error": "email already exists"}, status=400)

        return self.get_response(request)
    
class PasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if(request.path == "/signup/"):
            data = json.loads(request.body)
            password = data.get("password", "")

            # Empty check
            if not password:
                return JsonResponse({"error": "password should not be empty"}, status=400)

            # Length check
            if len(password) < 8 or len(password) > 12:
                return JsonResponse({"error": "password should contain 8 to 12 characters"}, status=400)

            # Strength check
            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,12}$'
            if not re.match(pattern, password):
                return JsonResponse({
                    "error": "Password must contain uppercase, lowercase, digit, and special character (@, $, !, %, ?, &)."
                }, status=400)

        return self.get_response(request)
