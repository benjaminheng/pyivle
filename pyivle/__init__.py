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
        self.module_readingformatted = module.module_readingformatted
        self.module_readingunformatted = module.module_readingunformatted
        self.module_readingsformatted_coop = module.module_readingsformatted_coop
        self.module_reading = module.module_reading
        self.modules_taken = module.modules_taken

        # Consultation
        self.consultation_modulefacilitatorswithslots = consultation.consultation_modulefacilitatorswithslots
        self.consultationslots = consultation.consultationslots
        self.consultation_signedupslots = consultation.consultation_signedupslots

    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call_method(self, method, auth=True, **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params, auth=auth)
