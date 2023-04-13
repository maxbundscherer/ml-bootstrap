import time

from stages.IStage import IStage
from utils.IProjectHandler import IProjectHandler


class ExampleStage0(IStage):

    def __init__(self,
                 project_handler: IProjectHandler,
                 stage_title: str,
                 stage_identifier: str
                 ):
        super().__init__(project_handler, stage_title, stage_identifier)

        self.file_path_test: str = self.get_file_path_out("test.txt")

    def run_stage(self):
        self._first_method()

    def _first_method(self):
        self.log_info("This is a Test. Write to " + self.file_path_test)

        with open(self.file_path_test, "w") as file:
            file.write("Hello World! " + str(time.time()))

        self.log_debug("Data path: " + self.get_file_path_data())
        self.log_debug("Out path: " + self.get_file_path_out())
