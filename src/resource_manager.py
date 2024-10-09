from PIL import Image
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

class ResourceManager:
    def __init__(self, img: Image, song: AudioFileClip=None):
        self.img = img.convert('RGBA')
        self.song = song
    
    # def add_effect()
    
    def show_img(self, timestamp:float=0.0):
        self.img.show()