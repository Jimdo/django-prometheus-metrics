# django-prometheus-metrics

Export Django monitoring metrics for Prometheus consumption.

## Requirements

- Django: `2.2`
- Python `3.6`, `3.8`

## Installation

Install the package via pip:

```
pip install django-prometheus-metrics
```

Add it to your apps:

```
INSTALLED_APPS = (
    # ...
    'django_prometheus_metrics',
    # ...
)
```

Register the middleware:

```
MIDDLEWARE_CLASSES = (
    'django_prometheus_metrics.middleware.PrometheusBeforeMiddleware',
    # All your other middlewares go here
    # ...
)
```

Add the urls:

```
urlpatterns = [
    # ...
    url('', include('django_prometheus_metrics.urls')),
    # ...
]
```

## Exported metrics

| Name                                 | Type      | Labels                          | Description                           |
| ------------------------------------ | --------- | ------------------------------- | ------------------------------------- |
| django_http_requests_total           | Counter   | `status_code`, `method`, `view` | Total count of requests               |
| django_http_requests_latency_seconds | Histogram | `status_code`, `method`, `view` | Histogram of requests processing time |
| django_model_inserts_total           | Counter   | `model`                         | Number of inserts on a certain model  |
| django_model_updates_total           | Counter   | `model`                         | Number of updates on a certain model  |
| django_model_deletes_total           | Counter   | `model`                         | Number of deletes on a certain model  |

### Exproting model metrics

In order to monitor a certain model your model has to inherit from the `MetricsModelMixin` in addition to the django model class:

```
from django_prometheus_metrics.models import MetricsModelMixin

class Car(MetricsModelMixin('car'), models.Model):
    name = models.CharField(max_length=100, unique=True)
    # ...
```
