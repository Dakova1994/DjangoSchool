from django.urls import path
from django.conf.urls import url
from .views import SignUpView, QuestionView,AssignmentView
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('question/', QuestionView.as_view(), name='question'),
    # url(r'', AssignmentViewSet, name='assignments'),
    path('assignment/', AssignmentView.as_view(), name='assignment'),
]