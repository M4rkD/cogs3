from cogs3.settings import *

# replace shibboleth middleware with middleware mock object
idx = MIDDLEWARE.index('users.middleware.SCWRemoteUserMiddleware')
MIDDLEWARE[idx] = 'users.tests.mocks.middleware.SCWRemoteUserMiddlewareTestMock'
