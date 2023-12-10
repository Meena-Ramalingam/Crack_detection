from flask import Flask, render_template
from script.test import crack_detection
import cv2
import os

app = Flask(__name__)

@app.route('/')
def index():
    model_path = 'CNN/models/imageclassifier.h5'
    image_path = 'enhancement/output/images'

    # Call crack_detection function to get images with cracks
    crack_detected_image_paths = crack_detection(model_path, image_path)

    # Convert image paths into actual images
    crack_detected_images = []
    for image_path in crack_detected_image_paths:
        img = cv2.imread(image_path)
        # Convert BGR to RGB if needed
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        crack_detected_images.append(img)

    # Render HTML template and pass the detected images to the frontend
    return render_template('index.html', images=crack_detected_images)

if __name__ == '__main__':
    app.run(debug=True)

