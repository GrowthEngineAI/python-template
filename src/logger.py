# Imports

import threading
import os
import sys
import logging
from typing import Optional
from rich.console import Console
from rich.logging import RichHandler

_lock = threading.Lock()
_lib_logger_handler: Optional[logging.Handler] = None

console = Console(file=sys.stdout)
fmt = "[%(name)s] %(funcName)-5s %(message)s"
logging.basicConfig(
    level="INFO", format=fmt, datefmt="[%X]", handlers=[RichHandler(console=console, show_level=True, show_path=True)]
)

class LibLogger:
    def __init__(self, config):
        self.config = config
        self.logger = self.setup_logging()
    
    def setup_logging(self):
        logger = logging.getLogger(self.config['name'])
        logger.setLevel(logging.INFO)
        if os.environ.get('IGNORE_LOGGERS', None):
            ignore_loggers = os.environ['IGNORE_LOGGERS'].split(',')
            for lgr_name in ignore_loggers:
                lgr = logging.getLogger(lgr_name)
                lgr.handlers = [h for h in lgr.handlers if not isinstance(h, logging.StreamHandler)]
        gdisclgr = logging.getLogger('googleapiclient')
        if gdisclgr:
            gdisclgr.setLevel(logging.ERROR)
        return logger

    def get_logger(self):
        return self.logger
    

def _setup_library_root_logger(name):
    logger_config = {
        'name': name,
    }
    logger = LibLogger(logger_config)
    return logger.get_logger()


def _configure_library_root_logger(name):
    global _lib_logger_handler
    with _lock:
        if _lib_logger_handler:
            return
        _lib_logger_handler = _setup_library_root_logger(name)
        _lib_logger_handler.propagate = True


def get_logger(name=None):
    if name is None:
        from . import _LIB_NAME
        name = _LIB_NAME
    _configure_library_root_logger(name)
    return _lib_logger_handler

