import logging
import os
import time

from utils.IProjectHandler import IProjectHandler


class SimpleProjectHandler(IProjectHandler):

    def __init__(
            self,
            file_path_root: str,
            file_path_data: str = "",
            project_title: str = "My Project",
            project_version_tag: str = "v0",
            logging_level: int = logging.DEBUG
    ):
        """
        Simple Project Handler. Automatically creates folders and provides utils.
        :param file_path_root: File Path to Root
        :param file_path_data: File Path to Data (if not specified, it will be set to file_path_project + "data/")
        :param project_title: Title of the Project
        :param project_version_tag: Version Tag of the Project
        :param logging_level: Logging Level
        """

        logging.basicConfig(level=logging_level, format='%(name)s - %(levelname)-8s - %(message)s')

        if not file_path_root.endswith("/"):
            raise ValueError("Root File path must end with '/'")

        if not os.path.exists(file_path_root):
            raise ValueError("Root File path must exist '" + file_path_root + "'")

        if project_version_tag == "":
            raise ValueError("Project Version Tag must not be None")

        self._file_path_project = file_path_root + project_version_tag + "/"

        if file_path_data == "":
            self._file_path_data = self._file_path_project + "data/"
        else:
            self.log_debug("Custom Data Path: '" + file_path_data + "'")

            if not os.path.exists(file_path_data):
                raise ValueError("Data File path must exist '" + file_path_data + "'")

            self._file_path_data = file_path_data

        if not self._file_path_data.endswith("/"):
            raise ValueError("Data File path must end with '/'")

        self._file_path_out = self._file_path_project + "out/"
        self._file_path_cache = self._file_path_project + "cache/"

        self._project_title: str = project_title
        self._project_version_tag: str = project_version_tag

        self._project_stopwatches: dict = {}

        super().__init__()

    def init_project(self):

        self.log_debug("Init Project '" + self._project_title + "' (" + self._project_version_tag + ")")

        self.log_debug("Project Path: '" + self._get_file_path_project() + "'")
        self.log_debug("Data Path: '" + self.get_file_path_data() + "'")
        self.log_debug("Out Path: '" + self.get_file_path_out() + "'")
        self.log_debug("Cache Path: '" + self.get_file_path_cache() + "'")

        if not os.path.exists(self._get_file_path_project()):
            self.log_warning("Create Project Folder '" + self._get_file_path_project() + "'")
            os.makedirs(self._get_file_path_project())

        if not os.path.exists(self.get_file_path_data()):
            self.log_warning("Create Data Folder '" + self.get_file_path_data() + "'")
            os.makedirs(self.get_file_path_data())

        if not os.path.exists(self.get_file_path_out()):
            self.log_warning("Create Output Folder '" + self.get_file_path_out() + "'")
            os.makedirs(self.get_file_path_out())

        if not os.path.exists(self.get_file_path_cache()):
            self.log_warning("Create Cache Folder '" + self.get_file_path_cache() + "'")
            os.makedirs(self.get_file_path_cache())

        self.stopwatch_start("Complete Run")

    def finish_project(self):

        self.log_debug("Finish Project '" + self._project_title + "'")

        self.stopwatch_stop("Complete Run")

        if self._project_stopwatches is not None:
            for key in self._project_stopwatches:
                self.log_warning("Stopwatch '" + key + "' is still running")

    def _get_file_path_project(self) -> str:
        return self._file_path_project

    def get_file_path_data(self) -> str:
        return self._file_path_data

    def get_file_path_out(self) -> str:
        return self._file_path_out

    def get_file_path_cache(self) -> str:
        return self._file_path_cache

    def _start_stopwatch(self, key: str):
        if key in self._project_stopwatches:
            raise ValueError("Stopwatch with key '" + key + "' already exists")
        self._project_stopwatches[key] = time.time()

    def _stop_stopwatch(self, key: str) -> float:
        if key not in self._project_stopwatches:
            raise ValueError("Stopwatch with key '" + key + "' does not exist")
        t = self._project_stopwatches[key]
        del self._project_stopwatches[key]
        return time.time() - t

    def stopwatch_start(self, key: str):
        self.log_debug("Start Stopwatch '" + key + "'")
        self._start_stopwatch(key)

    def stopwatch_stop(self, key: str):
        sec: float = self._stop_stopwatch(key)
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        out: str = "{0}h {1}m {2}s".format(int(hours), int(mins), round(sec, 2))
        self.log_debug("Stop Stopwatch '" + key + "' " + out)

    @staticmethod
    def log_debug(message: str):
        logging.debug(message)

    @staticmethod
    def log_info(message: str):
        logging.info(message)

    @staticmethod
    def log_warning(message: str):
        logging.warning(message)

    @staticmethod
    def log_error(message: str):
        logging.error(message)
