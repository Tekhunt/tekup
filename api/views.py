from django.shortcuts import render
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import generics
from api.models.availabilityModel import Availability
from api.models.curriculumModel import Curriculum
from api.models.notificationModel import Notification
from api.models.projectModel import Project

from api.models.reviewModel import Review
from api.models.sessionModel import Session
from api.models.skillCoveredModel import SkillCovered
from .models import Mentor, Mentee, Skill, Domain
from .serializers import AvailabilitySerializer, CurriculumSerializer, MentorSerializer, MenteeSerializer, NotificationSerializer, ProjectSerializer, ReviewSerializer, SessionSerializer, SkillCoveredSerializer, SkillSerializer, DomainSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# @extend_schema(tags=["Home"])
# class HomePageView(APIView):
#     def get(self, request):
#         message = {"message": "Visit our endpoints at www.tekup/api/your-favorite-resource and start exploring today!"}
#         return Response(message)
class RegisterApi(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                UserSerializer(user, context=self.get_serializer_context()).data
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@extend_schema(tags=["Users"])
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=["Users"])
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Mentor views
@extend_schema(tags=["Mentor"])
class MentorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

@extend_schema(tags=["Mentor"])
class MentorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


# Mentee views
@extend_schema(tags=["Mentee"])
class MenteeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer

@extend_schema(tags=["Mentee"])
class MenteeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer


# Skill views
@extend_schema(tags=["Skills"])
class SkillListCreateAPIView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

@extend_schema(tags=["Skills"])
class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# Domain views
@extend_schema(tags=["Domain"])
class DomainListCreateAPIView(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

@extend_schema(tags=["Domain"])
class DomainRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

@extend_schema(tags=["Review"])
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema(tags=["Review"])
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema(tags=["Skills-covered"])
class SkillCoveredListCreateAPIView(generics.ListCreateAPIView):
    queryset = SkillCovered.objects.all()
    serializer_class = SkillCoveredSerializer

@extend_schema(tags=["Skills-covered"])
class SkillCoveredRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillCovered.objects.all()
    serializer_class = SkillCoveredSerializer

@extend_schema(tags=["Project"])
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@extend_schema(tags=["Project"])
class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@extend_schema(tags=["Curriculum"])
class CurriculumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

@extend_schema(tags=["Curriculum"])
class CurriculumRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

@extend_schema(tags=["Session"])
class SessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@extend_schema(tags=["Session"])
class SessionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@extend_schema(tags=["Availability"])
class AvailabilityListCreateAPIView(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@extend_schema(tags=["Availability"])
class AvailabilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@extend_schema(tags=["Notification"])
class NotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

@extend_schema(tags=["Notification"])
class NotificationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer