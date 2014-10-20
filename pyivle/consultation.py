import api

# Consultation.Consultation_ModuleFacilitatorsWithSlots
def consultation_modulefacilitatorswithslots(courseId, includeSlots, slotType, auth=True):
    params = {'CourseID': courseId, 'IncludeSlots': includeSlots, 'SlotType': slotType}
    return api.call('Consultation_ModuleFacilitatorsWithSlots', params, auth=auth)

# Consultation.ConsultationSlots
def consultationslots(lecId, slotType, auth=True):
    params = {'LecID': lecId, 'SlotType': slotType}
    return api.call('ConsultationSlots', params, auth=auth)

# Consultation.Consultation_SignedUpSlots
def consultation_signedupslots(id, courseId, courseCode, courseName, lecturer, consultationStartDate, consultationEndDate, duration, contactMethod, venue, signUpDate, auth=True):
    params = {'ID': id, 'CourseID': courseId, 'CourseCode': courseCode, 'CourseName': courseName, 'Lecturer': lecturer, 'ConsultationStartDate': consultationStartDate, 'ConsultationEndDate': consultationEndDate, 'Duration': duration, 'ContactMethod': contactMethod, 'Venue': venue, 'SignUpDate': signUpDate}
    return api.call('Consultation_SignedUpSLots', params, auth=auth)
