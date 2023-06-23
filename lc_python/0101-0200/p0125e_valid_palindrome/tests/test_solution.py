import pytest

from ..solution import Solution


DATASET = [
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
    (' ', True),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().isPalindrome(data[0])
    assert result == data[1], result
