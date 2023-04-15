class PathConfig:
    def __init__(self,
                 file_path_data: str,
                 file_path_out: str,
                 file_path_cache: str):
        self.file_path_data: str = file_path_data
        self.file_path_out: str = file_path_out
        self.file_path_cache: str = file_path_cache


class LoggingConfig:
    def __init__(self,
                 level: int,
                 hide_prefix: bool):
        self.level: int = level
        self.hide_prefix: bool = hide_prefix
