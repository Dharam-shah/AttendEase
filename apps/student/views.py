from django.shortcuts import render
from apps.lecturer.views import Lecture
from django.views.generic import ListView 

# Create your views here.
class LectureInfoView(ListView):
    model = Lecture
    template_name = 'dashboard/student/lecture_info.html'