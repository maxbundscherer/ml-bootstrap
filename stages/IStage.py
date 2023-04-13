import os

from utils.IProjectHandler import IProjectHandler


class IStage:

    def __init__(self, project_handler: IProjectHandler, stage_title: str, stage_identifier: str):
        """
        Abstract Stage
        :param project_handler: Project Handler
        :param stage_title: Title of the Stage
        :param stage_identifier: Identifier of the Stage (no special characters, used for file paths
        """
        self._project_handler: IProjectHandler = project_handler

        if " " in stage_identifier or "/" in stage_identifier or "-" in stage_identifier:
            raise ValueError("Stage Identifier must not contain spaces, slashes or dashes")

        self._stage_title: str = stage_title
        self._stage_identifier: str = stage_identifier

        self._file_path_data = self._project_handler.get_file_path_data()
        self._file_path_out = self._project_handler.get_file_path_out() + "stage-" + stage_identifier + "/"
        self._file_path_cache = self._project_handler.get_file_path_cache() + "stage-" + stage_identifier + "/"

        if self._project_handler.hide_logger_stage_prefix():
            self._log_prefix = ""
        else:
            self._log_prefix = "(" + self._stage_identifier + ") "

    def init_stage(self):
        self.log_space()
        self.log_info("Init Stage '" + self._stage_title + "' (" + self._stage_identifier + ")")

        if not os.path.exists(self.get_file_path_out()):
            os.makedirs(self.get_file_path_out())

        if not os.path.exists(self.get_file_path_cache()):
            os.makedirs(self.get_file_path_cache())

        self.stopwatch_start("Stage-" + self._stage_identifier)

    def finish_stage(self):
        self.stopwatch_stop("Stage-" + self._stage_identifier)
        self.log_debug("Finish Stage '" + self._stage_title + "' (" + self._stage_identifier + ")")

    def run_stage(self):
        raise NotImplementedError

    def get_file_path_data(self, file_path_sub: str = "") -> str:
        return self._file_path_data + file_path_sub

    def get_file_path_out(self, file_path_sub: str = "") -> str:
        return self._file_path_out + file_path_sub

    def get_file_path_cache(self, file_path_sub: str = "") -> str:
        return self._file_path_cache + file_path_sub

    def log_debug(self, message: str):
        self._project_handler.log_debug(self._log_prefix + message)

    def log_info(self, message: str):
        self._project_handler.log_info(self._log_prefix + message)

    def log_warning(self, message: str):
        self._project_handler.log_warning(self._log_prefix + message)

    def log_error(self, message: str):
        self._project_handler.log_error(self._log_prefix + message)

    def log_space(self):
        self._project_handler.log_space()

    def stopwatch_start(self, key: str):
        self._project_handler.stopwatch_start(key, prefix=self._log_prefix)

    def stopwatch_stop(self, key: str):
        self._project_handler.stopwatch_stop(key, prefix=self._log_prefix)