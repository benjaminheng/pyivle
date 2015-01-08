import api

# Module.Modules
def modules(auth=True, duration=0, includeAllInfo=True):
    params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
    return api.call('Modules', params, auth)

# Module.Modules_Staff
def modules_staff(auth=True, duration=0, includeAllInfo=True):
    params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
    return api.call('Modules_Staff', params, auth)

# Module.Modules_Student
def modules_student(auth=True, duration=0, includeAllInfo=True):
    params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
    return api.call('Modules_Student', params, auth)

# Module.module
def module(courseId, auth=True, duration=0, includeAllInfo=True, titleOnly=False):
    params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo, 'CourseID': courseId, 'TitleOnly': titleOnly}
    return api.call('Module', params, auth)

# Module.Modules_Search
def modules_search(auth=True, duration=0, includeAllInfo=True):
    params = {'Duration': duration, 'IncludeAllInfo': includeAllInfo}
    return api.call('Modules_Search', params, auth)

# Module.Modules_Lecturers
def module_lecturers(courseId, auth=True, duration=0):
    params = {'Duration': duration, 'CourseID': courseId}
    return api.call('Module_Lecturers', params, auth)

# Module.Module_Information
def module_information(courseId, auth=True, duration=0):
    params = {'Duration': duration, 'CourseID': courseId}
    return api.call('Module_Information', params, auth)

# Module.Module_Weblinks
def module_weblinks(courseId, auth=True):
    params = {'CourseID': courseId}
    return api.call('Module_Weblinks', params, auth)

# Module.Module_ReadingFormatted
def module_reading_formatted(courseId, auth=True, duration=0):
    params = {'Duration': duration, 'CourseID': courseId}
    return api.call('Module_ReadingFormatted', params, auth)

# Module.Module_ReadingUnformatted
def module_reading_unformatted(courseId, auth=True, duration=0):
    params = {'Duration': duration, 'CourseID': courseId}
    return api.call('Module_ReadingUnformatted', params, auth)

# Module.Module_ReadingsFormatted_Coop
def module_readings_formatted_coop(date, auth=True):
    params = {'date': date}
    return api.call('Module_ReadingsFormatted_Coop', params, auth)

# Module.Module_Reading
def module_reading(courseId, auth=True, duration=0):
    params = {'Duration': duration, 'CourseID': courseId}
    return api.call('Module_Reading', params, auth)

# Module.Modules_Taken
def modules_taken(studentId, auth=True):
    params = {'StudentID': studentId}
    return api.call('Modules_Taken', params, auth)
