from django.conf.urls import url
from django_prometheus.views import MetricsView

urlpatterns = [
    url(r'^metrics$', MetricsView.as_view(), name='prometheus-django-metrics')
]