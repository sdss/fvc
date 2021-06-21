# encoding: utf-8
# isort: skip_file

import logging

from sdsstools import get_config, get_logger, get_package_version


NAME = "fvc"

__version__ = get_package_version(path=__file__, package_name=NAME)


config = get_config(NAME)
log = get_logger(NAME, log_level=logging.WARNING)
