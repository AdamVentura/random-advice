import praw
from keys import keys

def authenticate():
	# Create instance of reddit to authenticate
	reddit = praw.Reddit(
		client_id = keys['CLIENT_ID'],
		client_secret = keys['CLIENT_SECRET'],
		user_agent = keys['USER_AGENT'],
		)
	# Return instance
	return reddit