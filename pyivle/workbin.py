import api

class Workbin():
    # Workbin.Workbins
    def Workbins(courseId, duration=0, workbinId=None, titleOnly=False, auth=True):
        params = {'CourseID': courseId, 'Duration': duration, 'WorkbinID': workbinId, 'TitleOnly': titleOnly}
        return api.call('Workbins', params, auth)

    #TODO: Implement DownloadFile
