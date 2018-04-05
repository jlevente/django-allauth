from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class MapillaryAccount(ProviderAccount):
    def get_avatar_url(self):
        #return self.account.extra_data.get('photo')
        return None

    def to_str(self):
        dflt = super(MapillaryAccount, self).to_str()
        return self.account.extra_data.get('username', dflt)


class MapillaryProvider(OAuth2Provider):
    id = 'mapillary'
    name = 'Mapillary'
    account_class = MapillaryAccount

    def get_auth_params(self, request, action):
        data = super(MapillaryProvider, self).get_auth_params(request, action)
        data['scope'] = 'user:read'
        data['response_type'] = 'token'
        return data

    def extract_uid(self, data):
        return str(data['key'])

    def extract_common_fields(self, data):
        return dict(username=data.get('username'))


provider_classes = [MapillaryProvider]
