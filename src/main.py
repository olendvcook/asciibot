from PIL import Image	
from PIL import ImageOps	
	
im = Image.open('../resources/picture.png')

print im.size

im = ImageOps.grayscale(im)

im = im.resize((100,100), Image.ANTIALIAS)

#im.show()

fh = open('asciidata', 'w')



for y in range (0, im.size[1]):
	for x in range (0, im.size[0]):
		lum =  im.getpixel((x,y))
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
	fh.write('\n')
		
		

fh.close()