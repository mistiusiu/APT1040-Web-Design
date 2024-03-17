#!/usr/bin/python3
"""
Initialize the models package
"""

from os import getenv


storage_t = getenv("<storage_type>")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
"""else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()"""
# Only use else once the file storage engine is built
storage.reload()