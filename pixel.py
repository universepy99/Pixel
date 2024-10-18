import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

def blend(image1, op1, image2, op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1 * op1) + (img2 * op2)
    imgBlend = np.clip(imgBlend, 0, 255)
    return imgBlend.astype(np.uint8)

img1 = img.imread("C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\latihan\\img1_resized.jpg")
img2 = img.imread("C:\\Users\\ASUS VIVOBOOK GO14\\Documents\\latihan\\img2_resized (1).jpg")

imgBlend = blend(img1, 0.3, img2, 0.7)


plt.figure(figsize=(10, 10))
plt.subplot(3, 2, 1)
plt.imshow(img1)
plt.axis('off') 
plt.subplot(3, 2, 3)
plt.imshow(img2)
plt.axis('off')
plt.subplot(3, 2, 5)
plt.imshow(imgBlend)
plt.axis('off')


plt.subplot(3, 2, 2) 
plt.hist(imgBlend.ravel(), bins=256, color='gray', alpha=0.7)
plt.title('Histogram of Blended Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 2, 4)  
plt.hist(img1.ravel(), bins=256, color='blue', alpha=0.7)
plt.title('Histogram of Image 1')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 2, 6) 
plt.hist(img2.ravel(), bins=256, color='red', alpha=0.7)
plt.title('Histogram of Image 2')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()  
plt.show()