import json
import os
from pathlib import Path

import numpy as np
from PIL import Image


def vectorize_y(metadata):
    foreground_color = metadata['foreground_color']
    vector = np.array(foreground_color)
    vector = vector / 255
    return vector


def interpret_y_vector(vector):
    r, g, b = list(vector * 255)

    return r, g, b


def get_images(path):
    x = []
    y = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.png'):
                image_file_path = Path(os.path.join(path, filename))
                image = Image.open(image_file_path).convert('RGB')
                image = np.array(image) / 255
                x.append(image)

                metadata_file_path = image_file_path.with_suffix('.json')
                with metadata_file_path.open() as metadata_file:
                    metadata = json.load(metadata_file)
                vector_y = vectorize_y(metadata)
                y.append(vector_y)
        break  # no recursive walk

    x = np.array(x)
    y = np.array(y)
    return x, y
