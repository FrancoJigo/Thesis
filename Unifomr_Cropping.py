import Image

def crop_image(file_name,new_height,new_width):

    im = Image.open(file_name+".jpg")
    width, height = im.size   

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    crop_im = im.crop((left, top, right, bottom)) #Cropping Image 

    crop_im.save(file_name+"_new.jpg")  #Saving Images 

new_width = 256     #Enter the crop image width
new_height = 256    #Enter the crop image height
file_name = ["2.0"] #Enter File Names

for i in file_name:
    crop_image(i,new_height,new_width)


# crop_image('images/Species2/30pics/2.0.jpg',)