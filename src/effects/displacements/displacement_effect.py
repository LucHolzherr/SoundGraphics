import numpy as np

class DisplacementEffect:
    """Virtual Base class for effects which displace pixels in an image.
    """
    def __init__(self):
        pass

    def compute_displacement_pixel(self, x: float, y: float) -> list:
        default_displacement = [0.0, 0.0]
        return default_displacement
    
    def compute_displacement_img(self, img_width: int, img_height: int):
        def_displ = np.full((img_width, img_height, 2), [0.0, 0.0], dtype=np.float32)
        return def_displ