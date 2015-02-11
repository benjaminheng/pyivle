import api

class Workbin():
    # Workbin.Workbins
    def workbins(courseId, duration=0, workbinId=None, titleOnly=False, auth=True):
        params = {'CourseID': courseId, 'Duration': duration, 'WorkbinID': workbinId, 'TitleOnly': titleOnly}
        return api.call('Workbins', params, auth)

    # Non-standard API method, replacement for Workbin.DownloadFile
    def workbin_download_file(id, auth=True):
        return api.download_file(id, 'workbin', auth)
