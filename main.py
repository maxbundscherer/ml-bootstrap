import logging

from stages.ExampleStage0 import ExampleStage0

from utils import IProjectHandler
from utils.SimpleProjectHandler import SimpleProjectHandler


def run_main():
    # file_path_root = str(pathlib.Path().resolve()) + "/test/"  # Get current working directory
    file_path_root = "/Users/maximilianbundscherer/Desktop/test/"  # Set path manually

    project_handler: IProjectHandler = SimpleProjectHandler(
        file_path_root=file_path_root,
        file_path_data="",
        project_title="My Project",
        project_version_tag="v0",
        logging_level=logging.DEBUG,
        hide_logger_stage_prefix=False
    )

    project_handler.init_project()

    stage_0: ExampleStage0 = ExampleStage0(
        project_handler=project_handler,
        stage_title="Preload Data",
        stage_identifier="preload",
    )
    stage_0.init_stage()
    stage_0.run_stage(example_str="Bla")
    stage_0.finish_stage()

    stage_1: ExampleStage0 = ExampleStage0(
        project_handler=project_handler,
        stage_title="Preprocess Data",
        stage_identifier="preprocess",
    )
    stage_1.init_stage()
    stage_1.run_stage(example_str="Blub")
    stage_1.finish_stage()

    project_handler.finish_project()


if __name__ == '__main__':
    run_main()
