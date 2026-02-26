from dataclasses import dataclass, field, fields

from parameters.base_config import BaseConfig


@dataclass(slots=True)
class BarcodeGeneratorConfig(BaseConfig):
    db_name: str = field(init=False, default='data/data.db')
    img_dir: str = field(init=False, default='data/barcodes')
    n_data: int = field(init=False, default=100)

    def set_config_from_dict(self, dict_params: dict):
        valid_fields = {f.name for f in fields(self)}
        for key, value in dict_params.items():
            if key in valid_fields:
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown config field: {key}")
