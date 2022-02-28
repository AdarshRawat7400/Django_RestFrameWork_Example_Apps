from django.apps import AppConfig


class LibraryappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LibraryApp'

    def ready(self):
        import LibraryApp.signals
