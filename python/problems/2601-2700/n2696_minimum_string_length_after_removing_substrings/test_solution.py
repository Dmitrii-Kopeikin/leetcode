import pytest

from .solution import Solution

DATASET = [
    ("ABFCACDB", 2),
    ("ACBBD", 5),
    ("A", 1),
    ("ABFCACDB", 2),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().minLength(data[0])
    assert result == data[1], result
    