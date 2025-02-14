from django.apps import AppConfig


class ChawtsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chawtsApp'

    def ready(self):
        import chawtsApp.signals
