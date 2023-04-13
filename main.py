import logging
# import pathlib

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
        logging_level=logging.DEBUG
    )

    project_handler.init_project()

    project_handler.log_info("Hello World")

    project_handler.finish_project()


if __name__ == '__main__':
    run_main()
