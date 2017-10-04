from django.db.models import CharField, Model
from django_prometheus_metrics.middleware import PrometheusBeforeMiddleware
from django_prometheus_metrics.models import MetricsModelMixin
from django.test import TestCase
from prometheus_client import REGISTRY as registry

def get_metric(name, **labels):
    for metric in registry.collect():
        for k, l, v in metric.samples:
            if k == name and l == labels:
                return v
    return None

def get_metric_vector(name):
    result = []
    for metric in registry.collect():
        for k, l, v in metric.samples:
            if k == name:
                result.append((l, v))
    return result


class MiddlewareTestCase(TestCase):
    def test_process(self):
        # do two calls at least as after just one the histogram won't get exposed.
        self.client.get('/metrics')
        response = self.client.get('/metrics')

        val = get_metric('django_http_requests_total', status_code='200', method='GET', view='prometheus_django_metrics')
        self.assertEqual(val, 2)
        self.assertIn('django_http_requests_total', str(response.content))

        # take a random histogram val, in this case sum.
        val = get_metric('django_http_requests_latency_seconds_sum', status_code='200', method='GET', view='prometheus_django_metrics')
        self.assertGreater(val, 0)
        self.assertIn('django_http_requests_latency_seconds_sum', str(response.content))



class TestModel(MetricsModelMixin('test'), Model):
        name = CharField(max_length=100, unique=True)

class ModelMixinTestCase(TestCase):
    def test_mixin(self):
        t = TestModel()
        t.name = "foobar"
        t.save()
        val = get_metric('django_model_inserts_total', model='test')
        self.assertEqual(val, 1)

