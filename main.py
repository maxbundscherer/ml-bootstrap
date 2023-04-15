import logging

from framework.Config import LoggingConfig
from stages.ExampleStage0 import ExampleStage0, InputExampleStage0, ConfigExampleStage0, OutputExampleStage0
from stages.ExampleStage1 import ExampleStage1, InputExampleStage1, ConfigExampleStage1
from framework.Environment import Environment


def run_main():
    # file_path_local = str(pathlib.Path().resolve()) + "/test/"  # Get current working directory
    file_path_local = "/Users/maximilianbundscherer/Desktop/test/"  # Set path manually

    env: Environment = Environment(
        file_path_local=file_path_local,
        file_path_data="",
        env_id="001_local",
        logging_config=LoggingConfig(
            level=logging.DEBUG,
            hide_prefix=False
        ),
    )

    env.start()

    stage_0: ExampleStage0 = ExampleStage0(
        env=env,
        logging_config=LoggingConfig(
            level=logging.DEBUG,
            hide_prefix=False
        ),
        stage_title="Preload Data",
        stage_id="001_preload",
        inp=InputExampleStage0(),
        stage_config=ConfigExampleStage0(
            test_file_name="test.txt"
        )
    )

    # stage_0.preview()
    stage_0_out: OutputExampleStage0 = stage_0.process()

    stage_1: ExampleStage1 = ExampleStage1(
        env=env,
        logging_config=LoggingConfig(
            level=logging.DEBUG,
            hide_prefix=False
        ),
        stage_title="Filter Data",
        stage_id="002_filter",
        inp=InputExampleStage1(
            out_stage_0=stage_0_out
        ),
        stage_config=ConfigExampleStage1()
    )

    # stage_1.preview()
    stage_1.process()

    env.stop()


if __name__ == '__main__':
    run_main()
