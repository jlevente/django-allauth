from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider


class OSMAccount(ProviderAccount):

    def get_avatar_url(self):
        return None

    def to_str(self):
        dflt = super(OSMAccount, self).to_str()
        return self.account.extra_data.get('display_name', dflt)


class OSMProvider(OAuthProvider):
    id = 'openstreetmap'
    name = 'OpenStreetMap'
    package = 'allauth.socialaccount.providers.openstreetmap'
    account_class =OSMAccount

    def get_auth_params(self, request, action):
        data = super(OSMProvider, self).get_auth_params(request, action)
        #data['oauth_token'] = token.token
        return data

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            username=data.get('display_name'),
        )


providers.registry.register(OSMProvider)
