from django.urls import path
# from attendease import views
from .views import CreateAttendaceView

urlpatterns = [
    # path("dashboard/", dashboard, name="dashboard"),
    path("mark/<str:slug>/", CreateAttendaceView.as_view(), name="mark-attendance"),
]