from django.conf.urls import url
from django.conf import settings
from sirtrevor import views

urlpatterns = []

if 'Image' in settings.SIRTREVOR_BLOCK_TYPES:
    urlpatterns = [
        url(
            r'^attachments/',
            views.attachment,
            name='sirtrevor_attachments',
        ),
    ]
