from dataclasses import dataclass, field, fields
from pathlib import Path

from scan_mate.parameters.base_config import BaseConfig


@dataclass
class InferenceConfig(BaseConfig):
    data: list[str] | int = field(init=False, default_factory=list)

    def set_config_from_dict(self, params: dict):
        valid_fields = {f.name for f in fields(self)}
        for key, value in params.items():
            if key in valid_fields:
                setattr(self, key, value)
            else:
                raise ValueError(f'Unknown config field: {key}')
