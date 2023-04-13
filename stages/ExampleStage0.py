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

        self.test_artifact_path: str = self.get_file_path_out("test.txt")

    def run_stage(self):
        self._sample_write()

    def _sample_write(self):
        self.log_info("This is a Test. Write to " + self.test_artifact_path)

        with open(self.test_artifact_path, "w") as file:
            file.write("Hello World! " + str(int(time.time())))

        self.log_debug("Data path: " + self.get_file_path_data())
        self.log_debug("Cache path: " + self.get_file_path_cache())
        self.log_debug("Out path: " + self.get_file_path_out())
