<<<<<<< HEAD
from twython import Twython # Import Twitter's API module

# Import keys from conf.py
from conf import (twitter)

# Start Twitter API
twitter = Twython(
	twitter['consumer_key'],
	twitter['consumer_secret'],
	twitter['access_token'],
	twitter['access_token_secret']
)

# Basic tweet function
def tweet(msg, img):
	if img:
		photo = open(img, 'rb') # Turn img dir to img variable
		response = twitter.upload_media(media=photo) # Load responses
		twitter.update_status(status=msg, media_ids=[response['media_id']]) # Update status with response
	else:
=======
from twython import Twython # Import Twitter's API module

# Import keys from conf.py
from conf import (twitter)

# Start Twitter API
twitter = Twython(
	twitter['consumer_key'],
	twitter['consumer_secret'],
	twitter['access_token'],
	twitter['access_token_secret']
)

# Basic tweet function
def tweet(msg, img):
	if img:
		photo = open(img, 'rb') # Turn img dir to img variable
		response = twitter.upload_media(media=photo) # Load responses
		twitter.update_status(status=msg, media_ids=[response['media_id']]) # Update status with response
	else:
>>>>>>> e50165ac40ebc3d885aa3c27cdf9e22c3b99ba62
		twitter.update_status(status=msg)