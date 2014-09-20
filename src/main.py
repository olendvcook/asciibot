from PIL import Image

class Ascii_File:
    def __init__(self, filename):
        print 'File name - ' + filename
		
        self.imageHandler = Image.open(filename)
		
		
	
x = Ascii_File('resources/picture.png')

print x.imageHandler.size

