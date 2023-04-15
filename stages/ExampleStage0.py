import time
from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context


@dataclass
class InputExampleStage0:
    pass


@dataclass
class ConfigExampleStage0:
    test_file_name: str


@dataclass
class OutputExampleStage0:
    test_file_path: str


class ExampleStage0(Stage[InputExampleStage0, ConfigExampleStage0, OutputExampleStage0]):

    @staticmethod
    def _preview(context: Context, inp: InputExampleStage0, conf: ConfigExampleStage0):
        pass

    @staticmethod
    def _get_cached(context: Context, inp: InputExampleStage0, conf: ConfigExampleStage0) -> OutputExampleStage0:
        pass

    @staticmethod
    def _process(context: Context, inp: InputExampleStage0, conf: ConfigExampleStage0) -> OutputExampleStage0:
        f = context.get_file_path_out(conf.test_file_name)

        context.log_info("This is a Test. Write to " + f)

        with open(f, "w") as file:
            file.write("Hello World! " + str(int(time.time())))

        context.log_debug("Data path: " + context.get_file_path_data())
        context.log_debug("Cache path: " + context.get_file_path_cache())
        context.log_debug("Out path: " + context.get_file_path_out())

        return OutputExampleStage0(
            test_file_path=f
        )
