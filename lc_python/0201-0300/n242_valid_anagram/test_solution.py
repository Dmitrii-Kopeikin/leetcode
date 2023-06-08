import pytest

from .solution import Solution


DATASET = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isAnagram(*data[0])
    assert result == data[1], result
