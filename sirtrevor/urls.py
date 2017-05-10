from django.conf.urls import url
from django.conf import settings


urlpatterns = []

if 'Image' in settings.SIRTREVOR_BLOCK_TYPES:
    from sirtrevor.views import attachment

    urlpatterns = [
        url(
            r'^attachments/',
            attachment,
            name='sirtrevor_attachments',
        ),
    ]
