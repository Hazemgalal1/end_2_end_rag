from regex import match
def import_module(module_name):
    if match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', module_name):
        return __import__(module_name)
    else:
        raise ImportError(f"Invalid module name: {module_name}")
