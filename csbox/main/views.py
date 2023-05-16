import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Department, Batch, DepartmentBatchSection, Verification, TeacherProfile, StudentsProfile
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
#======================================================== Sign In
def signin(request):
    if request.mothod=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        invalid = "Invalid username of password"
        
        try:
            user_model = User.objects.get(username=username)
            if user_model:
                verify_model = Verification.objects.get(user=user_model)
                if verify_model.is_verified:
                    if verify_model.is_teacher:
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            login(request, user)
                            return HttpResponse("Teacher_Logged In")
                        else:
                            messages.info(request, invalid)
                            return redirect('signin')
                    elif verify_model.is_student:
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            login(request, user)
                            return HttpResponse("Student_Logged In")
                        else:
                            messages.info(request, invalid)
                            return redirect('signin')
                else:
                    messages.info(request, "User is not verified yet, check your email for verification.")
                    return redirect('signin')
            else:
                messages.info(request, "User not found")
                return redirect('signin')
        except Exception as e:
            print(e)
            messages.info(request, invalid)
            return redirect('signin')
    return render(request, 'signin.html')


#======================================================== Registration (Teacher)
def teacher_registration(request):
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
                new_user = User.objects.create(
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
                    "notification": "We have send an email to your email address for verify your registration process. Please check your email address."
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


#============================================================================= Teacher Verified
def teacher_verified(request, username, teacher_id, designation, dept_id, token):
    verify_model = Verification.objects.get(token=token)
    verify_model.is_verified = True
    verify_model.save()
    user_model = User.objects.get(username=username)
    department = Department.objects.get(id=dept_id)
    new_teacher_profile = TeacherProfile.objects.create(
        user=user_model,
        userId=user_model.id,
        teacher_id=teacher_id,
        designation=designation,
        department=department
    )
    new_teacher_profile.save()
    return render(request, 'signin.html', {
        "notification": True,
        "value": "Your email is verified, Please login again."
    })


#======================================================== Registration (student)
def student_registration(request):
    return render(request, 'student_registration.html')


#============================================================================= Student Verified
def student_verified(request):
    pass