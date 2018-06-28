import json
import os
import random
from pathlib import Path
from uuid import uuid4

from PIL import Image, ImageDraw
from tqdm import tqdm


def generate_image(background_color, foreground_color, image_shape):
    """
    Generate an image with the specified background color and foreground color
    """
    pillow_image = Image.new(
        'RGB',
        image_shape,
        background_color
    )

    draw = ImageDraw.Draw(pillow_image)

    rect_width = int(image_shape[0] * 0.5)
    rect_height = int(image_shape[1] * 0.5)
    rect_offset_x = int(image_shape[0] * 0.25)
    rect_offset_y = int(image_shape[1] * 0.25)
    draw.rectangle(
        (
            (rect_offset_x, rect_offset_y),
            (rect_offset_x + rect_width, rect_offset_y + rect_height),
        ),
        fill=foreground_color,
    )

    del draw

    return pillow_image


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


if __name__ == '__main__':
    image_directory = 'data'
    num_examples = 1000
    image_size = (32, 32)

    for i in tqdm(range(num_examples), desc='Generating examples'):
        image_file_path = Path(os.path.join(image_directory, '{}.png'.format(uuid4().hex)))

        foreground_color = get_random_color()
        background_color = get_random_color()
        image = generate_image(
            background_color=background_color,
            foreground_color=foreground_color,
            image_shape=image_size,
        )
        image.save(image_file_path)

        metadata_file_path = image_file_path.with_suffix('.json')
        metadata = {
            'background_color': background_color,
            'foreground_color': foreground_color,
        }
        with metadata_file_path.open(mode='w') as metadata_file:
            json.dump(metadata, metadata_file)
