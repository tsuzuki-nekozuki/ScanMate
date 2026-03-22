import yaml

from scan_mate.parameters.generator_configs import BarcodeGeneratorConfig
from scan_mate.parameters.inference_configs import InferenceConfig


class ScanMateParameters:
    def __init__(self):
        self.params_dict: dict = None

    def read_config(self, config_path: str, mode: str = None,
                    task: str = None) -> None | dict:
        with open(config_path, mode='r', encoding='utf-8') as f:
            self.params_dict = yaml.safe_load(f)
        task_params = self.params_dict.get(mode, {}).get(task)
        if mode is None or task is None or task_params is None:
            return None

        cfg = None
        match (mode, task):
            case ('prepare_data', 'generator'):
                cfg = BarcodeGeneratorConfig()
            case ('infer', 'picture'):
                cfg = InferenceConfig()

        cfg.set_config_from_dict(task_params)
        return cfg
