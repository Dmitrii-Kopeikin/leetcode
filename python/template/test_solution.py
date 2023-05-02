import pytest

from .solution import Solution


DATASET = [
    (None, None),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().some_method(data[0])
    assert result == data[1], result
