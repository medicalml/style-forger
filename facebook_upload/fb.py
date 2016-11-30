import requests
from StringIO import StringIO
from PIL import Image
# import config
import logging

page_id = '1880783985473739'
logging.basicConfig(filename="fb.log",
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

def request_token(page_id):

    try:
        user_token = open('facebook_upload/user_token.txt', 'r').read()
    except Exception as e:
        logging.error("Failed to open user token file with exception:")
        logging.error(e)
        return False

    try:
        token_request = requests.get('https://graph.facebook.com/v2.8/{0}?fields=access_token&access_token={1}'.format(page_id, user_token))
    except requests.exceptions.RequestException as e:
        logging.error("Failed to acquire page token with exception:")
        logging.error(e)
        return False

    return token_request.json()['access_token']

def upload_file(imageRaw, mock=False):
    if not mock:
        image = Image.fromarray(imageRaw)
        imageStringIO = StringIO()
        image.save(imageStringIO, "JPEG")
        imageStringIO.seek(0)
    else:
        imageStringIO = b'0';

    page_token = request_token(page_id)

    if (page_token is False):
        return False

    files = {'image': imageStringIO}
    url = 'https://graph.facebook.com/v2.8/{0}/photos?access_token={1}'.format(page_id, page_token)
    try:
        upload_request = requests.post(url, files=files)
    except requests.exceptions.RequestException as e:
        logging.error("Failed to upload a photo with exception:")
        logging.error(e)
        return False

    response = upload_request.json()

    if 'error' in response:
        # log error
        log_message = "{0}: {1}".format(response['error']['type'], response['error']['message'])
        logging.error(log_message)
        return False
    else:
        if 'id' in response:
            # successful POST
            log_message = "Success: photo id:{0}".format(response['id'])
            logging.info(log_message)
            return True
        else:
            log_message = "Failed to upload a photo (no further information)"
            logging.error(log_message)
            return False
