import praw
import requests
from collections import deque

from convertascii import create_ascii

# Required for reddit, description of who this is
user_agent = ("ASCII Art converter 1.0 by /u/olendvcook, /u/fofofosho "
	      "github.com/olendvcook/asciibot")

reddit = praw.Reddit(user_agent=user_agent)
reddit.login()

cache = deque(maxlen=69)

def downloadImage(imageUrl, localFileName):
	directory = '../resources/'
	print imageUrl
	response = requests.get(imageUrl)
	
	if response.status_code == 200:
		print 'Downloading %s...' % localFileName
		localFileName = directory + localFileName
		with open(localFileName, 'wb') as fh:
			for chunk in response.iter_content(4096):
				fh.write(chunk)
		print 'Download complete!'
	else:
		print 'Problem downloading - status code %s' % response.status_code
	return localFileName

# TODO: change after dev
# How many things we will receive
#thing_limit = 2

# Main loop
#while True:
subreddit = reddit.get_subreddit('botascii')
for submission in subreddit.get_new(limit=1):
	if 'http://imgur.com/a/' in submission.url:
		# html = requests.get(submission.url).text
		# print html		
		continue
	elif 'http://i.imgur.com/' in submission.url:
		imagePath = downloadImage(submission.url, submission.url.split('/')[-1].split('#')[0].split('?')[0])

		create_ascii(imagePath)



