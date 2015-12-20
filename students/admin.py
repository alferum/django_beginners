from django.contrib import admin
from .models.students import Student
from .models.groups import Group
from .models.journal import Journal
from .models.exam import Exam
from .models.exam_result import Exam_result

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
admin.site.register(Exam_result)
