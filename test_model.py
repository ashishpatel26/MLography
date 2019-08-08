from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import cv2


def load_image(img_path, show=True):

    img = image.load_img(img_path, target_size=(100, 100))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor

model = load_model('./model.h5')

anomaly_imp = "./ae_data/test_with_2_classes/anomaly/0.603991446964322scan3tag-16_impurity_1028.png"
normal_imp = "./ae_data/test_with_2_classes/normal/scan1tag-1_impurity_1936.png"

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# load a single image
new_image = load_image(anomaly_imp)

# check prediction
pred = model.predict(new_image)

# print prediction
print(pred)