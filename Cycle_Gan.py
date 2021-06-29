import tensorflow as tf
from PIL import Image
import numpy as np
import tensorflow_addons as tfa
monet_generator = tf.keras.models.load_model('resources/monet_generator.h5',
    custom_objects={'InstanceNormalization':tfa.layers.InstanceNormalization})

img_path='resources/00068bc07f.jpg'

img_array = np.array(Image.open(img_path))
# plt.imshow(img_array)
# img_array = np.expand_dims(img_array, axis=0)
print(img_array.shape)
# monet_generator.save('monet_generator.h5')
# plt.imshow(img_array)
generated_sample = monet_generator.predict(img_array)

print(generated_sample)
# plt.imshow(generated_sample)
print(new_model.predict(test_images).shape)
