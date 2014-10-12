import json
import api

class Pyivle(object):
    def __init__(self, apiKey, authToken=None, **kwargs):
        self.apiKey = apiKey
        self.authToken = authToken
        #self.authToken = self._login(userid, password)

    # TODO: authenticate and get authtoken
    def login(self, userid, password):
        self.authToken = api.get_auth_token(self.apiKey, userid, password)
    
    # Adds authentication parameters to parameter list
    # TODO: raise exception if authtoken not set
    def add_auth(self, params):
        params['APIKey'] = self.apiKey
        params['AuthToken'] = self.authToken
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

    #############################################
    # BEGIN API                                 #
    #############################################

    # Login.Validate
    def validate(self):
        params = {'APIKey': self.apiKey, 'Token': self.authToken}
        return api.call('Validate', params)

    # Login.UserName_Get
    def username_get(self):
        params = {'APIKey': self.apiKey, 'Token': self.authToken}
        return api.call('UserName_Get', params)

    # Login.UserID_Get
    def userid_get(self):
        params = {'APIKey': self.apiKey, 'Token': self.authToken}
        return api.call('UserID_Get', params)

    # Login.UserEmail_Get
    def useremail_get(self):
        params = {'APIKey': self.apiKey, 'Token': self.authToken}
        return api.call('UserEmail_Get', params)

    # Module.Modules
    def modules(self, auth=True, duration=0, includeAllInfo=True):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
        params = self.process_params(params, auth)
        return api.call('Modules', params)

    # Module.Modules_Staff
    def modules_staff(self, auth=True, duration=0, includeallinfo=True):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
        params = self.process_params(params, auth)
        return api.call('Modules_Staff', params)

    # Module.Modules_Student
    def modules_student(self, auth=True, duration=0, includeallinfo=True):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
        params = self.process_params(params, auth)
        return api.call('Modules_Student', params)

    # Module.module
    def module(self, courseId, auth=True, duration=0, includeAllInfo=True, titleOnly=False):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo, 'CourseID': courseId, 'TitleOnly': titleOnly}
        params = self.process_params(params, auth)
        return api.call('Module', params)

    # Module.Modules_Search
    def modules_search(self, auth=True, duration=0, includeallinfo=True):
        params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
        params = self.process_params(params, auth)
        return api.call('Modules_Search', params)

    # Module.Modules_Lecturers
    def module_lecturers(self, courseId, auth=True, duration=0):
        params = {'Duration': duration, 'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_Lecturers', params)

    # Module.Module_Information
    def module_information(self, courseId, auth=True, duration=0):
        params = {'Duration': duration, 'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_Information', params)

    # Module.Module_Weblinks
    def module_weblinks(self, courseId, auth=True):
        params = {'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_Weblinks', params)

    # Module.Module_ReadingFormatted
    def module_readingformatted(self, courseId, auth=True, duration=0):
        params = {'Duration': duration, 'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_ReadingFormatted', params)

    # Module.Module_ReadingUnformatted
    def module_readingunformatted(self, courseId, auth=True, duration=0):
        params = {'Duration': duration, 'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_ReadingUnformatted', params)

    # Module.Module_ReadingsFormatted_Coop
    def module_readingsformatted_coop(self, date, auth=True):
        params = {'date': date}
        params = self.process_params(params, auth)
        return api.call('Module_ReadingsFormatted_Coop', params)

    # Module.Module_Reading
    def module_reading(self, courseId, auth=True, duration=0):
        params = {'Duration': duration, 'CourseID': courseId}
        params = self.process_params(params, auth)
        return api.call('Module_Reading', params)

    # Module.Modules_Taken
    def modules_taken(self, studentId, auth=True):
        params = {'StudentID': studentId}
        params = self.process_params(params, auth)
        return api.call('Modules_Taken', params)
