from django.contrib import admin
from .models import CustomUser, Lecture, Period, Instructor, Course, Exam

admin.site.title = '管理画面'
admin.site.site_header = '京大Wiki管理'
admin.site.index_title = 'メニュー'


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'date_joined', 'icon_id')


class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'group_code', 'code', 'name',
                    'semester', 'major', 'url', 'num_periods', 'course_code', 'course_numbering')


class ExamAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'name', 'field', 'drive_id', 'drive_link', 'drive_link_tag')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_numbering', 'name', 'field', 'lecture_set', 'exam_set')

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'period')
    raw_id_fields = ('lecture',)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'instructor')
    raw_id_fields = ('lecture',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)
