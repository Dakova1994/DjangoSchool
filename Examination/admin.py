from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserChange, UserRegister,ChoiceForm, AssignmentForm
from .models import User
from .models import Choice, Question, Assignment, GradedAssignment

class AbstractUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username','index', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('username','index')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    model = User
    list_display = ['username','index']
    search_fields = ( 'username','index')
    ordering = ('username','index')
    add_form = UserRegister
    form = UserChange

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    add_form = ChoiceForm
    form = AssignmentForm
    add_fieldsets = (
        (None, {
            'fields': ('question','answer', 'choices')
        })
    )  
    fieldsets = (
        (None, {
            'fields': ('question','choices')
        }),(None, {
            'fields': ('answer','order')})
    )  
    
    ordering = ('assignment','question')


admin.site.register(User, AbstractUserAdmin)
admin.site.register(Question, QuestionAdmin)

admin.site.register(Assignment)
admin.site.register(GradedAssignment)
