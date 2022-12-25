from setuptools import setup, find_packages

setup(
    name='Wordpress_Rest_Api',
    version='0.0.0.1',
    author='Meher Nigar',
    author_email='mehernigarcu@gmail.com',
    description='A package for interacting with the WordPress REST API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/meher09/wp-rest-api-python',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
