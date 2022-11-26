#!/usr/bin/python3

"""Init file for models folder."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
