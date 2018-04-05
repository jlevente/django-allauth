from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import MapillaryProvider


urlpatterns = default_urlpatterns(MapillaryProvider)
