from django.contrib import admin
from . import models
from .models import Profile
# Register your models here.


@admin.register(models.UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email', 'is_staff')


admin.site.register(Profile)
