from dataclasses import dataclass, field, fields

from scan_mate.parameters.base_config import BaseConfig


@dataclass
class BarcodeGeneratorConfig(BaseConfig):
    db_name: str = field(init=False, default='data/data.db')
    root_dir: str = field(init=False, default='data')
    barcode_types: list[str] | None = field(init=False, default=None)
    barcode_ratio: list[float] | None = field(init=False, default=None)
    n_data: list[int] | int = field(init=False, default_factory=lambda: [60, 20, 20])

    def set_config_from_dict(self, params: dict):
        valid_fields = {f.name for f in fields(self)}
        for key, value in params.items():
            if key in valid_fields:
                setattr(self, key, value)
            else:
                raise ValueError(f"Unknown config field: {key}")
