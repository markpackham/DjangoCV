from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # override default app running process so signals is used with user profiles
    def ready(self):
        import main.signals