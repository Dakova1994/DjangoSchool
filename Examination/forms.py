from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Assignment,GradedAssignment,Question,Choice
### USER
class UserRegister(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','index')

class UserChange(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'password','index')
### EXAM

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','choices','answer','assignment','order')
        add_fields = ('choices') 

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'teacher')

class ChoiceForm(forms.Form):
    class Meta:
        model = Choice
        fields = ('title')
        
def add_choice_to_choices(request, Choice, question_choices ):
    question_choices.append(Choice())
    return question_choices
    
def add_question_to_assigment(request, question_assigment, assigment):
    assigment.append(question_assigment)
    return assigment


    

