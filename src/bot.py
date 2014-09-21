import praw
import requests
from bs4 import BeautifulSoup

from convertascii import create_ascii

# Required for reddit, description of who this is
user_agent = ("ASCII Art converter 1.0 by /u/olendvcook, /u/fofofosho "
	      "github.com/olendvcook/asciibot")

reddit = praw.Reddit(user_agent=user_agent)
reddit.login()

cache = deque(maxlen=69)

# TODO: change after dev
# How many things we will receive
#thing_limit = 2

# Main loop
#while True:
subreddit = reddit.get_subreddit('botascii')
for submission in subreddit.get_new(limit=1):
	if 'http://imgur.com/a/' in submission.url:
		continue
	elif 'http://i.imgur.com/' in submission.url:
		html = requests.get(submission.url).text
		print html
		

def downloadImage(imageUrl, localFileName):
	response = requests.get(imageUrl)
	
	if response.status_code == 200:
		print 'Downloading %s...' % localFileName
		with open(localFileName, 'wb') as fh:
			for chunk in response.iter_content(4096):
				fh.write(chunk)
	else:
		print 'Problem downloading - status code %s' 
		       % response.status_code


