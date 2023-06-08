import pytest

from .solution import Solution


DATASET = [
    (([1,1,1,2,2,3], 2), [1, 2]),
    (([1], 1), [1]),
    (([1,1,1,2,2,2,3,3,3,4,4,5,5,5,7,7,7], 3), [1, 2, 3]),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().topKFrequent(*data[0])
    assert result == data[1], result
