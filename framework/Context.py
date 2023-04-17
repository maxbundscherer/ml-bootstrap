import logging
import os
import time

from framework.Config import PathConfig, LoggingConfig


class Context:

    def __init__(self,
                 path_config: PathConfig,
                 logging_config: LoggingConfig,
                 logging_prefix: str,
                 ):

        # Logging

        logging.basicConfig(level=logging_config.level,
                            format='%(levelname)-8s - %(message)s')  # Default was '%(name)s - %(levelname)-8s - %(message)s'

        if logging_config.hide_prefix:
            self._logging_prefix = ""
        else:
            self._logging_prefix = "[" + logging_prefix + "] "

        # Paths

        if not path_config.file_path_data.endswith("/"):
            raise ValueError("Data File path must end with '/'")

        if not path_config.file_path_out.endswith("/"):
            raise ValueError("Out File path must end with '/'")

        if not path_config.file_path_cache.endswith("/"):
            raise ValueError("Cache File path must end with '/'")

        self._path_config: PathConfig = path_config

        self._is_created_data = False
        self._is_created_out = False
        self._is_created_cache = False

        if path_config.create_dir_on_demand is False:
            # Create not on demand

            self._create_path_data()
            self._create_path_out()
            self._create_path_cache()

        # Stopwatches

        self._stopwatches: dict = {}

    def _create_path_data(self):
        if not os.path.exists(self._path_config.file_path_data):
            self.log_debug("[Create Data Folder '" + self._path_config.file_path_data + "']")
            os.makedirs(self._path_config.file_path_data)
        self._is_created_data = True

    def _create_path_out(self):
        if not os.path.exists(self._path_config.file_path_out):
            self.log_debug("[Create Output Folder '" + self._path_config.file_path_out + "']")
            os.makedirs(self._path_config.file_path_out)
        self._is_created_out = True

    def _create_path_cache(self):
        if not os.path.exists(self._path_config.file_path_cache):
            self.log_debug("[Create Cache Folder '" + self._path_config.file_path_cache + "']")
            os.makedirs(self._path_config.file_path_cache)
        self._is_created_cache = True

    def get_file_path_data(self, file_path_sub: str = "") -> str:
        if self._is_created_data is False:
            self._create_path_data()
        return self._path_config.file_path_data + file_path_sub

    def get_file_path_out(self, file_path_sub: str = "") -> str:
        if self._is_created_out is False:
            self._create_path_out()
        return self._path_config.file_path_out + file_path_sub

    def get_file_path_cache(self, file_path_sub: str = "") -> str:
        if self._is_created_cache is False:
            self._create_path_cache()
        return self._path_config.file_path_cache + file_path_sub

    def _start_stopwatch(self, key: str):
        if key in self._stopwatches:
            raise ValueError("Stopwatch with key '" + key + "' already exists")
        self._stopwatches[key] = time.time()

    def _stop_stopwatch(self, key: str) -> float:
        if key not in self._stopwatches:
            raise ValueError("Stopwatch with key '" + key + "' does not exist")
        t = self._stopwatches[key]
        del self._stopwatches[key]
        return time.time() - t

    def stopwatch_start(self, key: str):
        # self.log_debug("Start Stopwatch '" + key + "'")
        self._start_stopwatch(key)

    def stopwatch_stop(self, key: str) -> str:
        sec: float = self._stop_stopwatch(key)
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        out: str = "{0}h {1}m {2}s".format(int(hours), int(mins), round(sec, 2))
        # self.log_debug("Stop Stopwatch '" + key + "' " + out)
        return out

    def log_debug(self, message: str):
        logging.debug(self._logging_prefix + message)

    def log_info(self, message: str):
        logging.info(self._logging_prefix + message)

    def log_warning(self, message: str):
        logging.warning(self._logging_prefix + message)

    def log_error(self, message: str):
        logging.error(self._logging_prefix + message)

    @staticmethod
    def log_space():
        logging.info("")
