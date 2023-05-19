from django.urls import path
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('logout/', views.logout_page, name='logout'),
    path('teacher_registration', views.teacher_registration, name='teacher_registration'),
    path('student_registration', views.student_registration, name='student_registration'),
    path('get-section/', views.get_section, name='get-section'),
    path('<str:username>/<str:teacher_id>/<str:designation>/<str:dept_id>/<str:token>/verified/', views.teacher_verified, name='teacher-verified'),
    path('<str:username>/<str:student_id>/<int:dept_id>/<int:batch_id>/<int:section_id>/<str:token>/verified/', views.student_verified, name='student-verified'),

]