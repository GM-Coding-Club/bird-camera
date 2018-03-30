# bird-camera

# Example conf.py

```
is_pi = True # Ensure platform is a pi
tweeting = True # Enable/disable tweeting
location = "Home" # Set location of camera

# Twitter keys

# From https://apps.twitter.com/

twitter = {
    'consumer_key': '<~25 chars>',
    'consumer_secret': '<~50 chars>',
    'access_token': '<~18 numbers>-<~31 chars>',
    'access_token_secret': '<~45 chars>'
}

# Firebase conf

# From https://console.firebase.google.com

firebase = {
    'database_url': 'https://<firebase_project_ID>.firebaseio.com/',
    'storage_bucket': '<Bucket>.appspot.com'
}
```

# Things we just expect you to know

```
AttributeError: 'module' object has no attribute 'python_2_unicode_compatible'
sudo pip install -U six
```