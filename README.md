# ml-bootstrap

A simple ml/data-science python framework.

``machine learning - data science - python - framework``

[![shields.io](https://img.shields.io/badge/license-Apache2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.txt)

Maintainer: [Maximilian Bundscherer](https://bundscherer-online.de)

## Overview

This repo is helping me to structure my machine learning projects in an efficient way.

## Let's get started

### Install (with Conda) and first run

- `conda create --name py311tbd python=3.11`
- `conda activate py311tbd`
- `pip install -r requirements.txt` (install requirements)
- `pip freeze > requirements.txt` (export requirements)
- `python main_example.py`

### Add your own project

- Read doc below
- Add `main.py` to your project (use `main_example.py` as template)
- Add Stages to `stages/` (read [Stage Documentation](framework/Stage.py) and see [ExampleStages](stages/))
- Run `python main.py`
- (Optional) See [workflows](.github/workflows) (trigger GitHub actions) and [tests](tests/)

## Framework documentation

- Add `git@github.com:maxbundscherer/ml-bootstrap.git` to git-remotes (get updates from bootstrap repo)
- Read [Stage Documentation](framework/Stage.py) and see [ExampleStages](stages/)

### Logging

- Use `context.log_*()` instead of `print` to log messages
- Use `context.log_space()` to log a new line

### Paths

- Use `context.get_file_path_data()` to get the path to the data directory (input data)
- Use `context.get_file_path_cache()` to get the path to the cache directory (**for framework!**)
- Use `context.get_file_path_out()` to get the path to the output directory (**for humans!**)
- Use `context.list_files_*()` to list all files in the * directory

### Utils

- Use `context.start_stopwatch()` and `context.stop_stopwatch()` to measure time
- Use `context.summary_add(*)` to add a summary entry (logged at the end of the environment)
    - Use `SummaryText` to add a text entry (logs text at the end)
    - Use `SummaryAccuracy` to add an accuracy entry (sorts and logs accuracy at the end)

### Cache Helper

- There are different cache helpers (see [CacheHelper](framework/CacheHelper.py)) included
    - Use `PandasCacheHelper` for pandas dataframes
    - Use `FileCacheHelper` for files (there is a method `check_if_all_file_exists_*(...)` to check if all files exists
      in * directory instead of reading them)