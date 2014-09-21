from PIL import Image	
from PIL import ImageOps	
	
im = Image.open('../resources/picture.png')

print im.size

im = ImageOps.grayscale(im)

#this size puts us at 8125 characters and a good size for reddit comments
im = im.resize((120,55), Image.ANTIALIAS)

#so the ascii looked really good when zoomed out so i wanted to keep it as an option
#but it does look better with less characters when not zoomed in
extraascii = False

#im.show()

fh = open('asciidata', 'w')



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
		
		

fh.close()