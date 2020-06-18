<<<<<<< HEAD
#from django.contrib import admin
#from .models import WorkshopTeamStatus,memberdetail

#admin.site.register(WorkshopTeamStatus)
#admin.site.register(memberdetail)
=======
from django.contrib import admin
from .models import userdetail,WorkshopTeamStatus,headdetail,User

admin.site.register(userdetail)
admin.site.register(WorkshopTeamStatus)
admin.site.register(headdetail)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
>>>>>>> 22b6358d3431b3e2f6e4825c25263330da131012
