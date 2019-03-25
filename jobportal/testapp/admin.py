from django.contrib import admin
from testapp.models import hydjobs,bangalorejobs,chennaijobs,keralajobs,punejobs
class hydjobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]
class bangalorejobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]
class chennaijobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]
class keralajobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]
class punejobsAdmin(admin.ModelAdmin):
    list_display=["date","company","title","eligibility","address","email","phonenumber"]

# Register your models here.
admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangalorejobs,bangalorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(keralajobs,keralajobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
