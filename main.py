import logging

from utils import IProjectHandler
from utils.ExampleProjectHandler import ExampleProjectHandler


def run_main():
    project_handler: IProjectHandler = ExampleProjectHandler(
        project_title="Example Project",
        file_path_project="/Users/maximilianbundscherer/Desktop/test/",
        logging_level=logging.DEBUG
    )
    project_handler.init_project()

    project_handler.log_info("Hello World")

    project_handler.finish_project()


if __name__ == '__main__':
    run_main()
