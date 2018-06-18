from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import employeesserializers


# Create your views here.

class getAllEmployees(APIView):

    def get(self, request):
        emp1 = employees.objects.all()
        serializer = employeesserializers(emp1,many=True)
        return Response(serializer.data)

class createEmployee(APIView):

    def get(self,request):
        if 'fname' in request.GET and 'lname' in request.GET and 'empid' in request.GET:
            fname = request.GET['fname']
            lname = request.GET['lname']
            empid = request.GET['empid']
            try:
                obj = employees.objects.get(emp_id = empid)
                return Response(status=status.HTTP_409_CONFLICT)
            except employees.DoesNotExist:
                emp1 = employees(firstname=fname, lastname=lname, emp_id=empid)
                emp1.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class updateFname(APIView):

    def get(self, request):
        if 'empid' in request.GET and 'fname' in request.GET:
            empid = request.GET['empid']
            fname = request.GET['fname']
            try:
                emp1 = employees.objects.get(emp_id=empid)
                emp1.firstname = fname
                emp1.save()
                return Response(status=status.HTTP_200_OK)
            except employees.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class deleteEmployee(APIView):

    def get(self, request):
        if 'empid' in request.GET:
            empid = request.GET['empid']
            try:
                emp1 = employees.objects.get(emp_id=empid)
                emp1.delete()
                return Response(status=status.HTTP_200_OK)
            except employees.DoesNotExist:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)