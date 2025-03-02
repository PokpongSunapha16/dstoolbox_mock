from django.urls import path
from .views import *
urlpatterns = [
    path('course/',course_list ,name='course_list'),
    path('update/<str:pk>/',CourseUpdateView.as_view() ,name='update'),
    path('delete/<int:pk>/',CourseDeleteView.as_view() ,name='delete'),
    path('course_search/',course_search,name='course_search'),
]