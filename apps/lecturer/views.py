from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from apps.users.models import Teacher
from .models import Lecture
from .forms import LectureForm
# Create your views here.

@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateLectureView(CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = 'dashboard/lecture/create_lecture.html'
    success_url = reverse_lazy('lecture-list')

    def form_valid(self, form):
        if not self.request.user.is_teacher:
            return HttpResponse(status=400, data="Not Allowed")
        form.instance.lecturer = self.request.user.teacher.id
        return super().form_valid(form)


class LectureListView(ListView):
    model = Lecture
    template_name = 'dashboard/lecture/lecture_list.html'
