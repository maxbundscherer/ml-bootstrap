import logging
import os


class IProjectHandler:

    def __init__(self, project_title: str, file_path_project: str, logging_level: int = logging.DEBUG):

        if not project_title:
            raise ValueError("Project title must not be empty")

        if not file_path_project.endswith("/"):
            raise ValueError("Project file path must end with '/'")

        self._project_title: str = project_title
        self._file_path_project: str = file_path_project

        self._init_project(logging_level)

    def _init_project(self, logging_level: int):

        logging.basicConfig(level=logging_level, format='%(name)s - %(levelname)-8s - %(message)s')

        self.log_debug("Start Init Project\t'" + self._project_title + "'")

        self.log_debug("Data Path:\t\t\t'" + self._get_file_path_project() + "'")

        if not os.path.exists(self._get_file_path_project()):
            self.log_warning("Create Project Folder '" + self._get_file_path_project() + "'")
            os.makedirs(self._get_file_path_project())

        if not os.path.exists(self.get_file_path_data()):
            self.log_warning("Create Data Folder '" + self.get_file_path_data() + "'")
            os.makedirs(self.get_file_path_data())

        if not os.path.exists(self.get_file_path_output()):
            self.log_warning("Create Output Folder '" + self.get_file_path_output() + "'")
            os.makedirs(self.get_file_path_output())

        if not os.path.exists(self.get_file_path_cache()):
            self.log_warning("Create Cache Folder '" + self.get_file_path_cache() + "'")
            os.makedirs(self.get_file_path_cache())

        self.log_debug("End Init Project\t\t'" + self._project_title + "'")

    def _get_file_path_project(self) -> str:
        return self._file_path_project

    def get_file_path_data(self) -> str:
        return self._get_file_path_project() + "data/"

    def get_file_path_output(self) -> str:
        return self._get_file_path_project() + "output/"

    def get_file_path_cache(self) -> str:
        return self._get_file_path_project() + "cache/"

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
