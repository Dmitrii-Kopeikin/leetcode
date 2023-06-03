import pytest

from .solution import Solution


DATASET = [
    ((2, [[1, 2]]), 2),
    ((3, [[1, 3], [2, 3]]), 3),
    ((3, [[1, 3], [2, 3], [3, 1]]), -1),
    ((4, [[1,3],[1,4],[2,3],[2,4],[4,3]]), 3),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().findJudge(*data[0])
    assert result == data[1], result
