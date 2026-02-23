from dataclasses import dataclass, field


@dataclass(slots=True)
class barcode_generator_params:
    db_name: str = field(init=True, default='data/data.db')
    img_dir: str = field(init=True, default='data/barcodes')
    n_data: int = field(init=True, default=100)
