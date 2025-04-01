from xml.etree.ElementTree import ParseError

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_200_OK
from rest_framework.views import APIView

from .serializer import SimpleUserSerializer, DetailUserSerializer, CreateUserSerializer, ChangePasswordSerializer
# Create your views here.


class User(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        user = request.user
        serializer = DetailUserSerializer(user)
        return Response(serializer.data)

    def put(self,request):
        user = request.user
        serializer = DetailUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            user=serializer.save()
            serializer = DetailUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    def delete(self,request):
        user=request.user
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class CreateUser(APIView):
    def post(self,request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            serializer=CreateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class ChangeUserPassword(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            if not old_password or not new_password:
                raise ParseError("Both old password and new password are required.")

            user=request.user

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({"detail":"changed"},status=HTTP_200_OK)
            else:
                return Response({"detail":"please check old password"},status=HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

