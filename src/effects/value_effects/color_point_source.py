from src.effects.value_effects.value_effect import ValueEffect
import numpy as np
import math

class ColorPointSource(ValueEffect):
    """Point-Source which radiates a color over the image. Intensity decreases linear or quadratically with distance.

    """
    def __init__(self, x: float, y: float, color_val: list, strength: float = 1.0, decrease_law: str='quadratic'):
        """Initializes the ColorPointSource

        Args:
            x (float): x-value of pointsource
            y (float): x-value of pointsource
            color_val (list): rgba value of point-source, requires 4 elements: r, g, b, a
            strength (float): scaling factor of how strong the source is, must be bigger 0
            init_alpha (float): alpha value at point-source
            decrease_law (float): supports linear and quadratic
        """
        self.x = x
        self.y = y
        
        assert(len(color_val) == 4)
        self.color_val = color_val
        assert(strength > 0.0)
        self.strength = strength
        assert(decrease_law=='linear' or decrease_law=="quadratic")
        self.decrease_law = decrease_law
        
        # small number to avoid division by 0
        self.epsilon = 10e-5
        
    
    def get_value_at_pixel(self, x: float, y: float) -> list:
        """Computes the color rgba value coming from this source at position x, y 

        Args:
            x (float): x position where the rgba value is computed
            y (float): y position where the rgba value is computed

        Returns:
            list: rgba values as 4 int values between 0 and 255
        """
        dist_squared = (self.x - x)**2 + (self.y - y)**2 + self.epsilon
        if self.decrease_law == 'quadratic':
            val = 255 * self.strength / dist_squared
        elif self.decrease_law == 'linear':
            val = 255 * self.strength / math.sqrt(dist_squared)
        
        col_val = [0, 0, 0, 0]
        col_val[0:4] = self.color_val[0:4]
        col_val[3] *= val
        col_val[3] = int(max(0.0, min(255, col_val[3])))
        
        return col_val
        
    
    def get_values_img(self, img_width: int, img_height: int) -> np.ndarray:
        """Computes the ColorPointSource effect on the entire image.

        Args:
            img_width (int): width of image
            img_height (int): height of image

        Returns:
            np.ndarray: values 
        """
        raise NotImplementedError("Todo!")
        values = np.full((img_height, img_width, 4), [255, 0, 0, 128], dtype=np.uint8)
        return values