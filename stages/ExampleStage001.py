import os
import time
from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context


@dataclass
class ExampleStage001Input:
    pass


@dataclass
class ExampleStage001Config:
    test_file_name: str


@dataclass
class ExampleStage001Output:
    test_file_path: str


class ExampleStage001(Stage[ExampleStage001Input, ExampleStage001Config, ExampleStage001Output]):

    @staticmethod
    def _preview(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config):
        context.log_info("Got name '" + conf.test_file_name + "'")

    @staticmethod
    def _get_cached(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config) -> ExampleStage001Output:
        f = context.get_file_path_out(conf.test_file_name)

        if os.path.exists(f):
            return ExampleStage001Output(
                test_file_path=f
            )

    @staticmethod
    def _process(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config) -> ExampleStage001Output:
        f = context.get_file_path_out(conf.test_file_name)

        context.log_info("This is a Test. Write to " + f)

        with open(f, "w") as file:
            file.write("Hello World! " + str(int(time.time())))

        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        return ExampleStage001Output(
            test_file_path=f
        )

    @staticmethod
    def _after_process(context: Context, out: ExampleStage001Output, conf: ExampleStage001Config):
        context.log_info("File written to " + out.test_file_path)
