import os
import tempfile

from monede import settings


class Storage:
    def __init__(self):
        self.__tempdir = tempfile.gettempdir()
        self._cache_dir = os.path.join(self.__tempdir, settings.CACHE_DIR_NAME)

    @property
    def cache_dir(self):
        return self._cache_dir


storage = Storage()
CACHE = storage.cache_dir
