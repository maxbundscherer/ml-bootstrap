import logging
import os
import shutil
import time
from dataclasses import dataclass

from framework.Config import LoggingConfig


@dataclass
class PathConfig:
    file_path_data: str
    file_path_out: str
    file_path_cache: str
    flush_cache_dir: bool
    flush_out_dir: bool
    create_dir_on_demand: bool


@dataclass
class SummaryItem:
    message: str


class SummaryText(SummaryItem):
    def __init__(self, message: str):
        super().__init__(message=message)


class SummaryAccuracy(SummaryItem):
    def __init__(self, identifier: str, accuracy: float):
        self.identifier: str = identifier
        self.accuracy: float = accuracy
        super().__init__(message=str(round(accuracy, 3)) + " by " + identifier)


class Context:

    def __init__(self,
                 path_config: PathConfig,
                 logging_config: LoggingConfig,
                 logging_prefix: str,
                 ):

        # Logging

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

        if path_config.flush_cache_dir:
            if os.path.exists(path_config.file_path_cache):
                # os.removedirs() # Complicated (must be empty)
                shutil.rmtree(path_config.file_path_cache)
                self.log_space()
                self.log_debug("[Flush Cache Folder '" + path_config.file_path_cache + "']")

        if path_config.flush_out_dir:
            if os.path.exists(path_config.file_path_out):
                # os.removedirs() # Complicated (must be empty)
                shutil.rmtree(path_config.file_path_out)
                self.log_space()
                self.log_debug("[Flush Out Folder '" + path_config.file_path_out + "']")

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

        # Summary

        self._summary: list[SummaryItem] = []

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

    def list_files_data(self) -> list[str]:
        return os.listdir(self.get_file_path_data())

    def list_files_out(self) -> list[str]:
        return os.listdir(self.get_file_path_out())

    def list_files_cache(self) -> list[str]:
        return os.listdir(self.get_file_path_cache())

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

    def check_running_stopwatches(self):
        for key, value in self._stopwatches.items():
            if value is not None:
                self.log_warning("[Stopwatch '" + key + "' is still running]")

    def summary_add(self, item: SummaryItem):
        self._summary.append(item)

    def summary_print(self):

        sum_text: [SummaryText] = []
        sum_ac: [SummaryAccuracy] = []

        for item in self._summary:

            if isinstance(item, SummaryText):
                sum_text.append(item)
            elif isinstance(item, SummaryAccuracy):
                sum_ac.append(item)
            else:
                raise ValueError("Unknown SummaryItem type")

        sum_ac.sort(key=lambda x: x.accuracy, reverse=True)

        for item in sum_ac:
            item: SummaryAccuracy = item
            self.log_info("[Summary AC] " + item.message)

        for item in sum_text:
            self.log_info("[Summary TX] " + item.message)
