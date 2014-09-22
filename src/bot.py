import praw
import requests
from collections import deque
from time import sleep

from convertascii import create_ascii

# TODO: Multi-threaded to check if previous ascii posts have been downvoted, if so delete them

# TODO: Make the console prints cleaner, more description

# Required for reddit, description of who this is
user_agent = ("ASCII Art converter 1.0 by /u/olendvcook, /u/fofofosho "
	      "github.com/olendvcook/asciibot")

reddit = praw.Reddit(user_agent=user_agent)
reddit.login()

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
	
def postAscii(submission):
	postCache = open('postCache.txt','a+')
	commentFlag = False
	
	postCache.seek(0)
	
	if submission.id in postCache.read():
		postCache.close()
		return False

	if 'imgur.com/a/' in submission.url:
		# Ignore galleries
		postCache.close()
		return False
	elif 'i.imgur.com/' in submission.url:
		postCache.seek(0,2)
		postCache.write(submission.id + '\n')
		imagePath = downloadImage(submission.url, submission.url.split('/')[-1].split('?')[0])
		create_ascii(imagePath)
		commentFlag = True
	elif 'imgur.com/' in submission.url:
		postCache.seek(0,2)
		postCache.write(submission.id + '\n')
		imageHash = submission.url.split('/')[-1].split('?')[0] + '.jpg'
		imagePath = downloadImage('i.imgur.com/' + imageHash, imageHash)
		create_ascii(imagePath)
		commentFlag = True

	if commentFlag:
		# Write out ASCII to post as code
		with open('asciidata', 'r') as fh:
			text = fh.read()
		comment.reply(text)
		print 'Posted ASCII!!!'
		postCache.close()
		return True
		
	postCache.close()
	return False

# Main loop
while True:
	subreddit = reddit.get_subreddit('botascii')
	commentCache = open('commentCache.txt', 'a+')

	# TODO: add functionality to listen for ascii bot's name in comments
	for submission in subreddit.get_hot():
		
		requested = False
		commentCache.seek(0)

		# Parse comments and look for bot getting called
		comments = praw.helpers.flatten_tree(submission.comments)
		for comment in comments:
			if 'bot_ascii, where art thou?' in comment.body.lower() and comment.id not in commentCache.read():
				requested = True
				commentCache.write(comment.id + '\n')
		if requested:
			postAscii(submission)
			

	commentCache.close()
	
	print 'Sleep for a minute..'
	sleep(60)

