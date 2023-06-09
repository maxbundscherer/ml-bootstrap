from typing import TypeVar, Generic

from framework.Context import Context, PathConfig
from framework.Environment import Environment

T_INPUT = TypeVar('T_INPUT')
T_CONFIG = TypeVar('T_CONFIG')
T_OUTPUT = TypeVar('T_OUTPUT')


class Stage(Generic[T_INPUT, T_CONFIG, T_OUTPUT]):
    """
    A Stage is a single step in a pipeline.
    It has an input (T_INPUT), a configuration (T_CONFIG) and an output (T_OUTPUT).
    Implement _preview() to do a preview of the stage.
    Implement _get_cached() to get the output from the cache. Please use CacheHelper from framework.
    Implement _process() to do the actual work.
    Implement _write_cache() to write the output to the cache. Please use CacheHelper from framework.
    Implement _after_process() to do something after the processing.
    Please see stages/ExampleStage001.py for an example.
    """

    @staticmethod
    def _preview(context: Context,
                 inp: T_INPUT,
                 conf: T_CONFIG) -> None:
        """
        Method does not return anything.
        """
        pass

    @staticmethod
    def _get_cached(context: Context,
                    inp: T_INPUT,
                    conf: T_CONFIG) -> T_OUTPUT:
        """
        Method return None if no cache is available.
        Implement get cache logic here (please use CacheHelper from framework).
        """
        pass

    @staticmethod
    def _process(context: Context,
                 inp: T_INPUT,
                 conf: T_CONFIG) -> T_OUTPUT:
        """
        Implement stage logic here.
        """
        raise NotImplementedError()

    @staticmethod
    def _write_cache(context: Context,
                     out: T_OUTPUT,
                     conf: T_CONFIG) -> None:
        """
        Implement write cache logic here (please use CacheHelper from framework).
        """
        pass

    @staticmethod
    def _after_process(context: Context,
                       out: T_OUTPUT,
                       conf: T_CONFIG) -> None:
        """
        Implement after process logic here.
        Method is called after _process() or _get_cached().
        """
        pass

    def __init__(self,
                 env: Environment,
                 inp: T_INPUT,
                 stage_config: T_CONFIG,
                 stage_title: str = "Preload Data",
                 stage_id: str = "001_preload",
                 flush_cache_dir=False,
                 flush_out_dir=False,
                 ignore_cache: bool = False
                 ):

        # Check stage_id and stage_title

        if stage_title == "":
            raise ValueError("Stage title must not be empty")

        if " " in stage_id or "/" in stage_id or "-" in stage_id:
            raise ValueError("Stage ID must not contain spaces, slashes or dashes")

        # Paths

        path_config = PathConfig(
            file_path_data=env.get_context().get_file_path_data(),
            file_path_out=env.get_context().get_file_path_out(stage_id + "/"),
            file_path_cache=env.get_context().get_file_path_cache(stage_id + "/"),
            flush_cache_dir=flush_cache_dir,
            flush_out_dir=flush_out_dir,
            create_dir_on_demand=True
        )

        # Context

        context = Context(
            path_config=path_config,
            logging_prefix="St-" + stage_id,
            logging_config=env.get_logging_config()
        )

        # Set attributes

        self._inp: T_INPUT = inp
        self._stage_title: str = stage_title
        self._stage_id: str = stage_id
        self._context: Context = context
        self._conf: T_CONFIG = stage_config
        self._ignore_cache: bool = ignore_cache

        env.register_context(context)

    def preview(self):
        self._context.log_space()

        self._context.log_info("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
        self._context.log_info("[Started Preview Stage '" + self._stage_title + "']")
        # self._context.log_info("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
        self._context.stopwatch_start("StPrev-" + self._stage_id)

        self._preview(
            context=self._context,
            inp=self._inp,
            conf=self._conf
        )
        o = self._context.stopwatch_stop("StPrev-" + self._stage_id)
        # self._context.log_info("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
        self._context.log_info("[Stopped Preview Stage '" + self._stage_title + "' (" + o + ")]")
        self._context.log_info("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

    def process(self) -> T_OUTPUT:
        self._context.log_space()

        self._context.log_info("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
        self._context.log_info("[Started Stage '" + self._stage_title + "']")
        # self._context.log_info("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
        self._context.stopwatch_start("St-" + self._stage_id)

        out: T_OUTPUT = None

        if not self._ignore_cache:
            out: T_OUTPUT = self._get_cached(
                context=self._context,
                inp=self._inp,
                conf=self._conf
            )
        else:
            self._context.log_debug("[Cache ignored]")

        if out is None:
            # Cache miss
            out = self._process(
                context=self._context,
                inp=self._inp,
                conf=self._conf
            )
            self._write_cache(
                context=self._context,
                out=out,
                conf=self._conf
            )
        else:
            # Cache hit
            self._context.log_debug("[Cached]")

        self._after_process(
            context=self._context,
            out=out,
            conf=self._conf
        )

        o = self._context.stopwatch_stop("St-" + self._stage_id)
        # self._context.log_info("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")
        self._context.log_info("[Stopped Stage '" + self._stage_title + "' (" + o + ")]")
        self._context.log_info("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫")

        return out
