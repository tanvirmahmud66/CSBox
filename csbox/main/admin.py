from django.contrib import admin
from .models import Department, Batch, Section, StudentId, Semester, Verification, TeacherProfile, StudentsProfile, SessionData


# Register your models here.
class DepartmentView(admin.ModelAdmin):
    list_display = ('id', 'department')


class BatchView(admin.ModelAdmin):
    list_display = ('id', 'batch')


class SectionView(admin.ModelAdmin):
    list_display = ('id', 'batch', 'section', 'department')



class StudentIdView(admin.ModelAdmin):
    list_display = ('id', 'department', 'batch', 'studentId')


class SemesterView(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')



class VerificationView(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'is_verified', 'is_teacher', 'is_student')


class TeacherProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'teacher_id', 'designation', 'department')


class StudentProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'student_id', 'department', 'batch', 'section')


class SessionDataView(admin.ModelAdmin):
    list_display = ('sessionName', 'department', 'batch', 'section', 'faculty', 'semester')


admin.site.register(Department, DepartmentView)
admin.site.register(Batch, BatchView)
admin.site.register(Section, SectionView)
admin.site.register(Verification, VerificationView)
admin.site.register(TeacherProfile, TeacherProfileView)
admin.site.register(StudentsProfile, StudentProfileView)
admin.site.register(StudentId, StudentIdView)
admin.site.register(Semester, SemesterView)
admin.site.register(SessionData, SessionDataView)