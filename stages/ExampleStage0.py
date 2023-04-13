from stages.IStage import IStage


class ExampleStage0(IStage):

    def run_stage(self, example_str: str):
        self.log_info("Hello World " + example_str)
        # self.log_space()
        self.log_debug("Data Path: " + self.get_file_path_data("test.txt"))
        self.log_debug("Out Path: " + self.get_file_path_out("test.txt"))
        self.log_debug("Cache Path: " + self.get_file_path_cache("test.txt"))
