try:
    from .production import *
except:
    pass

try:
    from .local import *
except:
    pass