TASK_REGISTRY = {}


def register_task(mode, task):
    def decorator(func):
        TASK_REGISTRY[(mode, task)] = func
        return func
    return decorator


def get_task(mode, task):
    key = (mode, task)
    if key not in TASK_REGISTRY:
        raise ValueError(f'Unknown combination: {mode}/{task}')
    return TASK_REGISTRY[key]
