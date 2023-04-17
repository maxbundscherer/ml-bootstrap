from dataclasses import dataclass


@dataclass
class LoggingConfig:
    level: int
    hide_prefix: bool
