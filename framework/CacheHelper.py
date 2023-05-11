import os
from typing import TypeVar, Generic

import pandas as pd

from framework.Context import Context

T_OUTPUT = TypeVar('T_OUTPUT')


class CacheHelperInterface(Generic[T_OUTPUT]):

    def __init__(self, context: Context, file_name: str):
        self._context = context
        self._file_name = file_name

    def _is_cached(self) -> bool:
        return os.path.exists(self._context.get_file_path_cache(self._file_name))

    def write_cache(self, o: T_OUTPUT) -> None:
        raise NotImplementedError()

    def read_cache(self) -> T_OUTPUT | None:
        raise NotImplementedError()


class PandasCacheHelper(CacheHelperInterface[pd.DataFrame]):

    def write_cache(self, df: pd.DataFrame) -> None:
        df.to_pickle(self._context.get_file_path_cache(self._file_name))

    def read_cache(self) -> pd.DataFrame | None:
        if self._is_cached():
            return pd.read_pickle(self._context.get_file_path_cache(self._file_name))
        else:
            return None


class FileCacheHelper(CacheHelperInterface[str]):

    def write_cache(self, o: str) -> None:
        with open(self._context.get_file_path_cache(self._file_name), "w") as file:
            file.write(o)

    def read_cache(self) -> str | None:
        if self._is_cached():
            with open(self._context.get_file_path_cache(self._file_name), "r") as file:
                m = file.read()
            return m
        else:
            return None

    @staticmethod
    def check_if_all_file_exists(context: Context, file_names: [str]) -> bool:

        for file_name in file_names:
            if not os.path.exists(context.get_file_path_cache(file_name)):
                return False

        return True
