from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'mobile', 'city', 'interested_model', 'source',
        'preferred_contact_time', 'status', 'email_sent', 'created_at',
    )
    list_filter = ('source', 'status', 'interested_model', 'created_at')
    search_fields = ('name', 'mobile', 'city', 'message')
    list_editable = ('status',)
    readonly_fields = ('email_sent', 'created_at', 'updated_at')
    ordering = ('-created_at',)