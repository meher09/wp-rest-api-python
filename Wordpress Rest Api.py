import requests
import base64


class WordPressAPI:
    def __init__(self, base_url, user, password):
        self.base_url = base_url
        token = base64.b64encode(f'{user}:{password}'.encode())
        self.headers = {'Authorization': f'Basic {token.decode("utf-8")}'}


