# from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

from .models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
# Create your views here.

def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    
    return Response({})
    
    















# def api_home(request,*args,**kwargs):
#     model_data = Product.objects.all().order_by("?").first()
    
#     data = {}
    
#     if model_data:
#         # data["id"] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         data = model_to_dict(model_data, fields=['id','title'])
        
#     return JsonResponse(data)











# def api_home(request,*args,**kwargs):
    
#     # request.body
#     if request.method == 'POST':
#         body = request.body # byte string json data
#         print("=======",request.body)
#     # data = {}
#     # try:
#     #     data = json.loads(body)
        
#     # except Exception as e:
#     #     print(e)
#     # print("******",data)
        
#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type
#     return JsonResponse({"pp":"kl"})
