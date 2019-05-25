from PIL import Image

def crop_image(file_name,new_height,new_width):

    im = Image.open(file_name+".jpg")
    width, height = im.size   

    left = (width - new_width - 500)/2
    top = (height - new_height -500)/2
    right = (width + new_width -800)/2
    bottom = (height + new_height+200)/2

    crop_im = im.crop((left, top, right, bottom)) #Cropping Image 

    crop_im.save(file_name+"_new.jpg")  #Saving Images 

new_width = 1000     #Enter the crop image width
new_height = 1000    #Enter the crop image height
i="species5"
file_name = ['species5']
# file_name = [i+".0",i+".01",i+".02",i+".03",i+".04",i+".05",i+".06",i+".07",i+".08",i+".09",i+".10",i+".11",i+".12",i+".13",i+".14",i+".15",i+".16",i+".17",i+".18",i+".19"] #Enter File Names
#,i+".20",i+".21",i+".22",i+".23",i+".24",i+".25",i+".26",i+".27",i+".28",i+".29"

for i in file_name:
    crop_image(i,new_height,new_width)


# crop_image('images/Species2/30pics/2.0.jpg',)