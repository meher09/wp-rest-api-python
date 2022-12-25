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

        if not parsed_url.scheme in ['http', 'https']:
            raise ValueError('base_url must start with http:// or https://')

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
            'posts': '{}/wp-json/wp/v2/posts'.format(self.base_url),
            'users': '{}/wp-json/wp/v2/users'.format(self.base_url),
            'comments': '{}/wp-json/wp/v2/comments'.format(self.base_url),
            'media': '{}/wp-json/wp/v2/media'.format(self.base_url),
        }

    def create_post(self, title, content, status='publish'):
        """Create a new post in the WordPress site.

        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            status (str, optional): The status of the post. Defaults to 'publish'.

        Returns:
            dict: A dictionary containing the data of the created post.
        """
        post_data = {
            'title': title,
            'content': content,
            'status': status,
        }
        response = requests.post(
            '{}{}'.format(self.base_url, self.endpoints['posts']),
            json=post_data,
            headers=self.headers
        )
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Failed to create post')
