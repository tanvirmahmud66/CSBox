from django.contrib import admin
from .models import Department, Batch, Section, TeacherId, StudentId, SemesterName, Semester, Verification, TeacherProfile, StudentsProfile


# Register your models here.
class DepartmentView(admin.ModelAdmin):
    list_display = ('id', 'department')


class BatchView(admin.ModelAdmin):
    list_display = ('id', 'batch')


class SectionView(admin.ModelAdmin):
    list_display = ('id', 'batch', 'section', 'department')


class TeacherIdView(admin.ModelAdmin):
    list_display = ('id', 'department', 'teacherId')

class StudentIdView(admin.ModelAdmin):
    list_display = ('id', 'department', 'batch', 'studentId')


class SemesterNameView(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')


class SemesterView(admin.ModelAdmin):
    list_display = ('id', 'semesterName', 'department', 'teacherId')


class VerificationView(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'is_verified', 'is_teacher', 'is_student')


class TeacherProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'teacher_id', 'designation', 'department')


class StudentProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'student_id', 'department', 'batch', 'section')


admin.site.register(Department, DepartmentView)
admin.site.register(Batch, BatchView)
admin.site.register(Section, SectionView)
admin.site.register(Verification, VerificationView)
admin.site.register(TeacherProfile, TeacherProfileView)
admin.site.register(StudentsProfile, StudentProfileView)
admin.site.register(TeacherId, TeacherIdView)
admin.site.register(StudentId, StudentIdView)
admin.site.register(SemesterName, SemesterNameView)
admin.site.register(Semester, SemesterView)