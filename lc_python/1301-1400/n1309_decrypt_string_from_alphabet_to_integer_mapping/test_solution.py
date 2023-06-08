import pytest

from .solution import Solution


DATASET = [
    ("10#11#12", "jkab"),
    ("1326#", "acz"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().freqAlphabets(data[0])
    assert result == data[1], result
