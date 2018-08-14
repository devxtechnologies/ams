from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *

# Register your models here.

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject

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
    list_display = ("teachers_first_name", "subject_name", "sem", "sec", "department_name")
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


admin.site.register(Department)
admin.site.register(Absentees)
admin.site.register(Attendance)
