from scan_mate.modes.mode_task_register import register_task
from scan_mate.parameters.generator_configs import BarcodeGeneratorConfig
from scan_mate.datasets.dataset_manager import DatasetManager
from scan_mate.datasets.barcode_generator import BarcodeGenerator


@register_task('prepare_data', 'generator')
def prepare_generator(config: BarcodeGeneratorConfig):
    print('Running data generator...')
    db_name = config.db_name
    root_dir = config.root_dir
    barcode_types = config.barcode_types
    barcode_ratio = config.barcode_ratio
    n_data = config.n_data
    if isinstance(n_data, int):
        n_data = [n_data]
    data_manager = DatasetManager(db_name)
    data_manager.create_barcode_db()
    
    modes = ['train', 'valid', 'test']
    for idata, imode in zip(n_data, modes):
        gen = BarcodeGenerator(root_dir, imode, barcode_types, barcode_ratio)
        b_infos = gen.generate_dataset(idata)
        data_manager.add_barcode_data(b_infos, imode)

    msg = 'Generate barcodes successfully.'
    return {'status': 'done', 'message': msg}


@register_task('prepare_data', 'augmenter')
def prepare_augmenter(args, config):
    print('Running data augmentation...')

    return {'status': 'done', 'task': 'augmenter'}


@register_task('prepare_data', 'rotator')
def prepare_rotator(args, config):
    print('Running data rotator...')

    return {'status': 'done', 'task': 'rotator'}


@register_task('prepare_data', 'compositor')
def prepare_compositor(args, config):
    print('Running data composition...')

    return {'status': 'done', 'task': 'compositor'}
