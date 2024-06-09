import cv2
import numpy as np
import os

input_dir = 'outtest5/'
output_dir = 'FCNTEST/'

os.makedirs(output_dir, exist_ok=True)

im_names = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

gray_to_color = {
    1: (0, 255, 255),    # urban_land
    2: (255, 255, 0),    # agriculture_land
    3: (255, 0, 255),    # rangeland
    4: (0, 255, 0),      # forest_land
    0: (255, 0, 0),      # water
    5: (255, 255, 255),  # barren_land
    6: (0, 0, 0)         # unknown
}


for im_name in im_names:
    image_path = os.path.join(input_dir, im_name)
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        continue

    rgb_image = np.zeros((*gray_image.shape, 3), dtype=np.uint8)

    for gray_value, color in gray_to_color.items():
        mask = gray_image == gray_value
        rgb_image[mask] = color

    output_filename = os.path.join(output_dir, f'desprocesadas_{im_name}')
    cv2.imwrite(output_filename, rgb_image)