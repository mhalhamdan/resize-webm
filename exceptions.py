# Exceptions for WEBMResizer
class InvalidWebmFile(Exception):
    def __init__(self, file_object) -> None:
        self.message = f"{file_object} is not a valid .webm file"
    
    def __str__(self) -> str:
        return self.message