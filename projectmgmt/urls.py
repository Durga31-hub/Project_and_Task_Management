from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    MilestoneViewSet,
    TaskViewSet,
    TaskCommentViewSet,
    TimeLogViewSet,
    ProjectAssignmentViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'milestones', MilestoneViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', TaskCommentViewSet)
router.register(r'timelogs', TimeLogViewSet)
router.register(r'assignments', ProjectAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
