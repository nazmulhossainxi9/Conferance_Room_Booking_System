from django.contrib import admin
from .models import Classroom, MasLAB, BdOSN

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'booked_by', 'email', 'phone', 'date', 'start_time', 'end_time')
    search_fields = ('title', 'email', 'phone')
    list_filter = ('date',)

@admin.register(BdOSN)
class MasLABAdmin(admin.ModelAdmin):
    list_display = ('title', 'booked_by', 'email', 'phone', 'date', 'start_time', 'end_time')
    search_fields = ('title', 'email', 'phone')
    list_filter = ('date',)

@admin.register(MasLAB)
class BdOSNAdmin(admin.ModelAdmin):
    list_display = ('title', 'booked_by', 'email', 'phone', 'date', 'start_time', 'end_time')
    search_fields = ('title', 'email', 'phone')
    list_filter = ('date',)