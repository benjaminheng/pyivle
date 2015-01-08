import api
import login
import module
import consultation
import rosters_and_groups as roster

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
        self.consultation_sign_up = consultation.consultation_sign_up
        self.consultation_cancel_slot = consultation.consultation_cancel_slot
        
        # Rosters & Groups
        self.class_roster = roster.class_roster
        self.guest_roster = roster.guest_roster
        self.groups_by_user_and_module = roster.groups_by_user_and_module
        self.groups_by_user = roster.groups_by_user
        self.module_class_groups = roster.module_class_groups
        self.module_class_group_users = roster.module_class_group_users
        self.module_official_group_users = roster.module_official_group_users
        self.class_group_sign_up = roster.class_group_sign_up
        self.class_group_sign_up_remove = roster.class_group_sign_up_remove
        self.group_projects_by_user = roster.group_projects_by_user
        self.project_self_enrol_groups = roster.project_self_enrol_groups
        self.project_group_users = roster.project_group_users
        self.project_enrolled_groups = roster.project_enrolled_groups
        self.project_group_sign_up = roster.project_group_sign_up
        self.project_group_remove_sign_up = roster.project_group_remove_sign_up
        
    def login(self, userid, password):
        api.authToken = api.get_auth_token(api.apiKey, userid, password)
    
    # Allow user to call custom methods in case of changes to the LAPI
    def call(self, method, auth=True, verb='get', **kwargs):
        params = self.process_params(kwargs, auth)
        return api.call(method, params, auth, verb)
