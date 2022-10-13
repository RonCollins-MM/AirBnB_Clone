"""
This module ensures that all previously created objects are reloaded from
storage when app is running.
"""

from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
