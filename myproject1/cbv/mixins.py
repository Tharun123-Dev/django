
from django.http import JsonResponse
class helperMixin:
    def greetingMessage(self):
        return "All the best"
class ResponseMixins:
    def success(self):
        return JsonResponse({"msg":"successfully done"})
    def error(self):
        return JsonResponse({"msg":"error are there"})
class ResponseeMixins:
    def success(self,name):
        return JsonResponse({"msg":"successfully done","name":name})
    def error(self,name):
        return JsonResponse({"msg":"error are there","name":name})
    
class JsonResponseMixins:
    def success(self,data):
        return JsonResponse({"status":"ok","msg":"record fetched successfully","result":data})
    def error():
        return JsonResponse({"status":"error","msg":"something went wrong"})
