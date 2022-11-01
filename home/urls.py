from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('faculty/', views.faculty, name="faculty"),
    path("courses/<str:hm>/", views.course_details, name="course_details"),
    path("courseAdd/", views.courseAdd, name="course_add"),
    path('course/', views.course, name="course"),
    path('notice/', views.notice, name="notice"),

]
