import urllib2
import urllib
import json
import re
from cookielib import CookieJar

def call(method, params):
    baseUrl = 'https://ivle.nus.edu.sg/api/Lapi.svc/'
    url = '%s?%s' % (baseUrl + method, urllib.urlencode(params))
    return url

def get_auth_token(apiKey, userid, password):
    loginUrl = 'https://ivle.nus.edu.sg/api/login/?apikey=%s' % apiKey
    data = urllib2.urlopen(loginUrl).read()

    if len(data) == 0:
        print 'HEY!'
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

    return userToken

