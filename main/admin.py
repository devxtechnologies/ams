from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone',)}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)

	list_display = ('username', 'first_name', 'last_name', 'phone', 'email')
	search_fields = ('email', 'first_name', 'last_name', 'username', 'phone')
	ordering = ('username',)