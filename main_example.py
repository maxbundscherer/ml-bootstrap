import logging
import pathlib

from framework.Config import LoggingConfig
from framework.Environment import Environment
from stages.ExampleStage001 import ExampleStage001, ExampleStage001Input, ExampleStage001Config, ExampleStage001Output
from stages.ExampleStage002 import ExampleStage002, ExampleStage002Config, ExampleStage002Input, ExampleStage002Output


def run_main():
    # Please don't forget update the test in tests/test_main_example.py
    file_path_local = str(pathlib.Path().resolve()) + "/workdir/"  # Get current working directory
    # file_path_local = "/Users/testuser/Desktop/test/"  # Set path manually

    env: Environment = Environment(
        file_path_local=file_path_local,
        file_path_data="",
        flush_cache_dir=False,
        flush_out_dir=False,
        env_title="Local Example",
        env_id="001_local_example",
        logging_config=LoggingConfig(
            level=logging.DEBUG,
            hide_prefix=False
        ),
    )

    env.start()

    stage_001: ExampleStage001 = ExampleStage001(
        env=env,
        stage_title="Preload Data",
        stage_id="001_preload",
        flush_cache_dir=False,
        flush_out_dir=False,
        ignore_cache=False,
        inp=ExampleStage001Input(
            test_message="Hello"
        ),
        stage_config=ExampleStage001Config(
            test_message_suffix=" World"
        )
    )
    stage_001.preview()
    stage_001_out: ExampleStage001Output = stage_001.process()

    stage_002: ExampleStage002 = ExampleStage002(
        env=env,
        stage_title="Filter Data",
        stage_id="002_filter",
        flush_cache_dir=False,
        flush_out_dir=False,
        ignore_cache=False,
        inp=ExampleStage002Input(
            stage_001_out=stage_001_out
        ),
        stage_config=ExampleStage002Config()
    )
    # stage_002.preview()
    _: ExampleStage002Output = stage_002.process()

    env.stop()


if __name__ == '__main__':
    run_main()
