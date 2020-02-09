from django.urls import path
# .views refer to the views.py in the current directory as this file

from .views import show_courses, create_course 

urlpatterns = [
    path('', show_courses),
    path('create', create_course),
]