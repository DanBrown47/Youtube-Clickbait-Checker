import os
import cv2
from PIL import Image 

# ResNet
import torch
import torchvision
import torchvision.transforms as transforms



VID_LOC = "./assets/video"
THUMB_LOC = "./assets/thumbnails/"

thumbnail = os.path.join(THUMB_LOC,os.listdir(THUMB_LOC)[0])
video  = cv2.VideoCapture(os.path.join(VID_LOC,os.listdir(VID_LOC)[0]))


class Click():
    def __init__(self):
        # Loading the model | Pretrained model
        print("loading model")
        model = torchvision.models.resnet50(weights='ResNet50_Weights.DEFAULT')

        # Set to the model evaluation mode
        model.eval()

        transform = transforms.Compose([
                transforms.Resize(256),
                    transforms.CenterCrop(224),
                        transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                            ])
        
        # Calling the driver function
        self.Frames_similarity_index = process()
        


        


    def sim_resnet(image1, image2) -> float:
        # Pass the images through the ResNet model to get the output feature vectors
        feature_vector1 = model(image1).squeeze()
        feature_vector2 = model(image2).squeeze()

        # Calculate the cosine similarity between the feature vectors
        similarity = torch.nn.functional.cosine_similarity(feature_vector1, feature_vector2, dim=0)
        similarity_score = float(similarity.detach_())
        
        return similarity_score


    def process():

        # Iterate through the frames of the video

        Frames_similarity_index = {}
        i = 0

        image1 = Image.open(thumbnail)
        image1 = transform(image1).unsqueeze(0)

        while (video.isOpened()):
            # Read a frame from the video
            ret, frame = video.read()
            if ret == False:
                print("=="*50)
                print("Cannot process the video Aborting  ")
                print("=="*50)
                break
            
            if i%12 == 0:
                
                filename = './frames/frame'+str(i)+'.jpg'
                
                cv2.imwrite(filename, frame) # Is I/O making it slow ?

                image2 = Image.open(filename)
                image2 = transform(image2).unsqueeze(0)

                score = sim_resnet(image1, image2)
                
                print("For Frame {} The score {}".format(i,score))
                Frames_similarity_index[i] = score 

            i+=1   # increment the frames here it is better than going through the entire video
            
            
            # Release the video capture object
        video.release()

        return Frames_similarity_index

    # Load the images and apply the transformation
