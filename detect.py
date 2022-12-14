import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model


def detector(imagePath):
    model = load_model('model_.h5')
    my_image = plt.imread(imagePath)
    my_image_resized = resize(my_image, (32, 32, 3))
    probabilities = model.predict(np.array([my_image_resized, ]))
    number_to_class = ['airplane', 'automobile', 'bird',
                       'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    index = np.argsort(probabilities[0, :])
    # create dictionary to store the results for all 10 classes
    results = {}
    for i in range(10):
        results[number_to_class[index[9 - i]]
                ] = str(probabilities[0, index[9 - i]])
    print(results)
    return results
