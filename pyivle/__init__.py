import api
import login
import module
import consultation

class Pyivle(object):
    def __init__(self, apiKey, authToken=None, **kwargs):
        api.apiKey = apiKey
        if authToken: api.authToken = authToken
        #self.authToken = self._login(userid, password)

        # Login
        self.validate = login.validate
        self.username_get = login.username_get
        self.userid_get = login.userid_get
        self.useremail_get = login.useremail_get

        # Module
        self.modules = module.modules
        self.modules_staff = module.modules_staff
        self.modules_student= module.modules_student
        self.module = module.module
        self.modules_search = module.modules_search
        self.module_lecturer = module.module_lecturers
        self.module_information = module.module_information
        self.module_weblinks = module.module_weblinks
        self.module_reading_formatted = module.module_reading_formatted
        self.module_reading_unformatted = module.module_reading_unformatted
        self.module_readings_formatted_coop = module.module_readings_formatted_coop
        self.module_reading = module.module_reading
        self.modules_taken = module.modules_taken

        # Consultation
        self.consultation_module_facilitators_with_slots = consultation.consultation_module_facilitators_with_slots
        self.consultation_slots = consultation.consultation_slots
        self.consultation_signed_up_slots = consultation.consultation_signed_up_slots

    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call(self, method, auth=True, **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params, auth=auth)

    def call_post(self, method, auth=True, **kwargs):
        pass
