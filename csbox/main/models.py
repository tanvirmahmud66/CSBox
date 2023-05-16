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
class DepartmentBatchSection(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    section = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'section'
        verbose_name = 'all batch section'

    def __str__(self):
        return f"{self.batch} {self.section} {self.department}"
    

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
    
#================================================================== Teacher Profile
class TeacherProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    teacher_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

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

    class Meta:
        verbose_name = 'StudentProfile'
        verbose_name_plural = 'StudentProfile'

    def __str__(self):
        return self.user.username
