import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import InatProvider


class InatOAuth2Adapter(OAuth2Adapter):
    provider_id = InatProvider.id
    access_token_url = 'https://www.inaturalist.org/oauth/token'  # noqa
    authorize_url = 'https://www.inaturalist.org/oauth/authorize'
    profile_url = 'https://www.inaturalist.org/users/edit.json'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(InatOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(InatOAuth2Adapter)
