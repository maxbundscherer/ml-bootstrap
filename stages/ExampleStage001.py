from dataclasses import dataclass

from framework.CacheHelper import FileCacheHelper
from framework.Stage import Stage
from framework.Context import Context, SummaryText


@dataclass
class ExampleStage001Input:
    test_message: str


@dataclass
class ExampleStage001Config:
    test_message_suffix: str


@dataclass
class ExampleStage001Output:
    message: str


class ExampleStage001(Stage[ExampleStage001Input, ExampleStage001Config, ExampleStage001Output]):

    @staticmethod
    def _preview(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config) -> None:
        context.log_debug("Should append '" + inp.test_message + "' with '" + conf.test_message_suffix + "'")

    @staticmethod
    def _get_cached(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config) -> ExampleStage001Output:
        content: str = FileCacheHelper(context=context, file_name="testfile.txt").read_cache()

        if content is not None:
            return ExampleStage001Output(
                message=content
            )

    @staticmethod
    def _process(context: Context, inp: ExampleStage001Input, conf: ExampleStage001Config) -> ExampleStage001Output:
        content: str = inp.test_message + conf.test_message_suffix

        context.log_debug("My content is '" + content + "'")

        # context.log_debug("Data path: " + context.get_file_path_data())
        # context.log_debug("Cache path: " + context.get_file_path_cache())
        # context.log_debug("Out path: " + context.get_file_path_out())

        return ExampleStage001Output(
            message=content
        )

    @staticmethod
    def _write_cache(context: Context, out: ExampleStage001Output, conf: ExampleStage001Config) -> None:
        FileCacheHelper(context=context, file_name="testfile.txt").write_cache(out.message)

    @staticmethod
    def _after_process(context: Context, out: ExampleStage001Output, conf: ExampleStage001Config) -> None:
        context.log_debug("Got content '" + out.message + "'")
        context.summary_add(SummaryText(message="My content is '" + out.message + "'"))
