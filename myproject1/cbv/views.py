from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PaymentDetails
# mixins
from .mixins import helperMixin, ResponseMixins, ResponseeMixins, JsonResponseMixins

@method_decorator(csrf_exempt, name='dispatch')
class DemoClass(View):
    def get(self, request):
        return HttpResponse("This is a GET request response from DemoClass view.")
    def post(self, request):
        return HttpResponse("This is a POST request response from DemoClass view.")         
    def put(self, request):
        return HttpResponse("This is a PUT request response from DemoClass view.")
    def delete(self, request):
        return HttpResponse("This is a DELETE request response from DemoClass view.")
    
@method_decorator(csrf_exempt, name='dispatch')
class PaymentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')
            user_email = data.get('user_email')
            payment_mode = data.get('payment_mode')
            amount = data.get('amount')
            currency = data.get('currency', 'INR')
            payment_status = data.get('payment_status')

            payment = PaymentDetails.objects.create(
                order_id=order_id,
                user_email=user_email,
                payment_mode=payment_mode,
                amount=amount,
                currency=currency,
                payment_status=payment_status
            )
            return HttpResponse(f"Payment recorded with Transaction ID: {payment.transaction_id}", status=201)
        except Exception as e:
            return HttpResponse(f"Error processing payment: {str(e)}", status=400)
        


# mixins

class Mixin1(helperMixin,View):
    def get(self,request):
        # return HttpResponse(self.greetingMessage())
        # return HttpResponse("Hello am from mixin1")
        return JsonResponse({"message":"am from mixin1","end":self.greetingMessage()})
    
class Mixin2(helperMixin,View):
    def get(self,request):
        # return HttpResponse("am from mixin2")
        #  return HttpResponse(self.greetingMessage())
         return JsonResponse({"message":"am from mixin2","end":self.greetingMessage()})
    
class Products(ResponseMixins,View):
    def get(self,request):
        qp1=request.GET.get("qp1")
        if qp1=="success":
            return self.success()   
        else:
            return self.error()
class Productss(ResponseeMixins,View):
    def get(self,request):
        qp1=request.GET.get("qp1")
        name=request.GET.get("name")

        if qp1=="success":
            return self.success(name)   
        else:
            return self.error(name)



products = [
    {
        "id": 1,
        "name": "Atomic Habits",
        "category": "Self Improvement",
        "price": 399,
        "rating": 4.8,
        "stock": 25,
        "author": "James Clear",
        "image": "/media/books/atomic-habits.jpg",
        "description": "Build good habits and break bad ones with proven techniques."
    },
    {
        "id": 2,
        "name": "Rich Dad Poor Dad",
        "category": "Finance",
        "price": 299,
        "rating": 4.7,
        "stock": 18,
        "author": "Robert Kiyosaki",
        "image": "/media/books/rich-dad.jpg",
        "description": "Learn how money works and build financial freedom."
    },
    {
        "id": 3,
        "name": "The Psychology of Money",
        "category": "Finance",
        "price": 329,
        "rating": 4.9,
        "stock": 20,
        "author": "Morgan Housel",
        "image": "/media/books/psychology-money.jpg",
        "description": "Timeless lessons on wealth, greed, and happiness."
    },
    {
        "id": 4,
        "name": "Think and Grow Rich",
        "category": "Motivation",
        "price": 349,
        "rating": 4.6,
        "stock": 15,
        "author": "Napoleon Hill",
        "image": "/media/books/think-grow-rich.jpg",
        "description": "Success principles based on mindset and persistence."
    },
    {
        "id": 5,
        "name": "The Alchemist",
        "category": "Fiction",
        "price": 249,
        "rating": 4.5,
        "stock": 30,
        "author": "Paulo Coelho",
        "image": "/media/books/alchemist.jpg",
        "description": "A story about dreams, destiny, and purpose."
    },
    {
        "id": 6,
        "name": "Ikigai",
        "category": "Lifestyle",
        "price": 199,
        "rating": 4.4,
        "stock": 40,
        "author": "Héctor García",
        "image": "/media/books/ikigai.jpg",
        "description": "Discover your reason for being and live happily."
    },
    {
        "id": 7,
        "name": "Deep Work",
        "category": "Productivity",
        "price": 379,
        "rating": 4.7,
        "stock": 12,
        "author": "Cal Newport",
        "image": "/media/books/deep-work.jpg",
        "description": "Rules for focused success in a distracted world."
    },
    {
        "id": 8,
        "name": "Start With Why",
        "category": "Leadership",
        "price": 289,
        "rating": 4.6,
        "stock": 22,
        "author": "Simon Sinek",
        "image": "/media/books/start-with-why.jpg",
        "description": "How great leaders inspire action."
    },
    {
        "id": 9,
        "name": "Zero to One",
        "category": "Startup",
        "price": 319,
        "rating": 4.5,
        "stock": 16,
        "author": "Peter Thiel",
        "image": "/media/books/zero-to-one.jpg",
        "description": "Notes on startups and building the future."
    },
    {
        "id": 10,
        "name": "The Power of Subconscious Mind",
        "category": "Mindset",
        "price": 259,
        "rating": 4.6,
        "stock": 28,
        "author": "Joseph Murphy",
        "image": "/media/books/subconscious-mind.jpg",
        "description": "Use your subconscious mind to achieve success."
    }
]


class getproductByCategory(JsonResponseMixins,View):
    filteredData=[]
    def get(self,request,ctg):
        for product in products:
            if product["category"].lower()==ctg.lower():
                self.filteredData.append(product)

        # return JsonResponse(self.filteredData,safe=False)
        return self.success(self.filteredData)
