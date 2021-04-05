from django.contrib import admin

# Register your models here.
from polls.models import Destination
class DestinationAdmin(admin.ModelAdmin):
       fields=['name']
       list_display=['name','place']
       list_editable=['place']
       list_filter=['place']
       search_field=['place']
       ordering=['place']
       
admin.site.register(Destination,DestinationAdmin)
