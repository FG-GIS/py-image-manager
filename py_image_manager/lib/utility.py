import pathlib

class Image:
    def __init__(self,path: pathlib.Path) -> None:
        self.location = path
        self.size = path.stat().st_size
        pass
