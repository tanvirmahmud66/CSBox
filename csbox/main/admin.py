from django.contrib import admin
from .models import Department, Batch, Section, Semester, Verification, TeacherProfile, StudentsProfile, SessionData, PostDB, CommentDB, FileDatabase, SessionMember


# Register your models here.
class DepartmentView(admin.ModelAdmin):
    list_display = ('id', 'department')


class BatchView(admin.ModelAdmin):
    list_display = ('id', 'batch')


class SectionView(admin.ModelAdmin):
    list_display = ('id', 'batch', 'section', 'department')


class SemesterView(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')



class VerificationView(admin.ModelAdmin):
    list_display = ('id', 'user', 'token', 'is_verified', 'is_teacher', 'is_student')


class TeacherProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'teacher_id', 'designation', 'department', 'works_at', 'bio', 'studied_at', 'program', 'address', 'profile_pic', 'cover_pic')


class StudentProfileView(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'student_id', 'department', 'batch', 'section', 'school', 'college', 'address', 'bio', 'profile_pic', 'cover_pic')


class SessionDataView(admin.ModelAdmin):
    list_display = ('sessionName', 'token','department', 'batch', 'section', 'faculty','semester')


class SessionMemberView(admin.ModelAdmin):
    list_display = ('id','session', 'member', 'token')


class PostDBView(admin.ModelAdmin):
    list_display = ('session', 'creator', 'postBody', 'is_teacher', 'is_student', 'is_announcement', 'created', 'updated')


class CommentDBView(admin.ModelAdmin):
    list_display = ('commenter', 'postId', 'commentBody', 'created')


class FileDatabaseView(admin.ModelAdmin):
    list_display = ('uploadFile', 'sessionId', 'postId')



admin.site.register(Department, DepartmentView)
admin.site.register(Batch, BatchView)
admin.site.register(Section, SectionView)
admin.site.register(Verification, VerificationView)
admin.site.register(TeacherProfile, TeacherProfileView)
admin.site.register(StudentsProfile, StudentProfileView)
admin.site.register(Semester, SemesterView)
admin.site.register(SessionData, SessionDataView)
admin.site.register(PostDB, PostDBView)
admin.site.register(CommentDB, CommentDBView)
admin.site.register(FileDatabase, FileDatabaseView)
admin.site.register(SessionMember, SessionMemberView)