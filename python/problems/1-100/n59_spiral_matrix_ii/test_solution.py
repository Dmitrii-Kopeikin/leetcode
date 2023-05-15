import pytest

from .solution import Solution


DATASET = [
    (3, [[1,2,3],[8,9,4],[7,6,5]]),
    (1, [[1]]),
]



@pytest.mark.parametrize('data', DATASET)
def test_solution(data):
    nums = Solution().generateMatrix(data[0])
    assert nums == data[1], nums
