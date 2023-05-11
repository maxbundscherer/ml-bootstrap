from dataclasses import dataclass


@dataclass
class LoggingConfig:
    level: int
    hide_prefix: bool


@dataclass
class PathConfig:
    file_path_data: str
    file_path_out: str
    file_path_cache: str
    flush_cache_dir: bool
    flush_out_dir: bool
    create_dir_on_demand: bool
