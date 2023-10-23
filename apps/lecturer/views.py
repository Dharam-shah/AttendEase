from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Lecture
from .forms import LectureForm
# Create your views here.

@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateLectureView(CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = 'dashboard/lecture/create_lecture.html'
    success_url = reverse_lazy('lecture-list')


class LectureListView(ListView):
    model = Lecture
    template_name = 'dashboard/lecture/lecture_list.html'
