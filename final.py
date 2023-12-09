#process:
#video -> frame extraction -> enhancement -> model

#frames extraction parameters (video_file_path, output_frames_folder, optional_frame_interval(60))
from script.video import extract_frames

import os

video_parent_dir = 'video/'
output_frames_folder = 'frames'
optional_frame_interval = 60
x = os.listdir(video_parent_dir)
video_file_path = video_parent_dir + x[0]

extract_frames(video_file_path, output_frames_folder, optional_frame_interval)
print("\n\nEXTRACTION OF FRAMES COMPLETED SUCCESSFULLY\n\n")

#enhancement paramenters (script_path, input_file_path, output_file_fath)
import subprocess

script_path = 'enhancement/finalEnhancer.py'
input_file_path = 'frames'
output_file_path = 'images'
weights = 'enhancement/weights.pt'

def enhancement(script_path, input_file_path, output_file_path, weights):

    command = [
    'python', script_path,
    '--source', input_file_path,
    '--name', output_file_path,
    '--weights', weights
]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("Command output (if available):", e.output)

enhancement(script_path, input_file_path, output_file_path, weights)
print("ENHANCEMENT OF IMAGES COMPLETED SUCCESSFULLY")



#crack detection model parameters (model_path, imgs_path)
from script.test import crack_detection

model_path = 'CNN/models/imageclassifier.h5'
image_path = 'enhancement/output/images/'  
#include '/' at the end of image path sd os.listdir() does not

crack_detection(model_path, image_path)