from aggregates.Config import PathConfig, LoggingConfig
from utils.Context import Context
from utils.Environment import Environment


class Stage:

    def __init__(self,
                 env: Environment,
                 logging_config: LoggingConfig,
                 stage_title: str = "My Stage",
                 stage_id: str = "01-my-stage",
                 ):

        # Check stage_id and stage_title

        if stage_title == "":
            raise ValueError("Stage title must not be empty")

        if " " in stage_id or "/" in stage_id or "-" in stage_id:
            raise ValueError("Stage ID must not contain spaces, slashes or dashes")

        # Paths

        path_config = PathConfig(
            file_path_data=env.get_context().get_file_path_data(),
            file_path_out=env.get_context().get_file_path_out(stage_id + "/"),
            file_path_cache=env.get_context().get_file_path_cache(stage_id + "/"),
        )

        # Context

        context = Context(
            path_config=path_config,
            logging_prefix="Stage-" + stage_id,
            logging_config=logging_config
        )

        # Set attributes

        self._context: Context = context
