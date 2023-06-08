import pytest

from .solution import Solution


DATASET = [
    ((1, 4), 2),
    ((3, 1), 1),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().hammingDistance(*data[0])
    assert result == data[1], result
