from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PaymentDetails

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