import urllib2
import urllib
import json
import re
from cookielib import CookieJar
from collections import namedtuple

def call(method, params):
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
        print 'API_KEY not valid!'
        # TODO: raise exception: apiKey not valid

    viewstate = re.search('__VIEWSTATE.+?value="(.+?)"', data);
    if not viewstate:
        print '[Error] Unable to get user token.'
        # TODO: Raise exception

    viewstate = viewstate.group(1)
    params = urllib.urlencode({'__VIEWSTATE': viewstate, 'userid': userid, 'password': password})

    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    userToken = opener.open(loginUrl, params).read()

    if len(userToken) != 416:
        # TODO: raise exception, invalid login parameters
        print 'login fail, unable to get usertoken'

    return userToken

