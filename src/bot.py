import praw
import requests
from collections import deque
from time import sleep

from convertascii import create_ascii

# TODO: Multi-threaded to check if previous ascii posts have been downvoted, if so delete them

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

# Main loop
while True:
	subreddit = reddit.get_subreddit('botascii')

	# TODO: add functionality to listen for ascii bot's name in comments
	for submission in subreddit.get_new(limit=1):
		commentFlag = False

		if submission.id in cache:
			continue

		if 'imgur.com/a/' in submission.url:
			# Ignore galleries
			continue
		elif 'i.imgur.com/' in submission.url:
			cache.append(submission.id)
			imagePath = downloadImage(submission.url, submission.url.split('/')[-1].split('?')[0])
			create_ascii(imagePath)
			commentFlag = True
		elif 'imgur.com/' in submission.url:
			cache.append(submission.id)
			imageHash = submission.url.split('/')[-1].split('?')[0] + '.jpg'
			imagePath = downloadImage('i.imgur.com/' + imageHash, imageHash)
			create_ascii(imagePath)
			commentFlag = True

		if commentFlag:
			# Write out ASCII to post as code
			with open('asciidata', 'r') as fh:
				text = fh.read()
			submission.add_comment(text)
			print 'Posted ASCII!!!'

	print 'Sleep for a minute..'
	sleep(60)

