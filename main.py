from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename

# Create Flask app
app = Flask(_name_)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Make sure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load your trained model
model = load_model('model.h5', compile=False)

# Define your classes (replace with your actual 4 classes)
classes = ['Pituitary','No Tumor','Meningioma','Glioma']

def predict_image(image_path):
    # Load image with target size same as your model
    img = load_img(image_path, target_size=(128, 128))  # adjust size to your model input
    img_array = img_to_array(img) / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)[0]
    return classes[class_idx]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    uploaded_image_path = None

    if request.method == 'POST':
        if 'mri_image' not in request.files:
            return "No file part in the request", 400

        file = request.files['mri_image']
        if file.filename == '':
            return "No selected file", 400

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            uploaded_image_path = url_for('static', filename=f'uploads/{filename}')
            prediction = predict_image(filepath)

    return render_template('index.html', prediction=prediction, uploaded_image_path=uploaded_image_path)

if _name_ == "_main_":
    app.run(debug=True)
