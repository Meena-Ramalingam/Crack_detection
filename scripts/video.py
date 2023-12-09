import cv2
import os
import shutil

def extract_frames(video_path, output_folder, frame_interval=60):
    # Create the output folder if it doesn't exist
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    success, image = video_capture.read()
    count = 0

    # Read frames until there are no more frames
    while success:
        if count % frame_interval == 0:
            # Save frame as a PNG file
            frame_path = os.path.join(output_folder, f"frame_{count:04d}.png")
            cv2.imwrite(frame_path, image)

        success, image = video_capture.read()
        count += 1

    video_capture.release()

# Example usage:
#video_file_path = 'video/vid.mp4'
#output_frames_folder = 'raw_imgs'
#frame_interval = 30  # Change this value to save every 100th or 200th frame

#extract_frames(video_file_path, output_frames_folder, frame_interval)
