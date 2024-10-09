import sys
import os
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.test_file import greet
from src.resource_manager import ResourceManager


if __name__ == "__main__":
    # load image
    img_path = 'resources/images/test_img.png'
    img = Image.open(img_path).convert('RGBA')
    
    # initialize resource manager
    rscmanager = ResourceManager(img)
    
    
    rscmanager.show_img(timestamp=0.0)
    
    print(greet('Wolrd'))
