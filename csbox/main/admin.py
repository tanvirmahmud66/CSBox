from django.contrib import admin
from .models import Department, Batch, DepartmentBatchSection, Verification, TeacherProfile, StudentsProfile


# Register your models here.
class DepartmentView(admin.ModelAdmin):
    list_display = ('id', 'department')


class BatchView(admin.ModelAdmin):
    list_display = ('id', 'batch')


class DepartmentBatchSectionView(admin.ModelAdmin):
    list_display = ('id', 'batch', 'section', 'department')


class VerificationView(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'is_verified', 'is_teacher', 'is_student')


class TeacherProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'teacher_id', 'designation', 'department')


class StudentProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'student_id', 'department', 'batch', 'section')


admin.site.register(Department, DepartmentView)
admin.site.register(Batch, BatchView)
admin.site.register(DepartmentBatchSection, DepartmentBatchSectionView)
admin.site.register(Verification, VerificationView)
admin.site.register(TeacherProfile, TeacherProfileView)
admin.site.register(StudentsProfile, StudentProfileView)