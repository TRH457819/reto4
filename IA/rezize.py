from PIL import Image
import os

def resize_image(input_path, output_path, size, keep_aspect_ratio=True):
    with Image.open(input_path) as img:
        if keep_aspect_ratio:
            img.thumbnail(size, Image.Resampling.LANCZOS)
        else:
            img = img.resize(size, Image.Resampling.LANCZOS)
        
        img.save(output_path)

def resize_images_in_directory(input_dir, output_dir, size, keep_aspect_ratio=True):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            resize_image(input_path, output_path, size, keep_aspect_ratio)


resize_images_in_directory('valid', 'eee', (1024,1024), True)
