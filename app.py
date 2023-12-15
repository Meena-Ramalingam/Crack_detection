# from flask import Flask, render_template,request,jsonify
# # from script.test import crack_detection
# import cv2
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
    
#     return render_template('display_images.html')

# @app.route('/saveVideo', methods=['POST'])
# def save_video():
#     if 'video' not in request.files:
#         return jsonify({'error': 'No video found'}), 400
    
#     video = request.files['video']
#     video.save('video/recorded_video.webm')
#     video.save('history/recorded_video.webm')
    
#     return jsonify({'message': 'File saved successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import os
# import uuid  # Python library for generating unique IDs
# from script.video import extract_frames
# import cv2
# import opencv

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('display_images.html')

# @app.route('/saveVideo', methods=['POST'])
# def save_video():
#     if 'video' not in request.files:
#         return jsonify({'error': 'No video found'}), 400
    
#     video = request.files['video']
    
#     # Generate a unique filename for the history directory
#     unique_filename = str(uuid.uuid4()) + '.webm'

#     history_path = os.path.join('history', unique_filename)
#     video.save(history_path)

#     # Replace the existing file in the video directory with the new one
#     video_path ='video/recorded_video.webm'

#     if os.path.exists(video_path):
#         os.remove(video_path)
#     video.save(video_path)

#     # video_file_path = 'video/recorded_video.webm'

#     # output_frames_folder = 'raw_imgs'
#     # frame_interval = 30  # Change this value to save every 100th or 200th frame
#     # extract_frames(video_file_path, output_frames_folder, frame_interval)


#     return jsonify({'message': 'File saved successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify,render_template, request, jsonify
import os
import uuid
import cv2

import backend


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('display_images.html')

@app.route('/saveVideo', methods=['POST'])
def save_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video found'}), 400
    
    video = request.files['video']
    
    # Generate a unique filename for the history directory
    unique_filename = str(uuid.uuid4()) + '.webm'

    history_path = os.path.join('history/', unique_filename)
    video.save(history_path)
    
    # Replace the existing file in the video directory with the new one
    video_path = 'video/recorded_video.webm'

    if os.path.exists(video_path):
        os.remove(video_path)
    video.save(video_path)

    return jsonify({'message': 'Files saved successfully'}), 200

@app.route('/saveVideoToVideoFolder', methods=['POST'])
def save_video_to_video_folder():
    if 'video' not in request.files:
        return jsonify({'error': 'No video found'}), 400
    
    video = request.files['video']

    video_path ='video/recorded_video.webm'
    
    if os.path.exists(video_path):
        os.remove(video_path)
    video.save(video_path)

    backend.frame_extraction()
    backend.enhancement()
    l1 = backend.crack_processing()
    print(l1)


    





    return jsonify({'message': 'File saved in video folder successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
