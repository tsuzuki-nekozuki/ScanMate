import importlib
import pkgutil

import modes
from modes.mode_task_register import get_task
from parameters.base_config import BaseConfig


def import_all_modes():
    for module_info in pkgutil.iter_modules(modes.__path__):
        importlib.import_module(f'modes.{module_info.name}')


class ScanMateController:
    def __init__(self):
        self.mode: str = None
        self.task: str = None

    def run(self, mode: str, task: str, params: BaseConfig):
        self.mode = mode
        self.task = task

        import_all_modes()
        proceed_task = get_task(self.mode, self.task)

        proceed_task(params)
