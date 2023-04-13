import logging

from utils import IProjectHandler
from utils.ExampleProjectHandler import ExampleProjectHandler


def run_main():
    project_handler: IProjectHandler = ExampleProjectHandler(
        project_title="Example Project",
        file_path_project="/Users/maximilianbundscherer/Desktop/test/",
        logging_level=logging.DEBUG
    )

    project_handler.log_info("Hello World")


if __name__ == '__main__':
    run_main()
