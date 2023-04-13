from utils.IProjectHandler import IProjectHandler
from stages.IStage import IStage
from stages import ExampleStage0


class ExampleStage1(IStage):

    def __init__(self,
                 project_handler: IProjectHandler,
                 stage_title: str,
                 stage_identifier: str,
                 example_stage_0: ExampleStage0,
                 ):
        super().__init__(project_handler, stage_title, stage_identifier)

        self.test_artifact_path: str = example_stage_0.test_artifact_path

    def run_stage(self):
        self._sample_read()

    def _sample_read(self):
        self.log_info("This is a Test Read from " + self.test_artifact_path)

        with open(self.test_artifact_path, "r") as file:
            self.log_info("Read: " + file.read())
