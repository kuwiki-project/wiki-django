from django_filters import rest_framework as filters
from .models import Course


class CourseFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    field = filters.CharFilter(field_name='field', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='lecture__year', lookup_expr='exact')
    instructor = filters.CharFilter(
        field_name='lecture__instructor__instructor', lookup_expr='icontains')
    period = filters.CharFilter(
        field_name='lecture__period__period', lookup_expr='icontains')
    semester = filters.CharFilter(field_name='semester', lookup_expr='icontains')
    major = filters.CharFilter(field_name='major', lookup_expr='icontains')
    exam_count = filters.NumberFilter(field_name='exam_count', lookup_expr='gt')

    class Meta:
        model = Course
        fields = ['name', 'field', 'year', 'instructor', 'period', 'semester', 'major', 'exam_count']
