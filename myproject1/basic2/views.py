from django.shortcuts import render
from django.http import JsonResponse

# # Create your views here.
# def bs2_view(request):
#     return JsonResponse({'message': 'This is the basic2 view response'})
# import uuid
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Product
# from .serializers import ProductSerializer
# from .supabase_client import supabase

# class ProductUploadView(APIView):

#     def post(self, request):
#         name = request.data.get("name")
#         image = request.FILES.get("image")

#         if not image:
#             return Response({"error": "Image is required"}, status=400)

#         # unique filename
#         file_name = f"{uuid.uuid4()}_{image.name}"

#         # upload to supabase
#         supabase.storage.from_("product-images").upload(
#             file_name,
#             image.read(),
#             {"content-type": image.content_type}
#         )

#         # get public url
#         image_url = supabase.storage.from_("product-images").get_public_url(file_name)

#         product = Product.objects.create(
#             name=name,
#             image_url=image_url
#         )

#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 65000,
        "stock": 15,
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 25000,
        "stock": 30,
        "rating": 4.3
    },
    {
        "id": 3,
        "name": "Headphones",
        "category": "Accessories",
        "price": 3000,
        "stock": 50,
        "rating": 4.1
    },
    {
        "id": 4,
        "name": "Keyboard",
        "category": "Accessories",
        "price": 1500,
        "stock": 40,
        "rating": 4.0
    },
    {
        "id": 5,
        "name": "Mouse",
        "category": "Accessories",
        "price": 800,
        "stock": 60,
        "rating": 4.2
    },
    {
        "id": 6,
        "name": "Smart Watch",
        "category": "Wearables",
        "price": 5000,
        "stock": 20,
        "rating": 4.4
    },
    {
        "id": 7,
        "name": "Bluetooth Speaker",
        "category": "Audio",
        "price": 3500,
        "stock": 25,
        "rating": 4.3
    },
    {
        "id": 8,
        "name": "Tablet",
        "category": "Electronics",
        "price": 18000,
        "stock": 10,
        "rating": 4.2
    },
    {
        "id": 9,
        "name": "Power Bank",
        "category": "Accessories",
        "price": 2000,
        "stock": 45,
        "rating": 4.1
    },
    {
        "id": 10,
        "name": "Web Camera",
        "category": "Electronics",
        "price": 2500,
        "stock": 18,
        "rating": 4.0
    }
]
def productById(request,id):
    for product in products:
        if product["id"]==id:
            return JsonResponse(product)
        return JsonResponse({"error":"product not found"})
    