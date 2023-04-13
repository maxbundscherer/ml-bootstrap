import logging

from utils import IProjectHandler
from utils.SimpleProjectHandler import SimpleProjectHandler


def run_main():
    project_handler: IProjectHandler = SimpleProjectHandler(
        file_path_root="/Users/maximilianbundscherer/Desktop/test/",
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
