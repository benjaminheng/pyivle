import urllib2
import urllib
import json
import re
from cookielib import CookieJar
from collections import namedtuple

apiKey = None
authToken = None

class InvalidAPIKeyException(Exception): pass
class InvalidLoginException(Exception): pass
class UnauthenticatedException(Exception): pass

# call the method specified. don't add auth params by default
def call(method, params, auth=False):
    params = process_params(params, auth=auth)
    baseUrl = 'https://ivle.nus.edu.sg/api/Lapi.svc/'
    url = '%s?%s' % (baseUrl + method, urllib.urlencode(params))
    jsonString = urllib2.urlopen(url).read()
    # DEBUG TODO: remove
    with open('jsondump.txt', 'w') as f:
        f.write(jsonString)
    # Magic (http://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object)
    result = json.loads(jsonString, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    return result

def get_auth_token(apiKey, userid, password):
    loginUrl = 'https://ivle.nus.edu.sg/api/login/?apikey=%s' % apiKey
    data = urllib2.urlopen(loginUrl).read()

    if len(data) == 0:
        raise InvalidAPIKeyException('API key is not valid.')

    viewstate = re.search('__VIEWSTATE.+?value="(.+?)"', data)
    if not viewstate:
        print '[Error] Unable to get user token.'
        # TODO: try a hardcoded VIEWSTATE value. if fail again, raise exception

    viewstate = viewstate.group(1)
    params = urllib.urlencode({'__VIEWSTATE': viewstate, 'userid': userid, 'password': password})

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    userToken = opener.open(loginUrl, params).read()

    if len(userToken) != 416:
        raise InvalidLoginException('Login credentials are not valid.')

    return userToken

# Adds authentication parameters to parameter list
# TODO: raise exception if authtoken not set
def add_auth(params):
    if not authToken:
        raise UnauthenticatedException('Not authenticated. Login or specify auth=False (if available) if you are sure you wish to call this function without authentication.')
    params['APIKey'] = apiKey
    params['AuthToken'] = authToken
    return params

# Converts params to strings. Add auth params if specified.
def process_params(params, auth=False):
    for i in params:
        params[i] = str(params[i])
    if auth: 
        params = add_auth(params)
    return params
