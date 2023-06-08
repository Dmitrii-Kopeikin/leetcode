import pytest

from ..solution import Solution


DATASET = [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().deleteAndEarn(data[0])
    assert result == data[1], result
