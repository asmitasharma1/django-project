from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Complaint, MissingPerson
from .models import PoliceOfficer

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

# Remove any previous registration of User with auth.UserAdmin
admin.site.unregister(User)

class PoliceOfficerAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge_number', 'name', 'rank', 'department')

admin.site.register(PoliceOfficer, PoliceOfficerAdmin)

# Register your User model with your custom admin class
admin.site.register(User, CustomUserAdmin)


admin.site.register(Complaint)
admin.site.register(MissingPerson)
