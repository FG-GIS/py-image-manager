import pathlib

class Image:
    def __init__(self,path: pathlib.Path) -> None:
        self.location = path
        self.size = path.stat().st_size
        pass

# what data do I want to extract from exif?
# define accepted formats (research what pillow/python supports)
