from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from main.views import CourseViewSet, ExamViewSet, LectureViewSet, PeriodViewSet, InstructorViewSet

router = routers.DefaultRouter()
router.register(r'exam', ExamViewSet)
router.register(r'lecture', LectureViewSet)
router.register(r'period', PeriodViewSet)
router.register(r'instructor', InstructorViewSet)

urlpatterns = [
    url(r'^course/', CourseViewSet.as_view()),
]
