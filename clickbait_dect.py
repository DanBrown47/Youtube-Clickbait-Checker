import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim



VID_LOC = "./assets/video"
THUMB_LOC = "./assets/thumbnails/"


def get_ssim_score(image, frame):

    height1, width1, _ = frame.shape
    height2, width2, _ = image.shape

    # Find the maximum dimensions
    max_height = max(height1, height2)
    max_width = max(width1, width2)

    # Create empty images with the maximum dimensions
    image1_resized = np.zeros((max_height, max_width, 3), np.uint8)
    image2_resized = np.zeros((max_height, max_width, 3), np.uint8)

    # Resize the images to the maximum dimensions
    image1_resized = cv2.resize(frame, (max_width, max_height), interpolation=cv2.INTER_CUBIC)
    image2_resized = cv2.resize(image, (max_width, max_height), interpolation=cv2.INTER_CUBIC)

    # Convert the images to grayscale
    image1_gray = cv2.cvtColor(image1_resized, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)

    # Compute the SSIM value
    score = ssim(image1_gray, image2_gray)

    return score




image = cv2.imread(os.path.join(THUMB_LOC,os.listdir(THUMB_LOC)[0]))

video  = cv2.VideoCapture(os.path.join(VID_LOC,os.listdir(VID_LOC)[0]))
# Check if the video file is opened successfully
if not video.isOpened():
    print('Error opening video file')


ret, frame = video.read()
i = 0
while ret:
    # Process the frame here
    # ...
    
    # Read the next frame
    
    i=i+1
    timestamp = video.get(cv2.CAP_PROP_POS_MSEC)
    score = get_ssim_score(frame, image)
    print("{} frame with SSIM Score as {:.5f} at {} timestamp".format(i, score,  timestamp))
    ret, frame = video.read()
