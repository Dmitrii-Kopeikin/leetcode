from copy import deepcopy

import pytest

from .solution import Solution


DATASET = [
    ([4000,3000,1000,2000], 2500.0),
    ([1000,2000,3000], 2000.0),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().average(data[0])
    assert result == data[1], result