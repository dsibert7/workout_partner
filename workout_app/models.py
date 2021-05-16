from django.db import models
import re
from datetime import date

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be more than 2 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be more than 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors['match'] = "Passwords do not match"
        EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_match'] = "Invalid email address"
        users_with_email = User.objects.filter(email=postData['email'])
        if len(users_with_email) != 0:
            errors['dup'] = "Email already exists"
        if len(postData['birthday']) == 0:
            errors['blank'] = "Please enter a date"
        return errors

class User(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    gender = models.CharField(max_length=8, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Workout(models.Model):
    # category = models.CharField(max_length=100) 
    workout_date = models.DateTimeField()
    exercise = models.CharField(max_length=100)
    weight = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)
    description = models.TextField()
    user = models.ForeignKey(User, related_name="workout", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    category = models.CharField(max_length=100) 
    workout = models.ManyToManyField(Workout, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

