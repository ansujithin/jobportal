from django.contrib import admin
from testApp.models import Jobs

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display=['loc','title','Desc','sal']

admin.site.register(Jobs, JobsAdmin)
