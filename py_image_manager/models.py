from pathlib import Path

class ImageData:
    def __init__(self,path: Path) -> None:
        self.location = path
        self.size = path.stat().st_size

# what data do I want to extract from exif?
# define accepted formats (research what pillow/python supports)
