import os
import time
from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context


@dataclass
class InputExampleStage001:
    pass


@dataclass
class ConfigExampleStage001:
    test_file_name: str


@dataclass
class OutputExampleStage001:
    test_file_path: str


class ExampleStage001(Stage[InputExampleStage001, ConfigExampleStage001, OutputExampleStage001]):

    @staticmethod
    def _preview(context: Context, inp: InputExampleStage001, conf: ConfigExampleStage001):
        context.log_info("Got name '" + conf.test_file_name + "'")

    @staticmethod
    def _get_cached(context: Context, inp: InputExampleStage001, conf: ConfigExampleStage001) -> OutputExampleStage001:
        f = context.get_file_path_out(conf.test_file_name)

        if os.path.exists(f):
            return OutputExampleStage001(
                test_file_path=f
            )

    @staticmethod
    def _process(context: Context, inp: InputExampleStage001, conf: ConfigExampleStage001) -> OutputExampleStage001:
        f = context.get_file_path_out(conf.test_file_name)

        context.log_info("This is a Test. Write to " + f)

        with open(f, "w") as file:
            file.write("Hello World! " + str(int(time.time())))

        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        return OutputExampleStage001(
            test_file_path=f
        )
