import api

# Consultation.Consultation_ModuleFacilitatorsWithSlots
def consultation_module_facilitators_with_slots(courseId, includeSlots, slotType, auth=True):
    params = {'CourseID': courseId, 'IncludeSlots': includeSlots, 'SlotType': slotType}
    return api.call('Consultation_ModuleFacilitatorsWithSlots', params, auth=auth)

# Consultation.ConsultationSlots
def consultation_slots(lecId, slotType, auth=True):
    params = {'LecID': lecId, 'SlotType': slotType}
    return api.call('ConsultationSlots', params, auth)

# Consultation.Consultation_SignedUpSlots
def consultation_signed_up_slots(id, courseId, courseCode, courseName, lecturer, consultationStartDate, consultationEndDate, duration, contactMethod, venue, signUpDate, auth=True):
    params = {'ID': id, 'CourseID': courseId, 'CourseCode': courseCode, 'CourseName': courseName, 'Lecturer': lecturer, 'ConsultationStartDate': consultationStartDate, 'ConsultationEndDate': consultationEndDate, 'Duration': duration, 'ContactMethod': contactMethod, 'Venue': venue, 'SignUpDate': signUpDate}
    return api.call('Consultation_SignedUpSLots', params, auth)

# Consultation.Consultation_SignUp_JSON
def consultation_sign_up(consultationId, auth=True):
    params = {'ConsultationID': consultationId}
    return api.call('Consultation_SignUp_JSON', params, auth, 'post')

# Consultation.Consultation_CancelSlot_JSON
def consultation_cancel_slot(consultationId, auth=True):
    params = {'ConsultationID': consultationId}
    return api.call('Consultation_CancelSlot_JSON', params, auth, 'post')
