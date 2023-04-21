from django.shortcuts import render
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import generics
from .models import Mentor, Mentee, Skill, Domain
from .serializers import MentorSerializer, MenteeSerializer, SkillSerializer, DomainSerializer
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
