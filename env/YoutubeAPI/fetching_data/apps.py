from django.apps import AppConfig


class FetchingDataConfig(AppConfig):
    name = 'fetching_data'

    def ready(self):
        from fetching_data import views
        views.start()
