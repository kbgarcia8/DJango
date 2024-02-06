from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import StudentSerializer
from drfapp.models import Student

class TestView(APIView): #inheriting APIView
    #permission we want to collect before allowing access
    permission_classes = (IsAuthenticated, ) #user needs to be authenticated before allowing access
    #leave blank if anybody can access
    
    def get(self, request, *args, **kwargs): #kwargs-keyword argument
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)#get the data that will be submitted to this view
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)