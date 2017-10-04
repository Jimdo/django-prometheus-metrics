from setuptools import setup, find_packages

setup(
    name='django-prometheus-metrics',
    version='0.0.1',
    packages=find_packages(),
    license='MIT License',
    description='Monitoring middleware for prometheus.',
    long_description="""Django-Prometheus-Metrics
This library lets you expose metrics in your django application for Prometheus consumption.
See https://github.com/Jimdo/django-prometheus-metrics
""",
    url='https://github.com/Jimdo/django-prometheus-metrics',
    author='Jimdo GmbH',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "prometheus_client>=0.0.21",
    ],
    test_suite='runtests.runtests',
)
