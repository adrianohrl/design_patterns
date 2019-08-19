def create(clazz, *args, **kwargs):
    return globals()[clazz](*args, **kwargs)