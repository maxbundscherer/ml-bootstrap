import logging
import os

from framework.Config import LoggingConfig, PathConfig
from framework.Context import Context


class Environment:

    def __init__(self,
                 logging_config: LoggingConfig,
                 file_path_local: str,
                 file_path_data: str = "",
                 env_title: str = "Local",
                 env_id: str = "001_local",
                 ):

        # Logging
        
        logging.basicConfig(level=logging_config.level,
                            format='%(levelname)-8s - %(message)s')  # Default was '%(name)s - %(levelname)-8s - %(message)s'

        # Check local path and env_id

        if not file_path_local.endswith("/"):
            raise ValueError("Local File path must end with '/'")

        if not os.path.exists(file_path_local):
            raise ValueError("Local File path must exist '" + file_path_local + "'")

        if env_id == "" or " " in env_id:
            raise ValueError("Env ID must not be empty or contain spaces")

        # Paths

        if file_path_data != "":
            # Overwritten by user
            if not file_path_data.endswith("/"):
                raise ValueError("Data File path must end with '/'")

            if not os.path.exists(file_path_data):
                raise ValueError("Data File path must exist '" + file_path_data + "'")

        else:
            # Default
            file_path_data = file_path_local + env_id + "/data/"

        # Context

        context = Context(
            path_config=PathConfig(
                file_path_data=file_path_data,
                file_path_out=file_path_local + env_id + "/out/",
                file_path_cache=file_path_local + env_id + "/cache/",
                create_dir_on_demand=False
            ),
            logging_prefix="Env-" + env_id,
            logging_config=logging_config
        )

        # Set attributes

        self._env_title: str = env_title
        self._env_id: str = env_id
        self._context: Context = context
        self._logging_config: LoggingConfig = logging_config

        # Context
        self._registered_contexts: list[Context] = []
        self.register_context(context)

    def start(self):
        self._context.log_info("[Started Environment '" + self._env_title + "']")
        self._context.stopwatch_start("Env-" + self._env_id)

        # self._context.log_debug("Data path: " + self._context.get_file_path_data())
        # self._context.log_debug("Cache path: " + self._context.get_file_path_cache())
        # self._context.log_debug("Out path: " + self._context.get_file_path_out())

    def stop(self):
        o = self._context.stopwatch_stop("Env-" + self._env_id)
        for c in self._registered_contexts:
            c.check_running_stopwatches()
        self._context.log_space()
        self._context.log_info("[Stopped Environment '" + self._env_title + "' (" + o + ")]")

    def register_context(self, context: Context):
        self._registered_contexts.append(context)

    def get_context(self) -> Context:
        return self._context

    def get_logging_config(self) -> LoggingConfig:
        return self._logging_config
