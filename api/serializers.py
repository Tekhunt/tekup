from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models.availabilityModel import Availability
from api.models.curriculumModel import Curriculum

from api.models.customUserModel import User
from api.models.messageModel import Message
from api.models.notificationModel import Notification
from api.models.projectModel import Project
from api.models.reviewModel import Review
from api.models.sessionModel import Session
from .models import Mentor, Mentee, Skill, Domain


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_mentor",
            "is_mentee",
        ]

        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super.update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class MentorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = SkillSerializer(many=True)
    domain = DomainSerializer(many=True)

    class Meta:
        model = Mentor
        fields = "__all__"


class MenteeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = SkillSerializer(many=True)
    domain = DomainSerializer(many=True)

    class Meta:
        model = Mentee
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(many=True)
    mentor = MenteeSerializer(many=True)

    class Meta:
        model = Review
        fields = "__all__"


class SkillCoveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CurriculumSerializer(serializers.ModelSerializer):
    domain = DomainSerializer(many=True)

    class Meta:
        model = Curriculum
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(many=True)
    mentee = MenteeSerializer(many=True)

    class Meta:
        model = Session
        fields = "__all__"


class AvailabilitySerializer(serializers.ModelSerializer):
    mentor = MentorSerializer(many=True)
    mentee = MenteeSerializer(many=True)

    class Meta:
        model = Availability
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)

    class Meta:
        model = Notification
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
