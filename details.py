APP_ACCESS_TOKEN =  '1705754005.29541b0.156ba485dedb482cbc95c8e430efa9ec'
BASE_URL = 'https://api.instagram.com/v1/'
import requests
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
    exit()

