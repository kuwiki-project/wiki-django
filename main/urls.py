from django.urls import path
from rest_framework import routers
from main.views import CourseViewSet, ExamViewSet, LectureViewSet, PeriodViewSet, InstructorViewSet

router = routers.DefaultRouter()
router.register('exam', ExamViewSet)
router.register('lecture', LectureViewSet)
router.register('period', PeriodViewSet)
router.register('instructor', InstructorViewSet)

urlpatterns = [
    path('course/', CourseViewSet.as_view()),
]
