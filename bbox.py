from PIL import ImageDraw

def restore_bbox(image, bbox, padding=None):
    bbox = bbox * max(image.size)
    if padding is not None:
        bbox[0] = bbox[0] - padding[0]
        bbox[1] = bbox[1] - padding[1]
    return bbox

def plot_bbox(image, bbox, outline='red', outline_width=3, display=False):
    image = image.convert('RGB')
    x, y, width, height = bbox
    left = x - width / 2
    top = y - height / 2
    right = x + width / 2
    bottom = y + height / 2
    draw = ImageDraw.Draw(image)
    draw.rectangle([left, top, right, bottom], outline=outline, width=outline_width)
    if display:
        image.show()
    return image

if __name__ == '__main__':
    from datasets import ScaphoidDataset
    from PIL import Image
    from torchvision import transforms

    dataset = ScaphoidDataset('dataset/scaphoid_detection')
    image, bbox, padding, filename = dataset[1]

    to_image = transforms.ToPILImage()
    image = to_image(image)

    image_bbox = restore_bbox(image, bbox)
    plot_bbox(image, image_bbox, display=True)

    origin_image = Image.open(f'dataset/scaphoid_detection/images/{filename}.jpg')
    origin_bbox = restore_bbox(origin_image, bbox, padding)
    plot_bbox(origin_image, origin_bbox, outline_width=5, display=True)
