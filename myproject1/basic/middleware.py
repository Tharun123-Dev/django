
# import json
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

     