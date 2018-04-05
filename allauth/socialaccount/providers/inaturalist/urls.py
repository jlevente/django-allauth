from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import InatProvider


urlpatterns = default_urlpatterns(InatProvider)
