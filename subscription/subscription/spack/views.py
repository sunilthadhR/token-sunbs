import json
from itertools import count

from django.core.mail.message import utf8_charset
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, PACK_CHOICES
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def subscription(request):
    if request.method=='POST':
       data = json.loads(request.body.decode('utf-8'))
       mobile=data.get('mobile')
       price = data.get('price')
       import random
       num = random.randint(1000000000, 9999999999)
       mob=[]
       val=User.objects.filter(mobile=mobile).exists()
       if price:
           if price == '499':
               pack = PACK_CHOICES[0]
           if price == "599":
               pack = PACK_CHOICES[1]
           if price == "699":
               pack = PACK_CHOICES[2]
           if price == "799":
               pack = PACK_CHOICES[3]
           if price == "899":
               pack = PACK_CHOICES[4]
       if val:
           mobil=User.objects.filter(mobile=mobile).all()
           for i in mobil:
               mob.append(i.mobile)
           value=len(mob)
           if value >3:
               return JsonResponse({"message": "you have reached your smc!"})

       p=[]
       pp=User.objects.filter(mobile=mobile, price=price).all()
       for i in pp:
           p.append(i.price)
           if pp:
               return JsonResponse({"message":"already pack subscribed"})
       User.objects.create(mobile=mobile, smc=num,price=price,pack=pack)
       breakpoint()
       return JsonResponse({"message":"subs added","smc":num})



@csrf_exempt
def token(request):
    if request.method=='POST':
        r=redis.Redis(host='localhost', port=6379, db=0)
        data = json.loads(request.body.decode('utf-8'))
        token =data.get('token')
        if token:
            r.set(token, token, ex=60)
            return JsonResponse({"message": "Token generated"})
        return JsonResponse({"error": "No token provided"}, status=400)


@csrf_exempt
def user(request):
    data = json.loads(request.body.decode('utf-8'))
    r = redis.Redis(host='localhost', port=6379, db=0)
    value = data.get('token')
    mobile = data.get('mobile')
    user=User.objects.filter(mobile=mobile).last()
    token = r.get(value)
    if token:
        if user:
            return JsonResponse({"message": "logined user"})
        return JsonResponse({"message": "Non_logined user"})
    return JsonResponse({"message": 'token expired,kindly Generate new Token'})




