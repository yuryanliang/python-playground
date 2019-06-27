import time
from urllib.parse import urljoin
import requests



class O365Portal(object):
    def __init__(self, tenant_id, endpoint):
        self._tenant_id = tenant_id
        self._endpoint = endpoint


class O365LoginPortal(O365Portal):
    def __init__(self, tenant_id, endpoint):
        super(O365LoginPortal, self).__init__(tenant_id, endpoint)
        path = '/{}/oauth2/token'.format(self._tenant_id)
        self._url = urljoin(self._endpoint, path)

    def get_token_by_psk(self, client_id, client_secret, resource, session):
        response = session.post(self._url, data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'resource': resource
        })

        content = response.json()
        token=O365Token(**content)
        return token



class O365TokenProvider(object):
    def __init__(self, resource, policy):
        self._resource = resource
        self._policy = policy
        self._token = None

    def set_auth_header(self, session):
        session.headers.update({
            'Authorization': '{} {}'.format(
                self._token.token_type,
                self._token.access_token
            )
        })
        return session

    def get_access_token(self):
        return '{} {}'.format(
            self._token.token_type,
            self._token.access_token
        )

    def set_access_token(self, session, access_token):
        session.headers.update({'Authorization': access_token})
        return session

    def auth(self, session):
        self._token = self._policy(self._resource, session)
        return self.set_auth_header(session)

    def need_retire(self, min_ttl):
        if not self._token:
            return True
        return self._token.need_retire(min_ttl)

class O365Token(object):
    def __init__(self, token_type, access_token, expires_on, **kwargs):
        self._token_type = token_type
        self._access_token = access_token
        self._expires_on = int(expires_on)
        self._now = time.time

    def ttl(self):
        return self._expires_on - self._now()

    def need_retire(self, min_ttl):
        # test if the current token has enough 'buffer' time before it expires
        return self.ttl() < min_ttl

    @property
    def token_type(self):
        return self._token_type

    @property
    def access_token(self):
        return self._access_token

    @property
    def expires_on(self):
        return self._expires_on

if __name__ == "__main__":
    endpoint = 'https://login.microsoftonline.com'
    tenant_id = '2ed28a74-1f6f-4829-8530-fe359c77d35c'

    client_id = 'e15d091b-990e-49fe-90e9-393445c0fcd4'
    client_secret = 'eg/z1x/Jh3P/iHs3rfnfsObTyvk3vhk16jIKEQo1nrk='
    resource = 'https://manage.office.com'
    login = O365LoginPortal(tenant_id, endpoint)
    session = requests.session()
    token = login.get_token_by_psk(client_id, client_secret, resource, session)




    1 == 1
