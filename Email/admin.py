from django.contrib import admin

from .models import Email


class EmailAdmin(admin.ModelAdmin):
    readonly_fields = (
        'from',
        'to',
        'html',
        # 'sender_ip',
        'subject',
        'text'
    )
    list_display = (
        'subject',
        'from',
        'to'
    )

admin.site.register(Email, EmailAdmin)