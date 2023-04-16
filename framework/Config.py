from dataclasses import dataclass


@dataclass
class PathConfig:
    file_path_data: str
    file_path_out: str
    file_path_cache: str


@dataclass
class LoggingConfig:
    level: int
    hide_prefix: bool
