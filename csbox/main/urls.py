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

    path('home/', views.home, name='home'),
    path('home/faculty/', views.teacher_home, name='teacher_home'),
    path('home/student/', views.student_home, name='student_home'),

    path('courses', views.courses, name='courses'),
    path('faculty/courses/', views.teacher_courses, name='teacher_courses'),
    path('student/courses/', views.student_courses, name='student_courses'),

    path('single_course/<str:session_name>-<int:pk>/', views.single_course, name='single_course'),
    path('faculty/courses/<str:session_name>-<int:pk>/', views.faculty_single_course, name='fuculty_single_course'),
    path('student/courses/<str:session_name>-<int:pk>/', views.student_single_course, name='student_single_course'),
]