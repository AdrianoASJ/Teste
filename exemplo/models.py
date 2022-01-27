from email.policy import default
from django.db import models
from exemplo.choices import STATUS_SISTEMA, NAO_CORRIGIDO, STATUS_DE_RISCO

class Vunerability(models.Model):
    hostname = models.CharField('Hostname', max_length=255)
    ip_address = models.TextField(verbose_name='Ip Address', blank=True, null=True)
    vulnerability_severity = models.IntegerField(verbose_name="Severity", choices=STATUS_DE_RISCO, blank=True, null=True)
    vulnerability_cvss = models.FloatField(verbose_name='CVSS', blank=True, null=True)
    vulnerability_publication_date = models.DateField(verbose_name='Publication Date', blank=True, null=True)
    status = models.IntegerField(choices=STATUS_SISTEMA, default=NAO_CORRIGIDO)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = 'Vulnerabilidade'
        verbose_name_plural = 'Vulnerabilidade'