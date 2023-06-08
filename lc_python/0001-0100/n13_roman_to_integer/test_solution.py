from copy import deepcopy

import pytest

from .solution import Solution


DATASET = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().romanToInt(data[0])
    assert result == data[1], result
