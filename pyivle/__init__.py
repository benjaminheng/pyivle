import api
from login import Login
from module import Module
from consultation import Consultation
from announcement import Announcement
from webcast_lectures import WebcastLectures
from rosters_and_groups import RostersAndGroups
from timetable import Timetable
from forum import Forum
from poll import Poll
from workbin import Workbin
from gradebook import Gradebook
from library_ereserves import LibraryEReserves 
from my_organizer import MyOrganizer
from community import Community
from open_webcast_lectures import OpenWebcastLectures 
from student_events import StudentEvents
from ivle_news import IVLENews 
from delta_datasets import DeltaDatasets
from profile import Profile

class Pyivle(Login, Module, Consultation, RostersAndGroups, Announcement, Forum, WebcastLectures, Poll, Gradebook, LibraryEReserves, MyOrganizer, Community, OpenWebcastLectures, StudentEvents, IVLENews, DeltaDatasets, Profile, Timetable):
    def __init__(self, apiKey, authToken=None, **kwargs):
        api.apiKey = apiKey
        if authToken: 
            api.authToken = authToken

    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call(self, method, auth=True, verb='get', **kwargs):
        return api.call(method, kwargs, auth, verb)

    # Custom API call for downloading files. Downloads from workbin
    # by default.
    def download_file(fileid, target='workbin', auth=True):
        return api.download_file(id, target, auth)
