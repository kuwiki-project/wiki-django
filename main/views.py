from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import CourseSerializer, ExamSerializer, InstructorSerializer, PeriodSerializer, LectureSerializer
from .models import Course, Lecture, Exam, Instructor, Period
from .filters import CourseFilter
from django.db.models import Prefetch, Q, Count

from functools import reduce
from operator import and_


class CourseViewSet(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CourseSerializer
    filter_class = CourseFilter
    queryset = Course.objects.all()

    def get_queryset(self):
        q = super(CourseViewSet, self).get_queryset().prefetch_related(Prefetch("lecture_set", queryset=Lecture.objects.all(
        ).prefetch_related("period_set", "instructor_set").order_by("-id")), "exam_set").annotate(exam_count=Count('exam', distinct=True)).order_by("-id")
        search_word = self.request.query_params.get('search', None)
        if search_word is not '' and search_word is not None:
            q_list = search_word.split()
            query = reduce(and_, [Q(name__icontains=q) | Q(field__icontains=q) | Q(lecture__year__icontains=q) | Q(lecture__instructor__instructor__icontains=q) | Q(lecture__period__period__icontains=q) | Q(lecture__semester__icontains=q) | Q(lecture__major__icontains=q) for q in q_list]
                           )
            return q.filter(query)
        return q

class ExamViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

class LectureViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()

    def get_queryset(self):
        return super(LectureViewSet, self).get_queryset().prefetch_related("period_set", "instructor_set")


class PeriodViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

class InstructorViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, )
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
