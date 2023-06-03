import pytest

from .solution import Solution


DATASET = [
    ((10, 1, 10), 1.0),
    ((6, 1, 10), 0.6),
    ((21, 17, 10), 0.73278),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().new21Game(*data[0])
    assert round(result, 5) == round(data[1], 5), result
