from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Technology, Member, Designation, Project, ContactUs, \
 Registration, Branch, Gender, Year,Domain, ContactInfo, Blog, Event, EmailContent, \
 EmailAttachment, AlumniRegistration
# from .forms import RegistrationForm

admin.site.site_header = "Software Incubator Administration"

class RegistrationAdmin(ImportExportActionModelAdmin):
    readonly_fields = ('timestamp',)
    list_display = (
            'name', 'college_email', 'branch', 'student_number', 'event', 'is_paid', 'mail_sent_status')
    search_fields = ('student_number', 'name')
    list_filter = ('event','mail_sent_status','is_paid','is_hosteler','gender')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'code')


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
admin.site.register(Domain)
admin.site.register(Year, YearAdmin)
admin.site.register(ContactInfo)
admin.site.register(Blog)
admin.site.register(EmailAttachment)
admin.site.register(EmailContent)
admin.site.register(AlumniRegistration)