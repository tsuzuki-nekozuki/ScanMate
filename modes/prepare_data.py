from modes.mode_task_register import register_task


@register_task('prepare_data', 'generator')
def prepare_generator(args, config):
    print('Running data generator...')

    return {'status': 'done', 'task': 'generator'}


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
