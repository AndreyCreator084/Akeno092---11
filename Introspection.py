
def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    info['module'] = type(obj).__module__
    if isinstance(obj, str):
        info['length'] = len(obj)
    return info


string_info = introspection_info('123')
print(string_info)
int_info = introspection_info(123)
print(int_info)
list_info = introspection_info([1, 2, 3])
print(list_info)
dict_info = introspection_info({'a': 1, 'b': 2, 'c': 3})
print(dict_info)
