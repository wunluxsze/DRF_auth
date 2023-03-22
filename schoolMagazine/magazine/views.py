from django.shortcuts import render
from rest_framework.response import Response
from .models import Students, SchoolClass, SchoolSubj
from .serializers import StudentsSerializer, SchoolClassSerializer, SchoolSubjSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.


class StudentsList(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )


class StudentsCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )


class SchoolClassList(ListCreateAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class SchoolClassCRUD(RetrieveUpdateDestroyAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )


class SchoolSubjList(ListCreateAPIView):
    queryset = SchoolSubj.objects.all()
    serializer_class = SchoolSubjSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class SchoolSubjCRUD(RetrieveUpdateDestroyAPIView):
    queryset = SchoolSubj.objects.all()
    serializer_class = SchoolSubjSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
