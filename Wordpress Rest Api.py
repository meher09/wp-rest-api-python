import requests
import base64
import urllib.parse


class WordPressAPI:

    def __init__(self, base_url, username, password):
        """Initialize a WordPressAPI object.

        Args:
            base_url (str): The base URL of the WordPress site.
            username (str): The username for authenticating with the WordPress REST API.
            password (str): The password for authenticating with the WordPress REST API.
        """

        # Check if base_url is a valid URL
        try:
            parsed_url = urllib.parse.urlparse(base_url)
        except ValueError:
            raise ValueError('Your Website url is not a valid URL')

        # Check if base_url starts with https://
        if not parsed_url.scheme == 'https':
            raise ValueError('Website url must start with http://')

        # Check if base_url is reachable
        response = requests.get(base_url)
        if response.status_code != 200:
            raise ValueError('Website url is not reachable')

        # Remove trailing slash from base_url if it exists
        if base_url[-1] == '/':
            base_url = base_url[:-1]
        self.base_url = base_url
        token = base64.b64encode(f'{username}:{password}'.encode())
        self.headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

        self.endpoints = {
            'posts': '/wp-json/wp/v2/posts',
            'users': '/wp-json/wp/v2/users',
            'comments': '/wp-json/wp/v2/comments',
            'media': '/wp-json/wp/v2/media',
        }
