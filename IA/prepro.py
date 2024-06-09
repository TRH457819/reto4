import cv2
import numpy as np
import os

input_dir = 'train/'
output_dir = 'train_g/'

os.makedirs(output_dir, exist_ok=True)

im_names = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

images = []
for im_name in im_names:
    image_path = os.path.join(input_dir, im_name)
    image = cv2.imread(image_path)
    if image is not None:
        images.append(image)

color_to_gray = {
    ((0, 250, 250), (0, 255, 255)): 1,  # urban_land
    ((250, 250, 0), (255, 255, 0)): 2,  # agriculture_land
    ((250, 0, 250), (255, 0, 255)): 3,  # rangeland
    ((0, 250, 0), (0, 255, 0)): 4,      # forest_land
    ((0, 0, 250), (0, 0, 255)): 0,      # water
    ((250, 250, 250), (255, 255, 255)): 5,  # barren_land
    ((0, 0, 0), (1, 1, 1)): 6           # unknown
}

for i, image in enumerate(images):

    combined_mask = np.zeros(images[i].shape[:2], dtype=np.uint8)

    for color, gray_value in color_to_gray.items():
        lower, upper = color
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(image, lower, upper)
        combined_mask[mask > 0] = gray_value

    output_filename = os.path.join(output_dir, f'{im_names[i]}')
    cv2.imwrite(output_filename, combined_mask)
