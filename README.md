# Crack Detection Web Application

This project is a web-based application for detecting cracks in images and videos using deep learning. It provides an end-to-end pipeline: video upload, frame extraction, image enhancement, crack detection, and result visualization.

## Project Structure

- `app.py` — Flask web server, handles video upload and orchestrates backend processing.
- `backend.py` — Main backend pipeline: frame extraction, enhancement, crack detection.
- `script/` — Contains scripts for crack detection (`crack.py`, `test.py`) and frame extraction (`video.py`).
- `CNN/` — Deep learning models, training notebooks, and datasets.
- `enhancement/` — Image enhancement scripts and weights.
- `templates/` — HTML templates for web UI.
- `logs/` — Training and validation logs.
- `video/` — Uploaded and processed videos.
- `history/` — Archive of uploaded videos.

## Features

- Upload video via web interface.
- Extract frames from uploaded video.
- Enhance extracted frames using a pre-trained model.
- Detect cracks in enhanced images using a CNN classifier.
- Display and download results.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Crack_detection.git
   cd Crack_detection
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download model weights:**
   - Place your trained model (`imageclassifier.h5`) in `CNN/models/`.
   - Place enhancement weights (`weights.pt`) in `enhancement/`.

## Usage

1. **Start the Flask server:**
   ```sh
   python app.py
   ```

2. **Open your browser:**
   - Go to `http://localhost:5000`
   - Upload a video and view results.

## Training

- Use `CNN/Crack.ipynb` to train your crack detection model.
- Training and validation logs are saved in `logs/`.

## File Descriptions

- [`app.py`](app.py): Main Flask application.
- [`backend.py`](backend.py): Backend pipeline functions.
- [`script/crack.py`](script/crack.py): CNN model definition and training.
- [`script/test.py`](script/test.py): Crack detection on images.
- [`script/video.py`](script/video.py): Frame extraction from video.
- [`enhancement/finalEnhancer.py`](enhancement/finalEnhancer.py): Image enhancement script.

## Requirements

- Python 3.8+
- Flask
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib

## License

MIT License

## Acknowledgements

- Deep learning model inspired by standard CNN architectures.
- Enhancement model based on PyTorch weights.
