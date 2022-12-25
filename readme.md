# Wordpress Rest Api


```python
username = 'admin'   
password = '123 456 789 0123'   
website = 'https://www.mywpsite.com'
api = WordPressAPI(website, username, password)
```

## How to get different endpoints

```python
posts_url = api.endpoints['posts']  # '/wp-json/wp/v2/posts'
```

