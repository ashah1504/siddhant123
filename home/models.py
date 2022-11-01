from django.db import models

# Create your models here.

class faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    qualifications = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.department

    class Meta:
        verbose_name_plural = "Faculty"




class course(models.Model):
    courses = [
        ('BT', "Btech"),
        ('MBT', "MBATech"),
        ('MT', "Mtech"),
    ]
    course_name = models.CharField(max_length=50)
    course_type = models.CharField(choices=courses, null=True, blank=True, max_length=10, default="Btech")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_type + " " + self.course_name

    class Meta:
        verbose_name_plural = "Course"


class notice(models.Model):
    subject = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Notice"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    context = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"

