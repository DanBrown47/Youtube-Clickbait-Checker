# Youtube-Clickbait-Checker

Find if the Youtube Thumbnail is a clickbait or not

# Installation

1. Download the code to PC
2. Install all the requirments
   `pip3 install -r requirments.txt`
3. Run the service
   `python3 app.py`

# Clickbait Dectection

### Algorithms

1. SSIM -> Structural Integrity

|
| To compare differences and determine the exact discrepancies between two images, we can utilize Structural Similarity Index (SSIM) which was introduced in Image Quality Assessment: From Error Visibility to Structural Similarity. SSIM is an image quality assessment approach which estimates the degradation of structural similarity based on the statistical properties of local information between a reference and a distorted image. The range of SSIM values extends between [-1, 1] and it typically calculated using a sliding window in which the SSIM value for the whole image is computed as the average across all individual window results. This method is already implemented in the scikit-image library for image processing and can be installed with pip install scikit-image.
|
| The skimage.metrics.structural_similarity() function returns a comparison score and a difference image, diff. The score represents the mean SSIM score between two images with higher values representing higher similarity. The diff image contains the actual image differences with darker regions having more disparity. Larger areas of disparity are highlighted in black while smaller differences are in gray
|

2. Dense Vector Representations | Deep Leaning Approach
   |
   | Typically, two images will not be exactly the same. They may have variations with slightly different backgrounds, dimensions, feature additions/subtractions, or transformations (scaled, rotated, skewed). In other words, we cannot use a direct pixel-to-pixel approach since with variations, the problem shifts from identifying pixel-similarity to object-similarity. We must switch to deep-learning feature models instead of comparing individual pixel values.
   |
   | To determine identical and near-similar images, we can use the the sentence-transformers library which provides an easy way to compute dense vector representations for images and the OpenAI Contrastive Language-Image Pre-Training (CLIP) Model which is a neural network already trained on a variety of (image, text) pairs. The idea is to encode all images into vector space and then find high density regions which correspond to areas where the images are fairly similar.
   |
   | When two images are compared, they are given a score between 0 to 1.00. We can use a threshold parameter to identify two images as similar or different. A lower threshold will result in clusters which have fewer similar images in it. Conversely, a higher threshold will result in clusters that have more similar images. A duplicate image will have a score of 1.00 meaning the two images are exactly the same. To find near-similar images, we can set the threshold to any arbitrary value, say 0.9. For instance, if the determined score between two images are greater than 0.9 then we can conclude they are near-similar images.
   |
