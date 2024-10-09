# tests/test_color_point_source.py

import pytest
from PIL import Image
import numpy as np
from src.effects.value_effects.color_point_source import ColorPointSource


def test_get_value_at_pixel_01():
    # create an empty image as numpy array
    img = np.full((200,200, 4), [255, 255, 255, 255], dtype=np.uint8)
    
    # create ColorPoint Source
    x_source = 100
    y_source = 100
    cps = ColorPointSource(x=x_source, y=y_source, color_val=[255, 0, 0, 1.0], strength=10, decrease_law='linear')
    
    # apply to a line
    x_vals = np.arange(start=0, stop=100, step=1, dtype=np.int32)
    line_x_forward = [cps.get_value_at_pixel(x=x_source + x_val, y=y_source) for x_val in x_vals]
    # for val in line_x_forward:
    #     print(val)
        
    line_x_backward = [cps.get_value_at_pixel(x=x_source - x_val, y=y_source) for x_val in x_vals]
    
    print(f"shape of line_x_forward: {len(line_x_forward)}, {len(line_x_forward[0])}")
    # construct new image
    for idx, x in enumerate(x_vals):
        img[y_source, x_source - x, :] = line_x_backward[idx]
        img[y_source, x_source + x, :] = line_x_forward[idx]
        
    
    # display image using PIL
    print("display!")
    image = Image.fromarray(img, 'RGBA')
    image.show()
    assert(1 == 1)