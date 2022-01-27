from django.contrib import admin

from exemplo.models import Vunerability

# Register your models here.

@admin.register(Vunerability)
class VunerabilityAdmin(admin.ModelAdmin):
    search_fields = ('hostname', 'ip_address')
    list_filter = ('status',)
    search_fields = (
        'hostname',
        'ip_address',
        'vulnerability_severity',
        'vulnerability_cvss',
        'vulnerability_publication_date',
        'status'
    )
    list_display = (
        'hostname',
        'ip_address',
        'vulnerability_severity',
        'vulnerability_cvss',
        'vulnerability_publication_date',
        'status'
    )
