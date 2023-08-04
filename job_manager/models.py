from django.db import models

class Job(models.Model):
    job=models.CharField(max_length=50)
    company=models.CharField(default="Coursify",max_length=50)
    cat=models.CharField(max_length=50, default='')
    desc=models.CharField(max_length=300)
    salary=models.IntegerField(default=0)
    pub_date=models.DateField()
    expe=models.IntegerField(default=0)
    location=models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    img = models.ImageField(upload_to='user_images/')  # This will store the uploaded image
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    resume = models.FileField(upload_to='user_resumes/')  # This will store the uploaded resume
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Applicant(models.Model):
    candidate=models.IntegerField(primary_key=True)
    job_list=models.JSONField(blank=True, null=True)



class Hiring(models.Model):
    job_id=models.IntegerField(primary_key=True)
    candidate_list=models.JSONField(blank=True, null=True)


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    def __str__(self):
      return self.email


