import pytest

from ..solution import Solution


DATASET = [
    (['a', 'a', 'b', 'b', 'c', 'c', 'c'], 6),
    (['a'], 1),
    (['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 4),
    (['a', 'b', 'c'], 3),
]


@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    result = Solution().compress(data[0])
    assert result == data[1], result
