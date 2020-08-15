from django.apps import AppConfig


class CentralConfig(AppConfig):
    name = 'central'

    def ready(self):
        import json_maker
        json_maker.start()