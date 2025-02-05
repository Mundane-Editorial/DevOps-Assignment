from flask import Flask, jsonify, request
from keras.models import model_from_json
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image

# Load the model
json_file = open("facialemotionmodel.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("facialemotionmodel.h5")

# Labels for prediction (emotion classes)
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# Initialize Flask app
app = Flask(__name__)

# Function to process image and extract features for prediction
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# Route for prediction (accepts image as input)
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    img_file = request.files['image']
    
    # Convert the image file to a format that can be processed by the model
    img = image.load_img(img_file, target_size=(48, 48), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize image

    # Make prediction
    prediction = model.predict(img_array)
    emotion = np.argmax(prediction, axis=1)  # Get the emotion index (e.g., happy, sad, etc.)
    prediction_label = labels[emotion[0]]  # Get the corresponding emotion label

    return jsonify({'emotion': prediction_label})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
