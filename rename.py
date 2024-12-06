import json
import os
import re
import shutil
from PIL import Image
from tqdm_rich import tqdm

image_dir = './ip_homework_data/scaphoid_detection/images'
scaphoid_annotation_dir = './ip_homework_data/scaphoid_detection/annotations'
fracture_annotation_dir = './ip_homework_data/fracture_detection/annotations'

new_scaphoid_dir = './dataset/scaphoid_detection'
new_fracture_dir = './dataset/fracture_detection'

os.makedirs(f'{new_scaphoid_dir}/images')
os.makedirs(f'{new_scaphoid_dir}/annotations')
os.makedirs(f'{new_fracture_dir}/images')
os.makedirs(f'{new_fracture_dir}/annotations')

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
for image_filename in tqdm(files):
    pattern = r'^(\d+).?([LR])?.*[ -](\S+)\.jpg'
    id, hand, side = re.search(pattern, image_filename).groups()
    side = new_sides[side]
    new_image_filename = f'{id}_{side}.jpg' if hand is None else f'{id}_{hand}_{side}.jpg'
    image = Image.open(f'{image_dir}/{image_filename}')
    image.save(f'{new_scaphoid_dir}/images/{new_image_filename}')

    filename = image_filename.replace('jpg', 'json')
    filename = filename.replace('OB', 'AP')
    new_filename = new_image_filename.replace('jpg', 'json')
    shutil.copyfile(f'{scaphoid_annotation_dir}/{filename}', f'{new_scaphoid_dir}/annotations/{new_filename}')
    shutil.copyfile(f'{fracture_annotation_dir}/{filename}', f'{new_fracture_dir}/annotations/{new_filename}')

    with open(f'{scaphoid_annotation_dir}/{filename}') as file:
        annotation = json.load(file)
    bbox = [int(box) for box in annotation[0]['bbox']]
    image = image.crop(bbox)
    image.save(f'{new_fracture_dir}/images/{new_image_filename}')
