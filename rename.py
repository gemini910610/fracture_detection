import os
import re
import shutil
from tqdm_rich import tqdm

image_dir = './ip_homework_data/scaphoid_detection/images'
scaphoid_annotation_dir = './ip_homework_data/scaphoid_detection/annotations'
fracture_annotation_dir = './ip_homework_data/fracture_detection/annotations'

new_image_dir = './dataset/images'
new_scaphoid_annotation_dir = './dataset/scaphoid_annotations'
new_fracture_annotation_dir = './dataset/fracture_annotations'

os.makedirs(new_image_dir)
os.makedirs(new_scaphoid_annotation_dir)
os.makedirs(new_fracture_annotation_dir)

new_sides = {
    'AP0': 'AP',
    'LA0': 'LAT',
    'LAT0': 'LAT',
    'LAT20': 'LAT',
    'OB0': 'AP',
    'RAP0': 'R_AP',
    'RLA0': 'R_LAT',
    'SC0': 'AP'
}

files = os.listdir(image_dir)
for filename in tqdm(files):
    pattern = r'^(\d+).?([LR])?.*[ -](\S+)\.jpg'
    id, hand, side = re.search(pattern, filename).groups()
    side = new_sides[side]
    new_filename = f'{id}_{side}.jpg' if hand is None else f'{id}_{hand}_{side}.jpg'
    shutil.copyfile(f'{image_dir}/{filename}', f'{new_image_dir}/{new_filename}')

    filename = filename.replace('jpg', 'json')
    filename = filename.replace('OB', 'AP')
    new_filename = new_filename.replace('jpg', 'json')
    shutil.copyfile(f'{scaphoid_annotation_dir}/{filename}', f'{new_scaphoid_annotation_dir}/{new_filename}')
    shutil.copyfile(f'{fracture_annotation_dir}/{filename}', f'{new_fracture_annotation_dir}/{new_filename}')
