from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseConfig(ABC):
    pass

    @abstractmethod
    def set_config_from_dict(self, dict_params: dict):
        raise NotImplementedError('Define set_config_from_dict().')
