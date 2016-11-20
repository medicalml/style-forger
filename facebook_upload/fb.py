import requests
from StringIO import StringIO
from PIL import Image

page_id = '1893358304217403'

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

    print upload_request.text