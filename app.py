import os
from flask import Flask, render_template
from script.test import crack_detection
from final import enhancement
from enhancement.net import Enhancer
from script.video import extract_frames

app = Flask(__name__)

# Video to Frame Extraction
def video_to_frames(video_parent_dir, output_frames_folder, optional_frame_interval=60):
    x = os.listdir(video_parent_dir)
    video_file_path = os.path.join(video_parent_dir, x[0])
    extract_frames(video_file_path, output_frames_folder, optional_frame_interval)
    print("\n\nEXTRACTION OF FRAMES COMPLETED SUCCESSFULLY\n\n")
    return os.path.join(output_frames_folder, x[0])  # Return the path to the frames


# Image Enhancement
def enhance_images(script_path, input_file_path, output_file_path, weights):
    enhancement(script_path, input_file_path, output_file_path, weights)
    print("ENHANCEMENT OF IMAGES COMPLETED SUCCESSFULLY")


# Crack Detection and Image Display
def detect_and_display_cracks(model_path, image_path):
    return crack_detection(model_path, image_path)


@app.route('/')
def display_cracked_images():
    # Set up paths and parameters
    video_parent_dir = 'video/'
    output_frames_folder = 'frames'
    optional_frame_interval = 60
    script_path = 'enhancement/finalEnhancer.py'
    input_file_path = 'frames'
    output_file_path = 'images'
    weights = 'enhancement/weights.pt'
    model_path = 'CNN/models/imageclassifier.h5'
    image_path = 'enhancement/output/images/'

    # Process steps
    frames_folder = video_to_frames(video_parent_dir, output_frames_folder, optional_frame_interval)
    enhance_images(script_path, frames_folder, output_file_path, weights)
    cracked_images = detect_and_display_cracks(model_path, image_path)
    
    # Render HTML to display cracked images
    return render_template('display_images.html', images=cracked_images)


if __name__ == '__main__':
    app.run(debug=True)
