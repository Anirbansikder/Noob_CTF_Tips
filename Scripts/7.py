from PIL import Image
new_image = Image.new('RGB',(600, 500), (250,250,250))
for i in range(1,3001):
	image1 = Image.open('60x50/' + str(i) + '.jpg')
	# image1 = image1.resize((100,100))
	new_image.paste(image1,(((i-1)//50)*10,((i-1)%50)*10))
new_image.show()