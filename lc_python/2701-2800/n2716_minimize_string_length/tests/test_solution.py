import pytest

from ..solution import Solution

DATASET = [
    ("dddaaa", 2),
    ("cbbd", 3),
    ("aaabc", 3),
    ("abbbcccdddbbb", 4),
    ("", 0),
    ("a", 1),
    ("ipi", 2),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().minimizedStringLength(data[0])
    assert result == data[1], result
    