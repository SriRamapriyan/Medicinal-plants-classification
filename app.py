from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your pre-trained CNN model
model = tf.keras.models.load_model('plant_leaf_classifier.h5')


# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to model input size
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('upload'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('upload'))

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)

        # Process the image
        image = Image.open(file_path)
        processed_image = preprocess_image(image)

        # Predict using the model
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)[0]

        # You can add more logic here to map class indices to actual plant names
        plant_name = "Predicted Plant Name"

        return render_template('result.html', plant_name=plant_name)

    return redirect(url_for('upload'))


if __name__ == '__main__':
    app.run(debug=True)
