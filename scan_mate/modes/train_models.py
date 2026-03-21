from scan_mate.modes.mode_task_register import register_task


@register_task('train', 'detector')
def train_detector(args, config):
    print('Training detector model...')
    return {'status': 'done', 'task': 'detector'}


@register_task('train', 'corrector')
def train_corrector(args, config):
    print('Training corrector model...')
    return {'status': 'done', 'task': 'corrector'}
