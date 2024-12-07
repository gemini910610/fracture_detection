import json
import os
import torch
from PIL import Image
from transforms import SquarePadding
from torch.utils.data import Dataset
from torchvision import transforms

class ScaphoidDataset(Dataset):
    def __init__(self, path, image_size=512):
        self.path = path
        self.filenames = [
            file.replace('.jpg', '')
            for file in os.listdir(f'{self.path}/images')
            if file.endswith('AP.jpg')
        ]
        self.image_size = image_size
        self.to_square_tensor = transforms.Compose([
            transforms.ToTensor(),
            SquarePadding()
        ])
        self.resize = transforms.Resize(image_size)
        self.length = len(self.filenames)

    def __getitem__(self, index):
        filename = self.filenames[index]
        origin_image = Image.open(f'{self.path}/images/{filename}.jpg')
        image, padding = self.to_square_tensor(origin_image)
        origin_size = image.size(1)
        image = self.resize(image)
        
        with open(f'{self.path}/annotations/{filename}.json') as file:
            annotation = json.load(file)
        origin_bbox = torch.tensor([int(box) for box in annotation[0]['bbox']])
        scale = self.image_size / origin_size
        bbox = (origin_bbox + padding.repeat(2)) * scale
        return image, bbox, padding, filename

    def __len__(self):
        return self.length

if __name__ == '__main__':
    from table import Table

    dataset = ScaphoidDataset('dataset/scaphoid_detection')
    image, bbox, padding, filename = dataset[0]

    table = Table(
        title='Scaphoid Detection',
        headers=['Object', 'Shape'],
        contents={
            'Image': tuple(image.shape),
            'Bounding Box': tuple(bbox.shape),
            'Padding': tuple(padding.shape),
            'Filename': filename
        }
    )
    table.display()
