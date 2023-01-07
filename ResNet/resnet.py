from PIL import Image
import torch
import torchvision
import torchvision.transforms as transforms

# Load the ResNet model
model = torchvision.models.resnet50(pretrained=True)

# Set the model to evaluation mode
model.eval()

# Define the transformation to apply to the images
transform = transforms.Compose([
        transforms.Resize(256),
            transforms.CenterCrop(224),
                transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                    ])

# Load the images and apply the transformation
image1 = Image.open('thumbnail.jpg')
image1 = transform(image1).unsqueeze(0)

image2 = Image.open('frame.jpg')
image2 = transform(image2).unsqueeze(0)

# Pass the images through the ResNet model to get the output feature vectors
feature_vector1 = model(image1).squeeze()
feature_vector2 = model(image2).squeeze()

# Calculate the cosine similarity between the feature vectors
similarity = torch.nn.functional.cosine_similarity(feature_vector1, feature_vector2, dim=0)

print(similarity)

