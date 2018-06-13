from users.middleware import SCWRemoteUserMiddleware
from institution.models import Institution

class SCWRemoteUserMiddlewareTestMock(SCWRemoteUserMiddleware):

    def process_request(self, request):
        """ Allows testing without a shibboleth server. Allows logging in as a shibboleth user by passing user email as a HTTP header REMOTE_USER in test """
        try:
            username = request.META['HTTP_REMOTE_USER']
            request.META['REMOTE_USER'] = username

            _, domain = username.split('@')
            institution = Institution.objects.get(base_domain=domain)

            request.META['Shib-Identity-Provider'] = institution.identity_provider
        except KeyError:
            pass
        super().process_request(request)
