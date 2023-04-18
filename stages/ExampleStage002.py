from dataclasses import dataclass

from framework.Stage import Stage
from framework.Context import Context, SummaryText
from stages.ExampleStage001 import ExampleStage001Output


@dataclass
class ExampleStage002Input:
    stage_001_out: ExampleStage001Output


@dataclass
class ExampleStage002Config:
    pass


@dataclass
class ExampleStage002Output:
    test_message: str


class ExampleStage002(Stage[ExampleStage002Input, ExampleStage002Config, ExampleStage002Output]):

    @staticmethod
    def _process(context: Context, inp: ExampleStage002Input, conf: ExampleStage002Config) -> ExampleStage002Output:
        content = inp.stage_001_out.message

        context.log_debug("Got message '" + content + "'")
        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        content = content + "!"

        return ExampleStage002Output(test_message=content)

    @staticmethod
    def _after_process(context: Context, out: ExampleStage002Output, conf: ExampleStage002Config) -> None:
        context.log_debug("Got final message '" + out.test_message + "'")
        context.summary_add(SummaryText(message="My content is '" + out.test_message + "'"))
