from uuid import uuid4
from os import path

def generate_filename(object, file):
    name, ext = path.splitext(file.filename)
    return f"{uuid4()}{ext}"