from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    DomainRetrieveUpdateDestroyAPIView,
    # HomePageView,
    MenteeRetrieveUpdateDestroyAPIView,
    MentorListCreateAPIView, 
    MenteeListCreateAPIView,
    MentorRetrieveUpdateDestroyAPIView,
    SkillListCreateAPIView,
    DomainListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView,
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('api/user/', UserListCreateAPIView.as_view(), name='register'),
    path('api/user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='register'),
    path('api/mentors/', MentorListCreateAPIView.as_view(), name='mentors-list-create'),
    path('api/mentors/<int:pk>/', MentorRetrieveUpdateDestroyAPIView.as_view(), name='mentors-detail'),
    path('api/mentees/', MenteeListCreateAPIView.as_view(), name='mentees-list-create'),
    path('api/mentees/<int:pk>/', MenteeRetrieveUpdateDestroyAPIView.as_view(), name='mentees-detail'),
    path('api/skills/', SkillListCreateAPIView.as_view(), name='skills-list-create'),
    path('api/skills/<int:pk>/', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skills-detail'),
    path('api/domains/', DomainListCreateAPIView.as_view(), name='domains-list-create'),
    path('api/domains/<int:pk>/', DomainRetrieveUpdateDestroyAPIView.as_view(), name='domains-detail'),
]
