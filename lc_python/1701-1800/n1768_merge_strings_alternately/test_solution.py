import pytest

from .solution import Solution


DATASET = [
    (("abc", "pqr"), "apbqcr"),
    (("ab", "pqrs"), "apbqrs"),
    (("abcd", "pq"), "apbqcd"),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().mergeAlternately(*data[0])
    assert result == data[1], result
