from scan_mate.modes.mode_task_register import register_task
from scan_mate.parameters.inference_configs import InferenceConfig
from scan_mate.utils.barcode_decoder import BarcodeDecoder


@register_task('infer', 'picture')
def picture(config: InferenceConfig):
    print('Running picture inference...')
    for i in config.data:
        decoder = BarcodeDecoder(i)
        print(decoder.read_barcodes())
    msg = 'Infer images.'
    return {'status': 'done', 'message': msg}
