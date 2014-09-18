import json
import api
import login

class Pyivle(object):
    def __init__(self, apiKey, **kwargs):
        self.apiKey = apiKey
        self.authToken = None
        #self.authToken = self._login(userid, password)

    # TODO: authenticate and get authtoken
    def login(self, userid, password):
        self.authToken = api.get_auth_token(self.apiKey, userid, password)
    
    # Adds authentication parameters to parameter list
    # TODO: raise exception if authtoken not set
    def add_auth(self, params):
        params['apikey'] = self.apiKey
        params['authtoken'] = self.authToken
        return params

    # Converts params to lowercase strings. Add auth params if specified.
    def process_params(self, params, auth=False):
        for i in params:
            params[i] = str(params[i]).lower()
        if auth: 
            params = self.add_auth(params)
        return params

    # Allow user to call custom methods in case of changes to the LAPI
    def call_method(self, method, auth=True, **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params)

    # Login.validate
    def validate(self):
        params = {'APIKey': apiKey, 'Token': authToken}
        return api.call('Validate', params)

    # Module.modules
    def modules(self, auth=True, duration=0, includeAllInfo=True):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
        params = self.process_params(params, auth)
        return api.call('Modules', params)

