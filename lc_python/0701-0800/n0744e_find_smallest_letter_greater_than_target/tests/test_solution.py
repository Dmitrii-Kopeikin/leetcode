import pytest

from ..solution import Solution


DATASET = [
    ((["x","x","y","y"], 'z'), 'x'),
    ((["c","f","j"], 'c'), 'f'),
    ((["c","f","j"], 'a'), 'c'),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().nextGreatestLetter(*data[0])
    assert result == data[1], result
