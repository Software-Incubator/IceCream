from django.contrib import admin
from models import Technology, Member, Designation, Project, ContactUs, Registration, Event, Branch


class RegistrationAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )


admin.site.register(Technology)
admin.site.register(Member)
admin.site.register(Designation)
admin.site.register(Project)
admin.site.register(ContactUs)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Event)
admin.site.register(Branch)