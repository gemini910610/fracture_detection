from PIL import ImageDraw

def restore_bbox(image, bbox):
    bbox = bbox * image.size[0]
    return bbox

def restore_origin_bbox(image, origin_image, bbox, padding):
    scale = max(origin_image.size) / image.size[0]
    bbox = bbox * image.size[0]
    bbox = bbox * scale - padding.repeat(2)
    return bbox

def plot_bbox(image, bbox, outline='red', width=3, display=False):
    image = image.convert('RGB')
    bbox = bbox.tolist()
    draw = ImageDraw.Draw(image)
    draw.rectangle(bbox, outline=outline, width=width)
    if display:
        image.show()
    return image

if __name__ == '__main__':
    from datasets import ScaphoidDataset
    from PIL import Image
    from torchvision import transforms

    dataset = ScaphoidDataset('dataset/scaphoid_detection')
    image, bbox, padding, filename = dataset[0]

    to_image = transforms.ToPILImage()
    image = to_image(image)

    image_bbox = restore_bbox(image, bbox)
    plot_bbox(image, image_bbox, display=True)

    origin_image = Image.open(f'dataset/scaphoid_detection/images/{filename}.jpg')
    origin_bbox = restore_origin_bbox(image, origin_image, bbox, padding)
    plot_bbox(origin_image, origin_bbox, width=5, display=True)
