from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context
from stages.ExampleStage001 import ExampleStage001Output


@dataclass
class ExampleStage002Input:
    stage_001_out: ExampleStage001Output


@dataclass
class ExampleStage002Config:
    pass


@dataclass
class ExampleStage002Output:
    pass


class ExampleStage002(Stage[ExampleStage002Input, ExampleStage002Config, ExampleStage002Output]):

    @staticmethod
    def _preview(context: Context, inp: ExampleStage002Input, conf: ExampleStage002Config):
        pass

    @staticmethod
    def _get_cached(context: Context, inp: ExampleStage002Input, conf: ExampleStage002Config) -> ExampleStage002Output:
        pass

    @staticmethod
    def _process(context: Context, inp: ExampleStage002Input, conf: ExampleStage002Config) -> ExampleStage002Output:
        f = inp.stage_001_out.test_file_path

        with open(f, "r") as file:
            context.log_info("This is a Test Read from " + f + ": " + file.read())

        context.log_debug("Debug message 123")
        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        return ExampleStage002Output()

    @staticmethod
    def _after_process(context: Context, out: ExampleStage001Output, conf: ExampleStage002Config):
        context.log_info("Done")
