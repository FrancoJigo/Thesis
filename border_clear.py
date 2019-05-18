from PIL import Image, ImageChops


def image_clearborder(im3):
	im = Image.open(im3)
	def trim(im):
		bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
		diff = ImageChops.difference(im, bg)
		diff = ImageChops.add(diff, diff, 2.0, -100)
		bbox = diff.getbbox()
		if bbox:
			return im.crop(bbox)
	trim(im).show()
	trim(im).save('cleared_border.jpg')