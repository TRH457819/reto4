import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

input_dir = 'train/'

im_names = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

#images = []
for im_name in im_names:
    image_path = os.path.join(input_dir, im_name)
    image = cv2.imread(image_path)
    print(f'imagen {im_name}: {np.unique(image)}')