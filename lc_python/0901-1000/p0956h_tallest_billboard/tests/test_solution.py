import pytest

from ..solution import Solution


DATASET = [
    ([1, 2, 3, 6], 6),
    ([1, 2, 3, 4, 5, 6], 10),
    ([1, 2], 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().tallestBillboard(data[0])
    assert result == data[1], result
