import numpy as np
from keras.preprocessing import image
import tensorflow as tf

test_image = image.load_img('species5.jpg', target_size = (64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

model = tf.keras.models.load_model("CNN.model")
result = model.predict(test_image)
print(result)
