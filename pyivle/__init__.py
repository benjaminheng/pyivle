import api
from login import Login
from module import Module
from consultation import Consultation
from announcement import Announcement
from webcast_lectures import WebcastLectures
from rosters_and_groups import RostersAndGroups
from timetable import Timetable

class Pyivle(Login, Module, Consultation, RostersAndGroups, Announcement, WebcastLectures, Timetable):
    def __init__(self, apiKey, authToken=None, **kwargs):
        api.apiKey = apiKey
        if authToken: api.authToken = authToken
        #self.authToken = self._login(userid, password)

    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call(self, method, auth=True, verb='get', **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params, auth, verb)
