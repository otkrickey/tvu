import pytest
import numpy as np
from tvu.decimal import DecimalNumber

# case_keys: str
case_keys = [
    '12', '0', '-12',
    '1.2', '0.0', '-1.2',
    'np.int16(12)', 'np.int16(0)', 'np.int16(-12)',
    'np.int32(12)', 'np.int32(0)', 'np.int32(-12)',
    'np.int64(12)', 'np.int64(0)', 'np.int64(-12)']
# case_args: int | float | np.int16 | np.int32 | np.int64
case_args = [
    12, 0, -12,
    1.2, 0.0, -1.2,
    np.int16(12), np.int16(0), np.int16(-12),
    np.int32(12), np.int32(0), np.int32(-12),
    np.int64(12), np.int64(0), np.int64(-12)]
# case_params: (s:int, x:int, e:int)
case_params = [
    (1, 12, 0), (0, 0, 0), (-1, 12, 0),
    (1, 12, -1), (0, 0, 0), (-1, 12, -1),
    (1, 12, 0), (0, 0, 0), (-1, 12, 0),
    (1, 12, 0), (0, 0, 0), (-1, 12, 0),
    (1, 12, 0), (0, 0, 0), (-1, 12, 0),]
# case_div_by_2: int | float | np.int16 | np.int32 | np.int64
case_div_by_2 = [
    6, 0, -6,
    0.6, 0, -0.6,
    np.int16(6), np.int16(0), np.int16(-6),
    np.int32(6), np.int32(0), np.int32(-6),
    np.int64(6), np.int64(0), np.int64(-6)]
# case_repr: str
case_repr = [
    'DecimalNumber(12)', 'DecimalNumber(0)', 'DecimalNumber(-12)',
    'DecimalNumber(12e-1)', 'DecimalNumber(0)', 'DecimalNumber(-12e-1)',
    'DecimalNumber(12)', 'DecimalNumber(0)', 'DecimalNumber(-12)',
    'DecimalNumber(12)', 'DecimalNumber(0)', 'DecimalNumber(-12)',
    'DecimalNumber(12)', 'DecimalNumber(0)', 'DecimalNumber(-12)']


# failed_cases: [key, ix, error]
failed_cases = [
    # ('"1.2"', "1.2", TypeError), # Added support for str in DecimalNumber.__init__
    ('1.2j', 1.2j, TypeError),
    ('[1.2]', [1.2], TypeError),
    ('(1.2,)', (1.2,), TypeError),
    ('{1.2}', {1.2}, TypeError),
    ('{1.2: 1.2}', {1.2: 1.2}, TypeError),
    ('np.array([1.2])', np.array([1.2]), TypeError),
    ('np.float64(1.2)', np.float64(1.2), TypeError),
]


def test_decimal_number___init__():
    for key, arg, (s, x, e) in zip(case_keys, case_args, case_params):
        _1 = DecimalNumber(arg)
        assert _1.s == s
        assert _1.x == x
        assert _1.e == e


def test_decimal_number___init__raises_TypeError():
    for key, ix, error in failed_cases:
        with pytest.raises(error):
            DecimalNumber(ix)


def test_decimal_number___repr__():
    for key, arg, _repr_ in zip(case_keys, case_args, case_repr):
        _1 = DecimalNumber(arg)
        assert repr(_1) == _repr_


def test_decimal_number___str__():
    for key, arg, (s, x, e) in zip(case_keys, case_args, case_params):
        _1 = DecimalNumber(arg)
        assert str(_1) == f"{x}e{e}"


def test_decimal_number___eq__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(args)
        assert _1 == _2


def test_decimal_number___ne__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(args + 1)
        assert _1 != _2


def test_decimal_number___lt__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(args + 1)
        assert _1 < _2


def test_decimal_number___le__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(args)
        _3 = DecimalNumber(args + 1)
        assert _1 <= _2
        assert _1 <= _3


def test_decimal_number___gt__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args + 1)
        _2 = DecimalNumber(args)
        assert _1 > _2


def test_decimal_number___ge__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(args)
        _3 = DecimalNumber(args - 1)
        assert _1 >= _2
        assert _1 >= _3


def test_decimal_number___abs__():
    for key, args in zip(case_keys, case_args):
        _1 = DecimalNumber(args)
        _2 = DecimalNumber(-args)
        assert abs(_1) == abs(_2)


def test_decimal_number___add__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(arg)
        _3 = DecimalNumber(arg + arg)
        assert _1 + _2 == _3


def test_decimal_number___sub__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(arg)
        _3 = DecimalNumber(arg - arg)
        assert _1 - _2 == _3


def test_decimal_number___mul__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(arg)
        _3 = DecimalNumber(arg * arg)
        assert _1 * _2 == _3


def test_decimal_number___truediv__():
    for key, arg, d in zip(case_keys, case_args, case_div_by_2):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(2)
        _3 = DecimalNumber(d)
        assert _1 / _2 == _3


def test_decimal_number___floordiv__():
    for key, arg, d in zip(case_keys, case_args, case_div_by_2):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(2)
        _3 = DecimalNumber(d)
        assert _1 // _2 == _3


def test_decimal_number___mod__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(2)
        _3 = DecimalNumber(0)
        assert _1 % _2 == _3


def test_decimal_number___pow__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(arg)
        _2 = DecimalNumber(2)
        _3 = DecimalNumber(arg ** 2)
        assert _1 ** _2 == _3


def test_decimal_number___int__():
    for key, arg in zip(case_keys, case_args):
        _1 = DecimalNumber(int(arg))
        assert int(_1) == int(arg)
