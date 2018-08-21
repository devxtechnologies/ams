from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *

# Register your models here.

admin.site.site_header = "BMSCL AMS Admin Interface"

# Used for import_export
class UserResource(resources.ModelResource):
    class Meta:
        model = User


# Used for import_export
class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject


# Used for import_export
class TeachesResource(resources.ModelResource):
    class Meta:
        model = Teaches


@admin.register(User)
class UserAdmin(DjangoUserAdmin, ImportExportModelAdmin):

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            ("Personal info"),
            {"fields": ("first_name", "last_name", "phone", "subjects")},
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Student Information"), {"fields": ("sem", "sec", "department")}),
        (("Parent Information"), {"fields": ("father", "mother", "phone_parent")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = ("username", "first_name", "last_name", "phone", "email")
    search_fields = ("email", "first_name", "last_name", "username", "phone")
    ordering = ("id",)
    read_only = "password"
    resource_class = UserResource


@admin.register(Teaches)
class TeachesAdmin(ImportExportModelAdmin):
    list_display = (
        "teachers_first_name",
        "subject_name",
        "sem",
        "sec",
        "department_name",
    )
    search_fields = ("teacher__first_name", "subject__name", "subject__code")
    ordering = ("id",)

    def teachers_first_name(self, instance):
        return instance.teacher.first_name

    def subject_name(self, instance):
        return instance.subject.name

    def semester(self, instance):
        return instance.sem.sem

    def department_name(self, instance):
        return instance.department.name

    resource_class = TeachesResource

    class Meta:
        verbose_name_plural = "Teaches"


@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    list_display = ("name", "code", "theory", "elective")
    search_fields = ("name", "code")
    ordering = ("name",)


@admin.register(Absentees)
class AbsenteeAdmin(admin.ModelAdmin):
    list_display = (
        "user_",
        "email_",
        "attendance_date",
        "teacher_",
        "subject_",
        "sem_",
        "sec_",
        "department_",
    )
    search_fields = ("user__first_name",)
    list_filter = (
        "attendance__date_time",
        "attendance__teaches__subject__name",
        "attendance__teaches__sem",
        "attendance__teaches__sec",
    )
    ordering = ("attendance__date_time",)

    def user_(self, instance):
        return instance.user.first_name

    def email_(self, instance):
        return instance.user.email

    def attendance_date(self, instance):
        return instance.attendance.date_time

    def teacher_(self, instance):
        return instance.attendance.teaches.teacher

    def subject_(self, instance):
        return instance.attendance.teaches.subject.name

    def department_(self, instance):
        return instance.attendance.teaches.department.name

    def sem_(self, instance):
        sm = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
        }
        return sm[int(instance.attendance.teaches.sem)]

    def sec_(self, instance):
        return instance.attendance.teaches.sec

    def has_add_permission(self, request):
        return False


admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(ChangeStatus)
