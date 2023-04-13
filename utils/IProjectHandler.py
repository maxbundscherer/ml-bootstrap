class IProjectHandler:

    def __init__(self):
        pass

    def init_project(self):
        raise NotImplementedError

    def finish_project(self):
        raise NotImplementedError

    def get_file_path_data(self) -> str:
        raise NotImplementedError

    def get_file_path_out(self) -> str:
        raise NotImplementedError

    def get_file_path_cache(self) -> str:
        raise NotImplementedError

    def stopwatch_start(self, key: str, prefix: str = ""):
        raise NotImplementedError

    def stopwatch_stop(self, key: str, prefix: str = ""):
        raise NotImplementedError

    @staticmethod
    def log_debug(message: str):
        raise NotImplementedError

    @staticmethod
    def log_info(message: str):
        raise NotImplementedError

    @staticmethod
    def log_warning(message: str):
        raise NotImplementedError

    @staticmethod
    def log_error(message: str):
        raise NotImplementedError

    @staticmethod
    def log_space():
        raise NotImplementedError

    def hide_logger_stage_prefix(self) -> bool:
        raise NotImplementedError
