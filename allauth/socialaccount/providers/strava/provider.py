from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class StravaAccount(ProviderAccount):

    def to_str(self):
        dflt = super(StravaAccount, self).to_str()
        return self.account.extra_data.get('username', dflt)


class StravaProvider(OAuth2Provider):
    id = 'strava'
    name = 'Strava'
    account_class = StravaAccount

    def get_auth_params(self, request, action):
        data = super(StravaProvider, self).get_auth_params(request, action)
        data['scope'] = "view_private"
        return data

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            email=data.get('email'),
            username=data.get('username'),
            first_name=data.get('firstname'),
            last_name=data.get('lastname'),
            name="%s %s" % (data.get('firstname'), data.get('lastname')),
        )


provider_classes = [StravaProvider]
