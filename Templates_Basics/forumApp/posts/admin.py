from django.contrib import admin
from posts.models import Department


@admin.register(Department)
class PostAdmin(admin.ModelAdmin):
    pass
