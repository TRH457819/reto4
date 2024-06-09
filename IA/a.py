import os

directory = 'train/'

part_to_remove = 'processed_'

for filename in os.listdir(directory):
    if filename.endswith('.png'):
        if part_to_remove in filename:
            new_filename = filename.replace(part_to_remove, '')
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_filename}')
