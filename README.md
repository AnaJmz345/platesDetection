# Plates detection
This project applies a sequence of computer vision techniques to detect and extract license plate numbers from images. It uses grayscale conversion to simplify data, Gaussian blur to suppress background noise and highlight prominent characters, Canny edge detection to outline the plate number, and EasyOCR to read the plate number

## Requirements

- Install OpenCV:
```
pip install opencv-python
```

- Install EasyOCR:
```
pip install easyocr
```

## Functionality

- Each plate image is displayed in two windows:
  - One with the blurred image.
  - One with the result of the Canny edge detection.
- Press any key to close the current windows and continue to the next plate.
- The detected text for each plate will be printed in the console.

## Execution

Run the script from your terminal using:
```
python -u "path in which you downloaded the repository/deteccionPlacas.py" 
```