import pytest

from ..solution import Solution


DATASET = [
    ([3, 6, 9, 12],  4),
    ([9, 4, 7, 2, 10], 3),
    ([20, 1, 15, 3, 10, 5, 8], 4),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().longestArithSeqLength(data[0])
    assert result == data[1], result
