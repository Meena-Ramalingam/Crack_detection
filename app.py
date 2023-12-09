from flask import Flask, render_template
from CNN.video import extract_frames
from test.test import crack_detection
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_video')
def process_video():
    video_parent_dir = 'video/'
    output_frames_folder = 'frames'
    optional_frame_interval = 60
    
    try:
        x = os.listdir(video_parent_dir)
        video_file_path = os.path.join(video_parent_dir, x[0])
        extract_frames(video_file_path, output_frames_folder, optional_frame_interval)
        message = "Frames extraction completed successfully."
    except Exception as e:
        message = f"An error occurred during frame extraction: {str(e)}"
    
    return render_template('index.html', message=message)

@app.route('/enhance_images')
def enhance_images():
    script_path = 'enhancement/finalEnhancer.py'
    input_file_path = 'frames'
    output_file_path = 'enhancement/output/images'
    weights = 'enhancement/weights.pt'

    try:
        command = [
            'python', script_path,
            '--source', input_file_path,
            '--name', output_file_path,
            '--weights', weights
        ]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        message = "Image enhancement completed successfully."
    except subprocess.CalledProcessError as e:
        message = f"Error during image enhancement: {e.stderr}"
    
    return render_template('index.html', message=message)

# Inside your Flask routes
@app.route('/process_video')
def process_video():
    # ... (your code for video processing)
   
    # After processing, render the template with appropriate data
    return render_template('index.html', message="Frames extraction completed successfully.", images=["image1.jpg", "image2.jpg"])

@app.route('/detect_cracks')
def detect_cracks():
    model_path = 'CNN/models/imageclassifier.h5'
    image_path = 'enhancement/output/images/'

    try:
        crack_detection(model_path, image_path)
        message = "Crack detection completed successfully."
    except Exception as e:
        message = f"An error occurred during crack detection: {str(e)}"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
