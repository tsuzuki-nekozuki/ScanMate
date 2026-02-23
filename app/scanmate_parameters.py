import yaml


class ScanMateParameters:
    def __init__(self):
        self.params_dict: dict = None

    def read_config(self, config_path: str, mode: str = None,
                    task: str = None) -> None | dict:
        with open(config_path, mode='r', encoding='utf-8') as f:
            self.params_dict = yaml.safe_load(f)
        if mode is not None and task is not None:
            try:
                return self.params_dict[mode][task]
            except KeyError:
                return None
        else:
            return None
