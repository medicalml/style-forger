import requests
from StringIO import StringIO
from PIL import Image
import config

page_id = '1880783985473739'

def request_token(page_id):
    user_token = open('facebook_upload/user_token.txt', 'r').read()
    token_request = requests.get('https://graph.facebook.com/v2.8/{0}?fields=access_token&access_token={1}'.format(page_id, user_token))
    return token_request.json()['access_token']

def upload_file(imageRaw):
    image = Image.fromarray(imageRaw)
    imageStringIO = StringIO()
    image.save(imageStringIO, "JPEG")
    imageStringIO.seek(0)

    page_token = request_token(page_id)

    files = {'image': imageStringIO}
    url = 'https://graph.facebook.com/v2.8/{0}/photos?access_token={1}'.format(page_id, page_token)
    upload_request = requests.post(url, files=files)

    response = upload_request.json()

    if 'error' in response:
        # log error
        log_message = "{0}: {1}".format(response['error']['type'], response['error']['message'])

        return False
    else:
        if 'id' in response:
            # successful POST
            log_message = "Success: photo id:{0}".format(response['id'])

            return True
        else:
            return False
