import json
import api
import module

class Pyivle(object):
    def __init__(self, apiKey, authToken=None, **kwargs):
        api.apiKey = apiKey
        if authToken: api.authToken = authToken
        #self.authToken = self._login(userid, password)

        self.module = module.module

    # TODO: authenticate and get authtoken
    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call_method(self, method, auth=True, **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params, auth=auth)
