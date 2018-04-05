import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import MapillaryProvider


class MapillaryOAuth2Adapter(OAuth2Adapter):
    supports_state = False
    provider_id = MapillaryProvider.id
    access_token_url = 'https://a.mapillary.com/v2/oauth/token'
    # Issue ?? -- this one authenticates over and over again...
    # authorize_url = 'https://foursquare.com/oauth2/authorize'
    authorize_url = 'https://www.mapillary.com/connect'

    def complete_login(self, request, app, token, **kwargs):
        profile_url = 'https://a.mapillary.com/v3/me'
        # Foursquare needs a version number for their API requests as
        # documented here
        # https://developer.foursquare.com/overview/versioning
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(profile_url + '?token=' + token.token + '&client_id=' + app.client_id, headers=headers)
        #    profile_url,
          #  params={'token': token.token, 'client_id': app.client_id})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(MapillaryOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(MapillaryOAuth2Adapter)
