from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    index = models.PositiveIntegerField(blank=True, null=True)
    # is_student = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    def __str__(self):
        return self.username

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     gradedAssignment = ManyToManyField(GradedAssignment)

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}
        )
    def __str__(self):
        return self.title


class GradedAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student


class Choice(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question
