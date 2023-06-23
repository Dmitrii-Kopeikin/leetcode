import pytest

from ..solution import Solution


DATASET = [
    (('sadbutsad', 'sad'), 0),
    (('sodbutsad', 'sad'), 6),
    (('leetcode', 'leeto'), -1),
    (('a', 'a'), 0),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().strStr(*data[0])
    assert result == data[1], result
