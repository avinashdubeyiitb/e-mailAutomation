from django.contrib import admin
from .models import WorkshopTeamStatus,User

admin.site.register(WorkshopTeamStatus)

<<<<<<< HEAD
#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
#    pass
=======
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
>>>>>>> 994864d3023cc34149e236b878e43e446fec56ee
