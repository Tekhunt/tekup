from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .views import (
    AvailabilityListCreateAPIView,
    AvailabilityRetrieveUpdateDestroyAPIView,
    CurriculumListCreateAPIView,
    CurriculumRetrieveUpdateDestroyAPIView,
    DomainRetrieveUpdateDestroyAPIView,
    LogoutView,
    MenteeRetrieveUpdateDestroyAPIView,
    MentorListCreateAPIView,
    MenteeListCreateAPIView,
    MentorRetrieveUpdateDestroyAPIView,
    MessageAPIView,
    NotificationListCreateAPIView,
    NotificationRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
    SessionListCreateAPIView,
    SessionRetrieveUpdateDestroyAPIView,
    SkillCoveredListCreateAPIView,
    SkillCoveredRetrieveUpdateDestroyAPIView,
    SkillListCreateAPIView,
    DomainListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView,
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("api/usercreate/", UserCreateAPIView.as_view(), name="register"),
    path("api/users/", UserListAPIView.as_view(), name="user-list"),
    path(
        "api/user/<int:pk>/",
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name="single-user",
    ),
    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair_after_login",
    ),
    path("api/logout/", LogoutView.as_view(), name="auth_logout"),
    path("api/mentors/", MentorListCreateAPIView.as_view(), name="mentors-list-create"),
    path(
        "api/mentors/<int:pk>/",
        MentorRetrieveUpdateDestroyAPIView.as_view(),
        name="mentors-detail",
    ),
    path("api/mentees/", MenteeListCreateAPIView.as_view(), name="mentees-list-create"),
    path(
        "api/mentees/<int:pk>/",
        MenteeRetrieveUpdateDestroyAPIView.as_view(),
        name="mentees-detail",
    ),
    path("api/skills/", SkillListCreateAPIView.as_view(), name="skills-list-create"),
    path(
        "api/skills/<int:pk>/",
        SkillRetrieveUpdateDestroyAPIView.as_view(),
        name="skills-detail",
    ),
    path("api/domains/", DomainListCreateAPIView.as_view(), name="domains-list-create"),
    path(
        "api/domains/<int:pk>/",
        DomainRetrieveUpdateDestroyAPIView.as_view(),
        name="domains-detail",
    ),
    path("api/reviews/", ReviewListCreateAPIView.as_view(), name="review-list-create"),
    path(
        "api/reviews/<int:pk>/",
        ReviewRetrieveUpdateDestroyAPIView.as_view(),
        name="review-retrieve-update-destroy",
    ),
    path(
        "api/skills-covered/",
        SkillCoveredListCreateAPIView.as_view(),
        name="skill_covered_list_create",
    ),
    path(
        "api/skills-covered/<int:pk>/",
        SkillCoveredRetrieveUpdateDestroyAPIView.as_view(),
        name="skill_covered_retrieve_update_destroy",
    ),
    path(
        "api/curriculum/",
        CurriculumListCreateAPIView.as_view(),
        name="curriculum_list_create",
    ),
    path(
        "api/curriculum/<int:pk>/",
        CurriculumRetrieveUpdateDestroyAPIView.as_view(),
        name="curriculum_retrieve_update_destroy",
    ),
    path(
        "api/project/", ProjectListCreateAPIView.as_view(), name="project_list_create"
    ),
    path(
        "api/project/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project_retrieve_update_destroy",
    ),
    path(
        "api/session/", SessionListCreateAPIView.as_view(), name="session_list_create"
    ),
    path(
        "api/session/<int:pk>/",
        SessionRetrieveUpdateDestroyAPIView.as_view(),
        name="session_retrieve_update_destroy",
    ),
    path(
        "api/availability/",
        AvailabilityListCreateAPIView.as_view(),
        name="availability_list_create",
    ),
    path(
        "api/availability/<int:pk>/",
        AvailabilityRetrieveUpdateDestroyAPIView.as_view(),
        name="availability_retrieve_update_destroy",
    ),
    path(
        "api/notifications/",
        NotificationListCreateAPIView.as_view(),
        name="notification_list",
    ),
    path(
        "api/notifications/mark-read/",
        NotificationRetrieveUpdateDestroyAPIView.as_view(),
        name="notification_mark_read",
    ),
    path("api/messages", MessageAPIView.as_view(), name="messages"),
]
