from django.urls import path, include

from .views import Index, Detail

urlpatterns = [
        # /portfolio/
        path("", Index.as_view(), name='index'),
        # /portfolio/<slug>
        path("<slug:slug>", Detail.as_view(), name='detail')
        ]
