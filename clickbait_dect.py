import os
import cv2
import numpy as np
import glob
from PIL import Image 
from sentence_transformers import SentenceTransformer, util

# Load the OpenAI CLIP Model
print('Loading CLIP Model...')
model = SentenceTransformer('clip-ViT-B-32')
print('Loading CLIP Model Done')

VID_LOC = "./assets/video"
THUMB_LOC = "./assets/thumbnails/"

thumbnail = cv2.imread(os.path.join(THUMB_LOC,os.listdir(THUMB_LOC)[0]))
video  = cv2.VideoCapture(os.path.join(VID_LOC,os.listdir(VID_LOC)[0]))



# Iterate through the frames of the video
i = 0
while (video.isOpened()):
    # Read a frame from the video
    ret, frame = video.read()

    if ret == False:
        break
    
    if i%12 == 0:
        
        filename = './frames/frame'+str(i)+'.jpg'
        print(filename)    
        cv2.imwrite(filename, frame)
    i+=1   

# Release the video capture object
video.release()


image_names = list(glob.glob('./frames/*.jpg'))
print("Images:", len(image_names))
encoded_image = model.encode([Image.open(filepath) for filepath in image_names], batch_size=128, convert_to_tensor=True, show_progress_bar=True)
# Train

processed_images = util.paraphrase_mining_embeddings(encoded_image)
NUM_SIMILAR_IMAGES = 10


# =================
# NEAR DUPLICATES
# =================
print('Finding near duplicate images...')
# Use a threshold parameter to identify two images as similar. By setting the threshold lower, 
# you will get larger clusters which have less similar images in it. Threshold 0 - 1.00
# A threshold of 1.00 means the two images are exactly the same. Since we are finding near 
# duplicate images, we can set it at 0.99 or any number 0 < X < 1.00.
# threshold = 0.50
near_duplicates = [image for image in processed_images ]

for score, image_id1, image_id2 in near_duplicates[0:NUM_SIMILAR_IMAGES]:
    print("\nScore: {:.3f}%".format(score * 100))
    print(image_names[image_id1])
    print(image_names[image_id2])