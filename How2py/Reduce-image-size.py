import cv2

IMAGE_SIZE = 64
PATH = "../current_dir/"

def change_size(img_id, resized_dim = IMAGE_SIZE)

  img = cv2.imread(img_id)
  resized_img = cv2_resize(img, (resized_dim,)*2.astype('uint8')
  
  return resized_img
  
  
resized = []

for img_id in list_of_files:
  
  resized_img = change_size(img_id)
  resized.append(resized_img)
