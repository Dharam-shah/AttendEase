from django.http import HttpResponse
from django.shortcuts import render
from apps.lecturer.models import Lecture
from django.views.generic import CreateView as GCV
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .models import Attendance
from django.views.generic import ListView, DetailView 
from apps.lecturer.forms import MarkAttendanceForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def index(request):
    return render(request, "attendease/homepage.html")


def dashboard(request):
    return render(request, "dashboard/base.html")


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateAttendaceView(CreateView, DetailView):
    """
    TODO: implement logic to mark attendance.
     - get user from request
     - validate that the requested user is student or not
     - save it
    """
   
    model = Attendance
    form_class = MarkAttendanceForm
    template_name = 'attendease/mark_attendance.html'

    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     lecture = Lecture.objects.all()

    #     return context
    
    queryset = Lecture.objects.all()

    def post(self, request, *args, **kwargs):
        self.object = None
        lecture = self.get_object()
        user = request.user

        if not user.is_student:
            return HttpResponse("Only Student Can Mark There Attendance")
        
        attendace = Attendance.entry(user.student, lecture)
        
        return HttpResponse(f"Successfully marked attanced for {attendace.lecture.title}.")


class AttendanceDetailView(ListView):
    model = Attendance
    template_name = 'attendease/attendance_detail.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     if self.request.user.is_teacher:
    #         return queryset.filter(lecturer__user=self.request.user)
    #     elif self.request.user.is_student:
    #         return queryset.filter(course__course_enroll__student__user=self.request.user)

    #     return queryset