# tbd

tbd tbd tbd tbd tbd tbd tbd tbd tbd

``tbd - tbd``

[![shields.io](https://img.shields.io/badge/license-Apache2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.txt)

Maintainer: [Maximilian Bundscherer](https://bundscherer-online.de)

## Overview

tbd tbd tbd

## Let's get started

### Install (with Conda)

- `conda create --name py311tbd python=3.11`
- `conda activate py311tbd`
- `pip install -r requirements.txt` (install requirements)
- `pip freeze > requirements.txt` (export requirements)

### Run

- `python main_example.py`

### Own project

- Add `main.py` to your project (use `main_example.py` as template)
- Add Stages to `stages/` (see Stages in `stages/` and see [doc](framework/Stage.py))
- Run `python main.py`

## TODOS

- [ ] Add `git@github.com:maxbundscherer/ml-bootstrap.git` to git-remotes (get updates from bootstrap)
- [ ] tbd
- [ ] tbd
- [ ] tbd

## Framework documentation

### Logging

- Use `context.log_*()` instead of `print` to log messages
- Use `context.log_space()` to log a new line

### Paths

- Use `context.get_file_path_data()` to get the path to the data directory (input data)
- Use `context.get_file_path_cache()` to get the path to the cache directory (for framework!)
- Use `context.get_file_path_out()` to get the path to the output directory (for humans!)

### Utils

- Use `context.start_stopwatch()` and `context.stop_stopwatch()` to measure time
- Use `context.summary_add(*)` to add a summary entry (logged at the end of the environment)
