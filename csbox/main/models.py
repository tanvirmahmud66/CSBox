from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#==================================================== Department
class Department(models.Model):
    department = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "All Department"

    def __str__(self):
        return self.department
    
#===================================================== Batch
class Batch(models.Model):
    batch = models.IntegerField()
    class Meta:
        verbose_name = "batch"
        verbose_name_plural = "All Batch"

    def __str__(self):
        return f"{self.batch}"
    
#======================================================================= All section of all department
class Section(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'all batch section'

    def __str__(self):
        return f" {self.department} {self.batch} {self.section}"
    





#=========================================================================== Semester Name
class Semester(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.name} {self.year}"




#=============================================================== User Verification
class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()
    is_verified = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'verification'
        verbose_name_plural = 'verification'

    def __str__(self):
        return self.user.username
    


# #====================================================== default profile pic path
# def get_default_profile_pic():
#     return 'path/to/default/profile_pic.jpg'


#================================================================== Teacher Profile
class TeacherProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    teacher_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    works_at = models.CharField(max_length=150, null=True, blank=True, default="Stamford University Bangladesh")
    bio = models.CharField(max_length=250, null=True, blank=True)
    studied_at = models.CharField(max_length=250, null=True, blank=True)
    program = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='teacher_profilePic/', null=True, blank=True)
    cover_pic = models.ImageField(upload_to='teacher_coverPic/', null=True, blank=True)

    class Meta:
        verbose_name = 'TeacherProfile'
        verbose_name_plural = 'TeacherProfile'

    def __str__(self):
        return self.user.username


#============================================================= Student Profile
class StudentsProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    student_id = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=False)
    section = models.CharField(max_length=1)
    school = models.CharField(max_length=255 ,null=True, blank=True)
    college = models.CharField(max_length=255 ,null=True, blank=True)
    address = models.CharField(max_length=255 ,null=True, blank=True)
    bio = models.CharField(max_length=255 ,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='student_profilePic/', default="default_profile_pic.webp",null=True, blank=True)
    cover_pic = models.ImageField(upload_to='student_coverPic/', null=True, blank=True)

    class Meta:
        verbose_name = 'StudentProfile'
        verbose_name_plural = 'StudentProfile'

    def __str__(self):
        return self.user.username


#============================================================= Session Data
class SessionData(models.Model):
    sessionName = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    faculty = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    token = models.CharField(max_length=5, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Session Data'
        verbose_name_plural = 'Session Data'
    
    def __str__(self):
        return self.sessionName


#============================================================== Session Member
class SessionMember(models.Model):
    session = models.ForeignKey(SessionData, on_delete=models.CASCADE)
    member = models.ForeignKey(StudentsProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Session Member'
        verbose_name_plural = 'Session Member'
    
    def __str__(self):
        return f"{self.member}"


#============================================================== Post Database
class PostDB(models.Model):
    session = models.ForeignKey(SessionData, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_announcement = models.BooleanField(null=True, blank=True)
    postBody = models.TextField()
    has_file = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post DB"
        verbose_name_plural = "Post DB"
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return f"{self.session.faculty.user}"


#=============================================================== File Database
class FileDatabase(models.Model):
    uploadFile = models.FileField(upload_to='', null=True, blank=True)
    sessionId = models.IntegerField()
    postId = models.IntegerField()

    class Meta:
        verbose_name = "Files Database"
        verbose_name_plural = "Files Database"

    def __str__(self):
        return f"{self.uploadFile}"    


#================================================================ Post's Comment Database
class CommentDB(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(SessionData, on_delete=models.CASCADE, blank=True, null=True)
    postId = models.ForeignKey(PostDB, on_delete=models.CASCADE)
    commentBody = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment DB"
        verbose_name_plural = "Comment DB"

    def __str__(self):
        return self.commentBody
