import email
from email import message
from multiprocessing import context

import django
from .models import AdminInfo, Links, User
from .serializers import AdminInfoSerializer, LinkSrializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



@api_view(['GET','POST','PUT'])
def AdminInfoViewset(request):
    if request.method == 'GET':
        notes = AdminInfo.objects.all()
        serializer = AdminInfoSerializer(notes,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def SingleAdminInfoViewset(request):
    if request.method == 'GET':
        # notes = AdminInfo.objects.all()
        # admin=AdminInfo.objects.filter(email=request.data["email"]) 
        admin=AdminInfo.objects.filter(email=request.query_params.get('email')) 
        serializer = AdminInfoSerializer(admin,many=True)
        if admin :
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET','POST','PUT'])
def UserViewset(request):
    if request.method == 'GET':
        users= User.objects.all() 
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        users=User.objects.all() 
        user = {}
        for i in users:
            if str(i) == request.data["email"]:
                user = i
                break
        if user != {}:
            print("user exists")
            serializer = UserSerializer(user,data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # if request.method == 'PUT':
    #     users=User.objects.all() 
    #     user = {}
    #     for i in users:
    #         if str(i) == request.data["email"]:
    #             user = i 
    #             break
    #     print(user)
    #     serializer = UserSerializer(user,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

@api_view(['GET'])
def SingeUserViewset(request):
    if request.method == 'GET': 
        print(request)
        # users=User.objects.filter(email=request.data["email"]) 
        # users=User.objects.all()
        users=User.objects.filter(email=request.query_params.get('email')) 
        serializer = UserSerializer(users,many=True)
        if users :
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
         

@api_view(['GET'])
def SingleUserLinkViewset(request):
    if request.method == 'GET':
        links=Links.objects.filter(email=request.query_params.get('email')) 
        serializer = LinkSrializer(links,many=True)
        return Response(serializer.data)    

@api_view(['GET','POST'])
def LinkViewset(request):
    if request.method == 'GET':
        link=Links.objects.all()
        serializer = LinkSrializer(link,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        print(request.data)
        message = f'Your bill link : {request.data["link"]}  and password : {request.data["password"]}'
        send_mail('your latest bill from vendor xyz',message,'settings.EMAIL_HOST_USER',[request.data["email"]],fail_silently=False)
        serializer = LinkSrializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


