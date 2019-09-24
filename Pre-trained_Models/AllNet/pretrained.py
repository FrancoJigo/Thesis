import os
import glob

import tqdm
import numpy as np
import scipy.ndimage
import scipy.misc


IMG_SIZE = (256, 256)

for image_path in tqdm.tqdm(list(glob.glob('simpsons_dataset/**/*.jpg'))):
    image_pixels = scipy.ndimage.imread(image_path)
    resized_image_pixels = scipy.misc.imresize(image_pixels, IMG_SIZE)
    image_basepath, _ = os.path.splitext(image_path)
    np.savez(image_basepath+'.npz', pixels=resized_image_pixels)
