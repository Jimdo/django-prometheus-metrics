from django.conf.urls import url
from django_prometheus_metrics.views import MetricsView

urlpatterns = [
    url(r'^metrics$', MetricsView.as_view(), name='prometheus-django-metrics')
]