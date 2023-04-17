import logging
import pathlib

from framework.Config import LoggingConfig
from framework.Environment import Environment
from stages.ExampleStage001 import ExampleStage001, InputExampleStage001, ConfigExampleStage001, OutputExampleStage001
from stages.ExampleStage002 import ExampleStage002, ConfigExampleStage002, InputExampleStage002


def run_main():
    file_path_local = str(pathlib.Path().resolve()) + "/workdir/"  # Get current working directory
    # file_path_local = "/Users/maximilianbundscherer/Desktop/test/"  # Set path manually

    env: Environment = Environment(
        file_path_local=file_path_local,
        file_path_data="",
        env_title="Local",
        env_id="001_local",
        logging_config=LoggingConfig(
            level=logging.DEBUG,
            hide_prefix=False
        ),
    )

    env.start()

    stage_1: ExampleStage001 = ExampleStage001(
        env=env,
        stage_title="Preload Data",
        stage_id="001_preload",
        inp=InputExampleStage001(),
        stage_config=ConfigExampleStage001(
            test_file_name="test.txt"
        )
    )

    # stage_1.preview()
    stage_1_out: OutputExampleStage001 = stage_1.process()

    stage_2: ExampleStage002 = ExampleStage002(
        env=env,
        stage_title="Filter Data",
        stage_id="002_filter",
        inp=InputExampleStage002(
            stage_1_out=stage_1_out
        ),
        stage_config=ConfigExampleStage002()
    )

    # stage_2.preview()
    stage_2.process()

    env.stop()


if __name__ == '__main__':
    run_main()
