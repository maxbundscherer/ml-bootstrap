from stages.ExampleStage0 import OutputExampleStage0
from framework.Stage import Stage
from framework.Context import Context


class InputExampleStage1:
    def __init__(self, out_stage_0: OutputExampleStage0):
        self.out_stage_0: OutputExampleStage0 = out_stage_0


class ConfigExampleStage1:
    pass


class OutputExampleStage1:
    pass


class ExampleStage1(Stage[InputExampleStage1, ConfigExampleStage1, OutputExampleStage1]):

    @staticmethod
    def _preview(context: Context, inp: InputExampleStage1, conf: ConfigExampleStage1):
        pass

    @staticmethod
    def _get_cached(context: Context, inp: InputExampleStage1, conf: ConfigExampleStage1) -> OutputExampleStage1:
        pass

    @staticmethod
    def _process(context: Context, inp: InputExampleStage1, conf: ConfigExampleStage1) -> OutputExampleStage1:
        f = inp.out_stage_0.test_file_path

        with open(f, "r") as file:
            context.log_info("This is a Test Read from " + f + ": " + file.read())

        context.log_debug("Data path: " + context.get_file_path_data())
        context.log_debug("Cache path: " + context.get_file_path_cache())
        context.log_debug("Out path: " + context.get_file_path_out())

        return OutputExampleStage1()
