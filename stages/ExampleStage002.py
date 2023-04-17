from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context
from stages.ExampleStage001 import OutputExampleStage001


@dataclass
class InputExampleStage002:
    stage_001_out: OutputExampleStage001


@dataclass
class ConfigExampleStage002:
    pass


@dataclass
class OutputExampleStage002:
    pass


class ExampleStage002(Stage[InputExampleStage002, ConfigExampleStage002, OutputExampleStage002]):

    @staticmethod
    def _preview(context: Context, inp: InputExampleStage002, conf: ConfigExampleStage002):
        pass

    @staticmethod
    def _get_cached(context: Context, inp: InputExampleStage002, conf: ConfigExampleStage002) -> OutputExampleStage002:
        pass

    @staticmethod
    def _process(context: Context, inp: InputExampleStage002, conf: ConfigExampleStage002) -> OutputExampleStage002:
        f = inp.stage_001_out.test_file_path

        with open(f, "r") as file:
            context.log_info("This is a Test Read from " + f + ": " + file.read())

        context.log_debug("Debug message 123")
        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        return OutputExampleStage002()
