from django.apps import AppConfig
from django.conf import settings
from prometheus_client import start_http_server
import django_prometheus

class DjangoPrometheusConfig(AppConfig):
    name = 'django_prometheus'
    verbose_name = 'Django Prometheus'

    def ready(self):
        port = getattr(settings, 'PROMETHEUS_METRICS_PORT')
        addr = getattr(settings, 'PROMETHEUS_METRICS_ADDRESS', '')

        if port:
            start_http_server(port, addr)
