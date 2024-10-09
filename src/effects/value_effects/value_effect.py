import numpy as np

class ValueEffect:
    """Virtual Base class for effects which add rgba values to an image.
    """
    def __init__(self):
        pass
    
    def get_value_at_pixel(self, x: float, y: float) -> list:
        raise NotImplementedError("Subclass must override this method")
        
    
    def get_values_img(self, img_width: int, img_height: int) -> np.ndarray:
        raise NotImplementedError("Subclass must override this method")
       