from copy import deepcopy

import pytest

from .solution import Solution as Solution


DATASET = [
    ((3, 7), 3),
    ((8, 10), 1),
    ((7, 13), 4),
    ((7, 14), 4),
    ((6, 13), 4),
    ((6, 14), 4),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().countOdds(*data[0])
    assert result == data[1], result
