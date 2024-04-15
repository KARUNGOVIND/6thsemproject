import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved model
model = tf.keras.models.load_model(r'G:\6sem project\py\fabric_classifier_model.h5')


def predict_image_class(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Predict the class probabilities
    prediction = model.predict(img_array)

    return prediction


# Example usage
image_path = r'G:\6sem project\sample\cotsam.jpg'
prediction = predict_image_class(image_path)

# Assuming it's a binary classification problem
if prediction[0][0] >= 0.5:
    print("Predicted class: Cotton")
else:
    print("Predicted class: Silk")
