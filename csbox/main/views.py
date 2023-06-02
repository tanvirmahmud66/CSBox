import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Department, Batch, Section, Verification, TeacherProfile, StudentsProfile, Semester, SessionData, PostDB, CommentDB, FileDatabase
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
#======================================================== Sign In

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        invalid = "Invalid username of password"
        try:
            user_model = User.objects.get(username=username)
            if user_model:
                verify_model = Verification.objects.get(user=user_model)
                if verify_model.is_verified and verify_model.is_teacher:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        print("user logged In As Teacher")
                        return redirect('teacher_home')
                    else:
                        messages.info(request, invalid)
                        return redirect('signin')
                elif verify_model.is_verified and verify_model.is_student:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return render(request, "student/home.html")
                    else:
                        messages.info(request, invalid)
                        return redirect('signin')
                else:
                    return render(request, 'signin.html', {
                        "notification": True,
                        "warning": True, 
                        "value": "Your Account not verified Yet. Please check your email for verification."
                    })
        except Exception as e:
            print(e)
            messages.info(request, "User Not Found!")
            return redirect('signin')
    return render(request, 'signin.html')


#======================================================== Logout User

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')


#======================================================== Registration (Teacher)

def teacher_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        teacher_id = request.POST["teacher_id"]
        designation = request.POST["designation"]
        department = request.POST["department"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('teacher_registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already used')
                return redirect('teacher_registration')
            elif TeacherProfile.objects.filter(teacher_id=teacher_id).exists():
                messages.info(request, 'This teacher id already used')
                return redirect('teacher_registration')
            else:
                new_user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name, 
                    username=username, 
                    email=email,
                    password=password
                )
                new_user.save()
                user_model = User.objects.get(username=username)
                token = str(uuid.uuid4())
                verify = Verification.objects.create(
                    user=user_model, 
                    token=token,
                    is_teacher=True,
                )
                verify.save()
                domain_name = get_current_site(request).domain
                dept = Department.objects.get(department=department)
                link = f"http://{domain_name}/{username}/{teacher_id}/{designation}/{dept.id}/{token}/verified/"
                subject = "Email Verification"
                message = f"Please Click This Link {link} to verify your registration process. Thanks in Advanced."
                recipient_list = [email]
                email_from = settings.EMAIL_HOST_USER
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False
                )

                return render(request,'notification.html', {
                    "title": "Confirm Your Email",
                    "notification": "We have send an email to your email address for verify your registration process. Please check your email address.",
                })
        # elif password[0]=="-" and confirm_password[0]=="-":
        #     messages.info(request, "Invalid Password")
        #     return redirect('teacher_registration')
        else:
            messages.info(request, "Password not matched")
            return redirect('teacher_registration')
    all_department = Department.objects.all()
    return render(request, 'teacher_registration.html', {
        "departments": all_department,
    })


#================================================================================= Teacher Verified

def teacher_verified(request, username, teacher_id, designation, dept_id, token):
    verify_model = Verification.objects.get(token=token)
    verify_model.is_verified = True
    verify_model.save()
    user_model = User.objects.get(username=username)
    department = Department.objects.get(id=dept_id)
    if TeacherProfile.objects.filter(user=user_model).exists():
        return redirect('signin')
    else:
        new_teacher_profile = TeacherProfile.objects.create(
            user=user_model,
            userId=user_model.id,
            teacher_id=teacher_id,
            designation=designation,
            department=department
        )
        new_teacher_profile.save()
        return render(request, 'notification.html', {
            "title": "Email Confirmed",
            "notification": "Your email is verified. Please", 
            "login": True
        })


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  Registration (student)

def student_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        student_id = request.POST['student_id']
        sec = request.POST['section']
        section_model = Section.objects.get(id=sec)
        department = section_model.department
        batch = section_model.batch
        section = section_model.section
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        print(first_name, last_name, username, email, student_id, department, batch, section, password)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('student_registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already used")
                return redirect('student_registration')
            elif StudentsProfile.objects.filter(student_id=student_id).exists():
                messages.info(request, "This Student ID already used")
                return redirect('student_registration')
            else:
                new_user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                new_user.save()
                user_model = User.objects.get(username=username)
                token = str(uuid.uuid4())
                verify = Verification.objects.create(
                    user=user_model,
                    token=token,
                    is_student=True
                )
                verify.save()
                domain_name = get_current_site(request).domain
                dept_model = Department.objects.get(department=department)
                batch_model = Batch.objects.get(batch=batch.batch)
                section_model = Section.objects.get(
                    department=department,
                    batch=batch,
                    section=section
                )
                link = f"http://{domain_name}/{username}/{student_id}/{dept_model.id}/{batch_model.id}/{section_model.id}/{token}/verified/"
                subject = "Email Verification"
                message = f"Please Click This Link {link} to verify your registration process. Thanks in Advanced."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,
                    fail_silently=False
                )
                return render(request, 'notification.html',{
                    "title": "Confirm Your Email",
                    "notification": "We have Send an email to your email address for verify registration process. Please check your email address.",
                })
        else:
            messages.info(request, 'Password not matched')
            return redirect('student_registration')
    all_department = Department.objects.all()
    all_batch = Batch.objects.all()
    return render(request, 'student_registration.html', {
        "departments": all_department,
        "batches": all_batch,
    })

#----------- get section ----------------
def get_section(request):
    department = request.GET['department']
    batch = request.GET['batch']
    filtered_section = Section.objects.filter(department=department, batch=batch)
    sections = [{"value": section.id, "text": section.section} for section in filtered_section]
    return JsonResponse(sections, safe=False)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  Student Verified

def student_verified(request, username, student_id, dept_id, batch_id, section_id, token):
    verify_model = Verification.objects.get(token=token)
    verify_model.is_verified = True
    verify_model.save()
    user_model = User.objects.get(username=username)
    department = Department.objects.get(id=dept_id)
    batch = Batch.objects.get(id=batch_id)
    section = Section.objects.get(id=section_id)
    new_student = StudentsProfile.objects.create(
        user=user_model,
        userId=user_model.id,
        student_id = student_id,
        department = department,
        batch = batch,
        section=section.section
    )
    new_student.save()
    return render(request, "notification.html", {
        "titile": "Email Confirmed",
        "notification": "Your email is verified. Please",
        "login": True
    })


#================================================================== Home
@login_required(login_url='signin')
def home(request):
    verify_user = Verification.objects.get(user=request.user)
    if verify_user.is_teacher:
        return redirect('teacher_home')
    else:
        return redirect('student_home')



#================================================================== Teacher Home page
@login_required(login_url='signin')
def teacher_home(request):
    normal_posts = PostDB.objects.filter(creator=request.user, is_announcement=False)
    announcement = PostDB.objects.filter(creator=request.user, is_announcement=True)
    return render(request, "teacher/home.html",{
        "normal_posts": normal_posts,
        "announcement": announcement,
    })

#--------------------------------------------------------- Profile
@login_required(login_url='signin')
def check_profile(request):
    try:
        user_verify = Verification.objects.get(user=request.user)
        if user_verify.is_teacher:
            return redirect('teacher_profile')
        else:
            return redirect('student_profile')
    except Exception as e:
        print(e)


#======================================================================= Teacher Profile
@login_required(login_url='signin')
def teacher_profile(request):
    teacher_profile = TeacherProfile.objects.get(user=request.user)
    if request.method=="POST":
        bio = request.POST.get('bio')
        studied_at = request.POST.get('studied_at')
        program = request.POST.get('program')
        address = request.POST.get('address')
        teacher_profile.bio = bio
        teacher_profile.program = program
        teacher_profile.studied_at = studied_at
        teacher_profile.address = address
        teacher_profile.save()
        return redirect('check_profile', request.user)
    return render(request, 'teacher/teacher_profile.html', {
        "teacher_profile": teacher_profile,
    })

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Student Profile
@login_required(login_url='signin')
def student_profile(request):
    student_profile = StudentsProfile.objects.get(user=request.user)
    if request.method == "POST":
        bio = request.POST.get('bio')
        school = request.POST.get('school')
        college = request.POST.get('college')
        address = request.POST.get('address')
        student_profile.bio = bio
        student_profile.school = school
        student_profile.college = college
        student_profile.address = address
        student_profile.save()
    return render(request, 'student/student_profile.html', {
        "student": True,
        "student_profile": student_profile,
    })


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Student Home page
@login_required(login_url='signin')
def student_home(request):
    return render(request, "student/home.html", {
        "student": True,
    })



#================================================================== Courses
@login_required(login_url='signin')
def courses(request):
    verify_user = Verification.objects.get(user=request.user)
    if verify_user.is_teacher:
        return redirect('teacher_courses')
    else:
        return redirect('student_courses')
    
#================================================================== Teacher Courses
@login_required(login_url='signin')
def teacher_courses(request):
    if request.method=="POST":
        sessionName = request.POST['sessionName']
        sec = request.POST['section']
        section_model = Section.objects.get(id=sec)
        department = section_model.department
        batch = section_model.batch
        section = section_model
        sem = request.POST['semester']
        semester = Semester.objects.get(id=sem)
        print("Course Name: ", sessionName)
        print("Department: ", department)
        print("Batch: ", batch)
        print("Section: ", section.section)
        print("Semester: ", semester)
        teacher_id = TeacherProfile.objects.get(user=request.user)
        new_session = SessionData.objects.create(
            sessionName=sessionName,
            department=department,
            batch=batch,
            section=section,
            faculty=teacher_id,
            semester=semester
        )
        new_session.save()
    departments = Department.objects.all()
    batches = Batch.objects.all()
    semesters = Semester.objects.all()
    if request.GET.get('q')!=None:
        q=request.GET.get('q')
        all_session = SessionData.objects.filter(
            faculty__user=request.user,
            semester=q
        )
        sem = Semester.objects.get(id=q)
        return render(request, 'teacher/all_courses.html', {
            "departments": departments,
            "batches": batches, 
            "semesters": semesters,
            "all_session": all_session.order_by('semester'),
            "q": sem
        })
    else:
        all_session = SessionData.objects.filter(
           faculty__user=request.user,
           semester=semesters[0] 
        )
        
    return render(request, 'teacher/all_courses.html', {
        "departments": departments,
        "batches": batches, 
        "semesters": semesters,
        "all_session": all_session.order_by('semester'),
        "q": semesters[0]
    })


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Student Courses
@login_required(login_url='signin')
def student_courses(request):
    return render(request, 'student/all_courses.html')


#================================================================== Single course
@login_required(login_url='signin')
def single_course(request, session_name,pk):
    verify_user = Verification.objects.get(user=request.user)
    if verify_user.is_teacher:
        return redirect('fuculty_single_course', session_name,pk)
    else:
        return redirect('student_single_course', session_name,pk)

#=================================================================== Faculty Single Course
@login_required(login_url='signin')
def faculty_single_course(request, session_name,pk):
    course_obj = SessionData.objects.get(id=pk)
    verify_obj = Verification.objects.get(user=request.user)
    all_post = PostDB.objects.filter(session=course_obj)
    all_files = FileDatabase.objects.filter(sessionId=pk)
    if request.method=="GET":
        post_id_edit = request.GET.get('post_id')
        edit_post_body = request.GET.get('edit_post_content')
        edit_announcement = request.GET.get('edit-announcement')
        try:
            editpost_postdb = PostDB.objects.get(id=post_id_edit)
            if editpost_postdb is not None:
                editpost_postdb.postBody = edit_post_body
                editpost_postdb.is_announcement = edit_announcement
                editpost_postdb.save()
        except Exception as e:
            print(e)
        
    if request.method == "POST":
        postbody = request.POST['post_content']
        files = request.FILES.getlist('files')
        is_announcement = request.POST.get("announcement")
        if is_announcement=="True":
            announcement = True
        else:
            announcement = False
        print(postbody, files, is_announcement)
        if verify_obj.is_teacher:
            new_post = PostDB.objects.create(
                session = course_obj,
                creator = course_obj.faculty.user,
                is_teacher=True,
                is_announcement=announcement,
                postBody = postbody,
            )
            new_post.save()
            for file in files:
                file_upload = FileDatabase.objects.create(
                    uploadFile = file,
                    sessionId = course_obj.id,
                    postId=new_post.id
                )
                file_upload.save()
            return redirect("fuculty_single_course", session_name, pk)
    return render(request, 'teacher/single_course.html', {
        "course_obj": course_obj,
        "posts": all_post,
        "files": all_files,
    })

#------------ faculty delete post -------------
def faculty_del_post(request, session_name, session_id, pk):
    del_post = PostDB.objects.get(id=pk)
    del_post.delete()
    return redirect("fuculty_single_course", session_name, session_id)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Student Single Course
# @login_required(login_url='signin')
def student_single_course(request, pk):
    pass



#@@@@@@@@@@@@@@@@@@@@@ single post page @@@@@@@@@@@@@@@@@@@@@@@@@@@
def single_post(request, post_id):
    target_post = PostDB.objects.get(id=post_id)
    return render(request, 'single_post.html', {
        "post": target_post,
    })