from django.shortcuts import render
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import generics
from api.models.availabilityModel import Availability
from api.models.curriculumModel import Curriculum
from api.models.messageModel import Message
from api.models.notificationModel import Notification
from api.models.projectModel import Project
from .pusher import pusher_client
from api.models.reviewModel import Review
from api.models.sessionModel import Session
from api.models.skillCoveredModel import SkillCovered
from .models import Mentor, Mentee, Skill, Domain
from .serializers import AvailabilitySerializer, CurriculumSerializer, MentorSerializer, MenteeSerializer, MessageSerializer, NotificationSerializer, ProjectSerializer, ReviewSerializer, SessionSerializer, SkillCoveredSerializer, SkillSerializer, DomainSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

    
@extend_schema(tags=["Users"])
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=["Users"])
class UserListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=["Users"])
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=["Logout"])
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Mentor views
@extend_schema(tags=["Mentor"])
class MentorListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

@extend_schema(tags=["Mentor"])
class MentorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


# Mentee views
@extend_schema(tags=["Mentee"])
class MenteeListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer

@extend_schema(tags=["Mentee"])
class MenteeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer


# Skill views
@extend_schema(tags=["Skills"])
class SkillListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

@extend_schema(tags=["Skills"])
class SkillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# Domain views
@extend_schema(tags=["Domain"])
class DomainListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

@extend_schema(tags=["Domain"])
class DomainRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

@extend_schema(tags=["Review"])
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema(tags=["Review"])
class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema(tags=["Skills-covered"])
class SkillCoveredListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SkillCovered.objects.all()
    serializer_class = SkillCoveredSerializer

@extend_schema(tags=["Skills-covered"])
class SkillCoveredRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SkillCovered.objects.all()
    serializer_class = SkillCoveredSerializer

@extend_schema(tags=["Project"])
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@extend_schema(tags=["Project"])
class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@extend_schema(tags=["Curriculum"])
class CurriculumListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

@extend_schema(tags=["Curriculum"])
class CurriculumRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

@extend_schema(tags=["Session"])
class SessionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@extend_schema(tags=["Session"])
class SessionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@extend_schema(tags=["Availability"])
class AvailabilityListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@extend_schema(tags=["Availability"])
class AvailabilityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@extend_schema(tags=["Notification"])
class NotificationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

@extend_schema(tags=["Notification"])
class NotificationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

@extend_schema(tags=["Message"])
class MessageAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        sender = request.data['sender']
        receiver = request.data['receiver']
        content = request.data['content']
        
        pusher_client.trigger('chat', 'message', {
            'sender': sender,
            'receiver': receiver,
            'content': content,
        })

        Message.objects.create(sender_id=sender, receiver_id=receiver, content=content)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)