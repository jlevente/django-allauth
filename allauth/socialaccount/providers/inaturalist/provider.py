from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class InatAccount(ProviderAccount):

    def get_avatar_url(self):
        return None

    def to_str(self):
        dflt = super(InatAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class InatProvider(OAuth2Provider):
    id = 'inaturalist'
    name = 'Inaturalist'
    account_class = InatAccount

    def get_auth_params(self, request, action):
        data = super(InatProvider, self).get_auth_params(request, action)
        data['type'] = 'web_server'
        return data

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            email=data.get('login'),
            username=data.get('email'),
            fame=data.get('name'),
            )


provider_classes = [InatProvider]
