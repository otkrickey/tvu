import math
import numpy as np
from ..decimal_value import Dn


class TypicalValueWithUncertainty:
    """TypicalValueWithUncertainty is a class that represents a typical value with uncertainty.

    Attributes
    ----------
    t : DecimalNumber
        The typical value.
    u : DecimalNumber
        The uncertainty.

    Properties
    ----------
    e : int
        The exponent of the typical value.

    """
    t: Dn
    u: Dn

    @property
    def T(self) -> int | float | np.integer: return self.t.X

    @property
    def U(self) -> int | float | np.integer: return self.u.X

    def __init__(self, *args):
        if len(args) == 1:
            arg1 = args[0]
            if isinstance(arg1, Dn):
                self.t = arg1
                self.u = Dn(0)
            elif isinstance(arg1, TypicalValueWithUncertainty):
                self.t = arg1.t
                self.u = arg1.u
            elif not isinstance(arg1, np.floating) and isinstance(arg1, int | float | np.integer):
                self.t = Dn(arg1)
                self.u = Dn(0)
            elif isinstance(arg1, np.ndarray) and arg1.ndim == 1:
                self.t = Dn(np.average(arg1))
                self.u = Dn(np.std(arg1, ddof=1) / math.sqrt(len(arg1)))
            else:
                raise TypeError(f'Unsupported type: {type(arg1)}')
        elif len(args) == 2:
            arg1, arg2 = args
            if isinstance(arg1, Dn):
                self.t = arg1
            elif not isinstance(arg1, np.floating) and isinstance(arg1, int | float | np.integer):
                self.t = Dn(arg1)
            else:
                raise TypeError(f'Unsupported type: {type(arg1)}')
            if isinstance(arg2, Dn):
                self.u = arg2
            elif not isinstance(arg2, np.floating) and isinstance(arg2, int | float | np.integer):
                self.u = Dn(arg2)
            else:
                raise TypeError(f'Unsupported type: {type(arg2)}')
        else:
            raise TypeError(f'Unsupported number of arguments: {len(args)}')
