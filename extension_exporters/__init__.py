import glob
import importlib
import os.path

files = [
    os.path.basename(f)[:-3]
    for f in glob.glob(os.path.dirname(__file__) + '/*.py')
    if os.path.isfile(f)
]
modules = [f for f in files if not f.startswith('_')]

__all__  = []
for module in modules:
    module = importlib.import_module('.'+module, __name__)
    for attr in [getattr(module, attr) for attr in dir(module)]:
        if hasattr(attr, 'ext_meta'):
            __all__.append(attr)