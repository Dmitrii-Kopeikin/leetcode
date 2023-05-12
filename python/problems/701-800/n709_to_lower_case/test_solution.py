import pytest

from .solution import Solution


DATASET = [
    ("Hello", "hello"),
    ("LOVELY", "lovely"),
    ("here", "here"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().toLowerCase(data[0])
    assert result == data[1], result
