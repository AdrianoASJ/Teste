from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin
from datetime import datetime
from exemplo.choices import STATUS_DE_RISCO, LOW, MIDIUM, HIGH, DANGER

from exemplo.models import Vunerability

# Register your models here.

class VunerabilityResource(resources.ModelResource):
    hostname = Field(attribute='hostname', column_name='ASSET - HOSTNAME')
    ip_address = Field(attribute='ip_address', column_name='ASSET - IP_ADDRESS')
    title = Field(attribute='title', column_name='VULNERABILITY - TITLE')
    vulnerability_severity = Field(attribute='vulnerability_severity', column_name='VULNERABILITY - SEVERITY')
    vulnerability_cvss = Field(attribute='vulnerability_cvss', column_name='VULNERABILITY - CVSS')
    vulnerability_publication_date = Field(attribute='vulnerability_publication_date', column_name='VULNERABILITY - PUBLICATION_DATE')

    class Meta:
        model = Vunerability

    def before_import_row(self, row, **kwargs):
        if row['VULNERABILITY - SEVERITY'] == 'Baixo':
            row['VULNERABILITY - SEVERITY'] = LOW
        if row['VULNERABILITY - SEVERITY'] == 'Médio':
            row['VULNERABILITY - SEVERITY'] = MIDIUM
        if row['VULNERABILITY - SEVERITY'] == 'Alto':
            row['VULNERABILITY - SEVERITY'] = HIGH
        if row['VULNERABILITY - SEVERITY'] == 'Crítico':
            row['VULNERABILITY - SEVERITY'] = DANGER
        if row['VULNERABILITY - PUBLICATION_DATE']:
            my_date = datetime.strptime(row['VULNERABILITY - PUBLICATION_DATE'], '%Y-%m-%d')
            row['VULNERABILITY - PUBLICATION_DATE'] = my_date


class VunerabilityAdmin(ImportExportActionModelAdmin):
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
    resource_class = VunerabilityResource


admin.site.register(Vunerability, VunerabilityAdmin)