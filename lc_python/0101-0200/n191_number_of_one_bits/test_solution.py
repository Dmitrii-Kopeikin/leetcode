from copy import deepcopy

import pytest

from .solution import Solution


DATASET = [
    (1, 1),
    (13, 3),
    (139, 4),
    (139123, 11),
    (0, 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().hammingWeight(data[0])
    assert result == data[1], result