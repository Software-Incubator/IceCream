from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Technology, Member, Designation, Project, ContactUs, \
    Registration, Event, Branch, Gender, Year, ContactInfo, Blog



class RegistrationAdmin(ImportExportActionModelAdmin):
    readonly_fields = ('timestamp',)
    list_display = (
    'name', 'student_number', 'branch', 'year', 'event', 'fee_paid')
    search_fields = ('student_number', 'name')
    list_filter = ('event','fee_paid')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class YearAdmin(admin.ModelAdmin):
    list_display = ('value', 'active')


admin.site.register(Technology)
admin.site.register(Member)
admin.site.register(Designation)
admin.site.register(Project)
admin.site.register(ContactUs)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Gender)
admin.site.register(Year, YearAdmin)
admin.site.register(ContactInfo)
admin.site.register(Blog)

