from django.apps import AppConfig
from django.conf import settings
from prometheus_client import start_http_server
import django_prometheus_metrics

class DjangoPrometheusConfig(AppConfig):
    name = 'django_prometheus_metrics'
    verbose_name = 'Django Prometheus Metrics'

    def ready(self):
        port = getattr(settings, 'PROMETHEUS_METRICS_PORT', None)
        addr = getattr(settings, 'PROMETHEUS_METRICS_ADDRESS', '')

        if port:
            start_http_server(port, addr)
