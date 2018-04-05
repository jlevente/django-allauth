import requests
import xml.etree.ElementTree as ET

from allauth.socialaccount.providers.oauth.views import (OAuthAdapter,
                                                          OAuthLoginView,
                                                          OAuthCallbackView)
from allauth.socialaccount.providers.oauth.client import OAuth
from .provider import OSMProvider


class OSMApi(OAuth):
    def get_user_info(self):
        profile_url = 'https://api.openstreetmap.org/api/0.6/user/details'
        raw_xml = self.query(profile_url)
        return ET.fromstring(raw_xml)

class OSMOAuthAdapter(OAuthAdapter):
    provider_id = OSMProvider.id
    request_token_url = 'https://www.openstreetmap.org/oauth/request_token'
    access_token_url = 'https://www.openstreetmap.org/oauth/access_token'
    authorize_url = 'https://www.openstreetmap.org/oauth/authorize'

    def complete_login(self, request, app, token, **kwargs):
        client = OSMApi(request, app.client_id, app.secret, self.request_token_url)
        #headers = {'Authorization': '{0}'.format(token.token)}
        user_data = client.get_user_info()

        user = user_data.find('user')
        extra_data = user.attrib
        extra_data['description'] = user.find('description').text
        extra_data['changeset_count'] = user.find('changesets').attrib['count']
        extra_data['traces_count'] = user.find('traces').attrib['count']
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth_login = OAuthLoginView.adapter_view(OSMOAuthAdapter)
oauth_callback = OAuthCallbackView.adapter_view(OSMOAuthAdapter)
