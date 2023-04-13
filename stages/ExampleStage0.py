from stages.IStage import IStage


class ExampleStage0(IStage):

    def run_stage(self, example_str: str):
        self.log_info("Hello World " + example_str)
