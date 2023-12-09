from flask import Flask, render_template
from CNN.video import extract_frames
from CNN.test import crack_detection
import subprocess
import os

app = Flask(__name__)

# Video frame extraction route
@app.route('/extract_frames')
def extract_video_frames():
    video_parent_dir = 'video/'
    output_frames_folder = 'frames'
    optional_frame_interval = 60

    # Perform frame extraction
    # Extract frames from the video and save them in the output folder
    # Call the function for frame extraction
    # Add appropriate error handling
    try:
        x = os.listdir(video_parent_dir)
        video_file_path = os.path.join(video_parent_dir, x[0])
        extract_frames(video_file_path, output_frames_folder, optional_frame_interval)
        message = "Frames extraction completed successfully."
    except Exception as e:
        message = f"An error occurred during frame extraction: {str(e)}"

    return render_template('index.html', message=message)

# Enhancement route
@app.route('/enhance')
def enhance_images():
    # Define enhancement parameters
    script_path = 'enhancement/finalEnhancer.py'
    input_file_path = 'frames'
    output_file_path = 'images'
    weights = 'enhancement/weights.pt'

    # Perform enhancement
    # Execute enhancement using subprocess module
    # Capture output and handle any errors
    try:
        enhancement_command = [
            'python', script_path,
            '--source', input_file_path,
            '--name', output_file_path,
            '--weights', weights
        ]
        result = subprocess.run(enhancement_command, check=True, capture_output=True, text=True)
        message = "Image enhancement completed successfully."
    except subprocess.CalledProcessError as e:
        message = f"Error during image enhancement: {e.stderr}"

    return render_template('index.html', message=message)

# Crack detection route
@app.route('/detect_cracks')
def detect_cracks():
    # Define crack detection model parameters
    model_path = 'CNN/models/imageclassifier.h5'
    image_path = 'enhancement/output/images/'

    # Perform crack detection
    # Call the function for crack detection on enhanced images
    try:
        crack_detection(model_path, image_path)
        message = "Crack detection completed successfully."
    except Exception as e:
        message = f"An error occurred during crack detection: {str(e)}"

    return render_template('index.html', message=message)

# Route to display images with detected cracks
@app.route('/show_cracks')
def show_cracks():
    # Code to display images with detected cracks
    # This could involve fetching the images that were detected with cracks and displaying them on the webpage
    # You might use HTML/CSS/JS or a frontend library like Bootstrap to display the images

    # Example placeholder code to render a template with a message
    return render_template('index.html', message="Images with detected cracks")

if __name__ == '__main__':
    app.run(debug=True)
