import requests
import os.path

page_token = None

#debug
page_id = '1893358304217403'
page_token = 'EAACEdEose0cBADBwfEXZBtkb2upWflGLjW2gzVs4XAZBzhAD3x6vGVDs29oUtD8w74lMN9wxOJUXOQ3NQ3zF5TxvyPi5jylaCRx6rdJYZAZArZA3ZAywjINe44VSibwMURsZA0ByQlI7LHfRc3kHEMcneGZBZA6euNeSd1EKjYimSRqZCZBZAIlZAbVGsaWka09SZBZBDcZD'
filename = 'img.jpg'

def request_token(page_id):
    user_token = open('token', 'r').read()

    token_request = requests.get('https://graph.facebook.com/v2.8/{0}?fields=access_token&access_token={1}'.format(page_id, user_token))

    page_token = token_request.json()['access_token']

def upload_file(page_id, filename):
    if not os.path.isfile(filename):
        return False

    # request_token(page_id) # TODO: should request only when neccessary

    upload_request = requests.post('https://graph.facebook.com/v2.8/{0}/photos?access_token={1}'.format(page_id, page_token), files={'image': open(filename, 'rb')})

    print(upload_request.text)


# usage:
# upload_file(page_id, filename)