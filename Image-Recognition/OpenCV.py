---### cv2 package ###---

# Importing packages
# cv2 is for image processing and computer vision, matplotlib is for displaying images
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Check the version
print(cv2.__version__)

# Reading an image
img = cv2.imread("file.name")
img_grayscale = cv2.imread("file.name", cv2.IMREAD_GRAYSCALE)

# Shape of an image and datatype
print(img.shape)
print(img.dtype)

# Converting image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Saving the image
cv2.imwrite("file.name", img)

---### Plotting(displaying) the images ###---

# Displaying the image
plt.imshow(img)
plt.show()

# For displaying gray-scale images
plt.imshow(img, cmap = "gray")

# Subplotting - displying multiple plots
ax1 = plt.subplot(1,3,1)
plt.title("Input Image")
plt.imshow(img_rgb)
ax2 = plt.subplot(1,3,2)
plt.imshow(img)
ax3=plt.subplot(1,3,3)
plt.imshow(input_image, cmap='gray')  

# Assuming the image is BGR
# Splitting and displaying images
plt.figure(figsize = (15, 15))



# Original image
plt.subplot(1, 4, 1) # Note: originally 'ax1 = plt.subplot(1,4,1)'
plt.title("Original image")
plt.imshow(img_original)

# Grayscale channels of each colour
img_blue_g = img[:,:,0]
img_green_g = img[:,:,1]
img_red_g = img[:,:,2]

# Displaying each channel's intensity
plt.subplot(1, 4, 2)
plt.title("Blue channel")
plt.imshow(img_blue_g)

plt.subplot(1, 4, 3)
plt.title("Green channel") 
plt.imshow(img_green_g)

plt.subplot(1, 4, 4)
plt.title("Red channel")
plt.imshow(img_red_g)

# Channels each colour channel
img_blue = img
img_blue[:, :, 1] = 0
img_blue[:, :, 2] = 0

img_green = img
img_green[:, :, 0] = 0
img_green[:, :, 2] = 0

img_red = img
img_red[:, :, 0] = 0
img_Red[:, :, 1] = 1

# Displaying each colour
plt.figure(figsize = (15, 15))

plt.subplot(1, 4, 1)
plt.title("Original Image")
plt.imshow(img)

plt.subplot(1, 4, 2)
plt.title("Blue channel")
plt.imshow(img_blue)

plt.subplot(1, 4, 3)
plt.title("Green channel")
plt.imshow(img_green)

plt.subplot(1, 4, 4)
plt.title("Red channel")
plt.imshow(img_red)

