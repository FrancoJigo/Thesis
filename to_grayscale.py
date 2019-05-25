import cv2
import glob, os, errno

# Replace mydir with the directory you want
mydir = r'C:/Users/63917/Documents/Jigo/Thesis/'


for fil in glob.glob("*.jpg"):
    image = cv2.imread(fil,0) 
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
    # print(image.shape)
    cv2.imwrite(os.path.join(mydir,fil),image)