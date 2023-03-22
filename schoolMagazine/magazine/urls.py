from django.contrib import admin
from django.urls import path, include, re_path
from .views import StudentsList, StudentsCRUD, SchoolClassList, SchoolClassCRUD, SchoolSubjList, SchoolSubjCRUD

urlpatterns = [
    path('students/', StudentsList.as_view()),
    path('students/<int:pk>/', StudentsCRUD.as_view()),
    path('schoolclass/', SchoolClassList.as_view()),
    path('schoolclass/<int:pk>/', SchoolClassCRUD.as_view()),
    path('schoolsubjects/', SchoolSubjList.as_view()),
    path('schoolsubjects/<int:pk>/', SchoolSubjCRUD.as_view()),
]