from twython import Twython # Import Twitter's API module

# Import keys from auth.py
from auth import (twitter)

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
		twitter.update_status(status=msg)