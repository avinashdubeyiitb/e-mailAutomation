from django.contrib import admin
from .models import userdetail,WorkshopTeamStatus,headdetail,User

admin.site.register(userdetail)
admin.site.register(WorkshopTeamStatus)
admin.site.register(headdetail)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
