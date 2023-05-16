from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('teacher_registration', views.teacher_registration, name='teacher_registration'),
    path('student_registration', views.student_registration, name='student_registration'),
    path('<str:username>/<str:teacher_id>/<str:designation>/<str:dept_id>/<str:token>/verified/', views.teacher_verified, name='teacher-verified'),
]