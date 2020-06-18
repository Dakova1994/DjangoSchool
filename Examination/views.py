from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import UserRegister, QuestionForm,AssignmentForm
from http import HTTPStatus
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import User,Assignment,GradedAssignment,Question,Choice
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

class SignUpView(CreateView):
    form_class = UserRegister
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@method_decorator(staff_member_required, name='dispatch')
class QuestionView(CreateView):
    form_class = QuestionForm
    template_name = 'question.html'

class AssignmentView(CreateView):
    form_class = AssignmentForm
    template_name = 'assignment.html'

    def get_success_url(self):
        return reverse('home')



def get_questions(request, question_id):
    return HttpResponse("Question %s." % question_id)
    
    
    
    
    
    
    
    # def create(self, request):
    #     serializer = AssignmentForm(data=request.data.data)
    #     if serializer.is_valid():
    #         assignment = serializer.create(request)
    #         if assignment:
    #             return HttpResponse(status=201)
    #         return Http404('<h1>Page not found</h1>')

# class AssignmentViewSet(CreateView):
#     form_class = AssignmentForm
#     success_url = reverse_lazy('assignments')
#     template_name = 'assignment.html'
#     def create(self, request):
#         serializer = AssignmentForm(data=request.data)
#         if serializer.is_valid():
#             assignment = serializer.create(request)
#             if assignment:
#                 return HttpResponse(status=201)
#         return Http404('<h1>Page not found</h1>')
    



# class GradedAssignmentListView(ListView):
#     get_template_names = GradedAssignmentForm

#     def get_queryset(self):
#         queryset = GradedAssignment.objects.all()
#         username = self.request.query_params.get('username', None)
#         if username is not None:
#             queryset = queryset.filter(student__username=username)
#         return queryset

# class GradedAssignmentCreateView(CreateView):
#     get_template_names = GradedAssignmentForm
#     queryset = GradedAssignment.objects.all()

#     def post(self, request):
#         print(request.data)
#         serializer = GradedAssignmentForm(data=request.data)
#         serializer.is_valid()
#         graded_assignment = serializer.create(request)
#         if graded_assignment:
#             return HttpResponse(status=201)
#         return Http404('<h1>Page not found</h1>')