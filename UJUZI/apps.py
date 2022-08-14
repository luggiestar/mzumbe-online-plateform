from dal.test.utils import fixtures
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UjuziConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UJUZI'

    def ready(self):
        post_migrate.connect(fixtures, sender=self)

    def ready(self):
        import UJUZI.signals