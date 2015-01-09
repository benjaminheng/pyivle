import api

# Announcement.Announcements
def announcements(courseId, duration=0, titleOnly=False, auth=True):
    params = {'CourseID': courseId, 'Duration': duration, 'TitleOnly': titleOnly}
    return api.call('Announcements', params, auth)

# Announcement.Announcements_Unread
def announcements_unread(titleOnly=False, auth=True):
    params = {'TitleOnly': titleOnly}
    return api.call('Announcements_Unread', params, auth)

# Announcement.Announcements_AddLog_JSON
def announcements_add_log(annEventId, auth=True):
    params = {'AnnEventID': annEventId}
    return api.call('Announcements_AddLog_JSON', params, auth, 'post')

# Announcement.Announcements_Add_JSON
def announcements_add(courseId, annTitle, annMessage, sendEmail, auth=True):
    params = {'CourseID': courseId, 'AddTitle': annTitle, 'AnnMessage': annMessage, 'SendEmail': sendEmail}
    return api.call('Announcements_Add_JSON', params, auth, 'post')
