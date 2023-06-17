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
    path('faculty/home/', views.teacher_home, name='teacher_home'),
    path('student/home/', views.student_home, name='student_home'),

    # profile page
    path('visit/profile/<str:pk>/', views.visit_profile, name='visit_profile'),
    path('check_profile/', views.check_profile, name='check_profile'),
    path('faculty/profile/', views.teacher_profile, name='teacher_profile'),
    path('student/profile/', views.student_profile, name='student_profile'),

    path('courses', views.courses, name='courses'),
    path('faculty/courses/', views.teacher_courses, name='teacher_courses'),
    path('student/courses/', views.student_courses, name='student_courses'),

    path('single_course/<str:session_name>-<int:pk>/', views.single_course, name='single_course'),
    path('faculty/courses/<str:session_name>-<int:pk>/', views.faculty_single_course, name='faculty_single_course'),
    path('student/courses/<str:session_name>-<int:pk>/', views.student_single_course, name='student_single_course'),

    # CRUD operation
    path('faculty/delete-post/<str:session_name>-<int:session_id>/<int:pk>/', views.faculty_del_post, name='faculty-del-post'),
    path('student/delete-post/<str:session_name>-<int:session_id>/<int:pk>/', views.student_del_post, name='student-del-post'),

    # file remove
    path('files/remove/<int:session_id>/<int:file_id>/', views.file_remove, name='remove_file'),

    #home single post section
    path('home/single_post/<int:post_id>/', views.single_post, name='single_post'),
]