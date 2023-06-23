import pytest

from ..solution import Solution


DATASET = [
    (['flower','flow','flight'], 'fl'),
    (['dog','racecar','car'], ''),
    (['cir', 'car'], 'c'),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().longestCommonPrefix(data[0])
    assert result == data[1], result
