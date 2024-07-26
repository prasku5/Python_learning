from .arithmetic import add, subtract
from .geometry import area_of_circle, perimeter_of_square

__all__ = ["add", "subtract", "area_of_circle", "perimeter_of_square"]

# The __all__ variable is a list of strings that specifies the names of 
# the modules that should be imported when using the from ... import * syntax.

# The __all__ variable is optional. If it is not present, all public names
# (those not starting with an underscore) will be imported. If it is present,
# only the names in the list will be imported.

# It is different than from module import * because it only imports the names
# specified in the __all__ list. This is useful for limiting the number of
# names imported from a module. 

# We can avoid writing from statement multiple times by using __all__ variable.