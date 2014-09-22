import os

from PIL import Image
from PIL import ImageOps

def create_ascii(imagePath):
	# Open the image
	im = Image.open(imagePath)

	# Grey the image
	im = ImageOps.grayscale(im)

	# This size puts us at 8125 characters and a good size for
	# reddit comments
	if im.size[0] / im.size[1] < .56:
		im = im.resize((85,55), Image.ANTIALIAS)
	elif im.size[0] / im.size[1] < .60:
		im = im.resize((100,55), Image.ANTIALIAS)
	else:
		im = im.resize((120,55), Image.ANTIALIAS)
	
	# Use more characters?
	extraascii = False

	# Open ASCII file, fh is handler
	fh = open('asciidata', 'w')

	# Go through picture's pixels, check luminosity, and print
	# out a character
	for y in range (0, im.size[1]):
		fh.write('    ')
		for x in range (0, im.size[0]):
			lum =  im.getpixel((x,y))
			if extraascii :
				if lum <= 29:
					fh.write('@')
				elif lum <= 67:
					fh.write('#')
				elif lum <= 85:
					fh.write('8')
				elif lum <= 113:
					fh.write('&')
				elif lum <= 141:
					fh.write('o')
				elif lum <= 169:
					fh.write(':')
				elif lum <= 197:
					fh.write('*')
				elif lum <= 225:
					fh.write(',')
				elif lum <= 255:
					fh.write(' ')
			
			else:
				if lum <= 38:
					fh.write('@')
				elif lum <=75:
					fh.write('&')
				elif lum <= 98:
					fh.write('o')
				elif lum <= 157:
					fh.write("|")
				elif lum <= 210:
					fh.write(":")
				elif lum <= 224:
					fh.write(".")
				else:
					fh.write(' ')
		fh.write('\n')

	# Close the file handler
	fh.close()
	
	# Delete image
	print 'Deleting %s' % imagePath
	os.remove(imagePath)
