import api

# Login.Validate
def validate():
    params = {'APIKey': api.apiKey, 'Token': api.authToken}
    return api.call('Validate', params)

# Login.UserName_Get
def username_get():
    params = {'APIKey': api.apiKey, 'Token': api.authToken}
    return api.call('UserName_Get', params)

# Login.UserID_Get
def userid_get():
    params = {'APIKey': api.apiKey, 'Token': api.authToken}
    return api.call('UserID_Get', params)

# Login.UserEmail_Get
def useremail_get():
    params = {'APIKey': api.apiKey, 'Token': api.authToken}
    return api.call('UserEmail_Get', params)
