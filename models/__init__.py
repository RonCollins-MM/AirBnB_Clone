"""
This module ensures that all previously created objects are reloaded from
storage when app is running.
"""

from models.engine.file_storage import FileStorage

storage = engine.file_storage.FileStorage()
storage.reload()
