from rest_framework import serializers
from .models import Lecture, Instructor, Period, Course, Exam
from rest_auth.serializers import PasswordResetSerializer

class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        data = {
            'email_template_name': 'password_reset.html',
            'subject_template_name': 'password_reset_subject.txt',
        }
        return data


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('lecture', 'instructor')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('lecture', 'period')


class LectureSerializer(serializers.ModelSerializer):
    instructor_set = InstructorSerializer(many=True, read_only=True)
    period_set = PeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Lecture
        fields = ('year', 'group_code', 'code', 'name', 'instructor_set',
                  'period_set', 'semester', 'major', 'url', 'num_periods', 'course_code', 'course_numbering')


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields =  ('course_code', 'name', 'field', 'drive_id', 'drive_link', 'drive_link_tag')

class CourseSerializer(serializers.ModelSerializer):
    lecture_set = LectureSerializer(many=True, read_only=True)
    exam_set = ExamSerializer(many=True, read_only=True)
    exam_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        read_only_fields = ['id', 'course_code', 'course_numbering', 'name', 'field', 'lecture_set', 'exam_set', 'exam_count']
        fields = ('id', 'course_code', 'course_numbering', 'name', 'field', 'lecture_set', 'exam_set', 'exam_count')
