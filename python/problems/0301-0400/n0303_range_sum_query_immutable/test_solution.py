import pytest

from .solution import NumArray


DATASET = [
    ([-2, 0, 3, -5, 2, -1], [[0, 2], [2, 5], [0, 5]], [1, -1, -3]),
]


@pytest.mark.parametrize("data", DATASET)
def test_num_array(data):
    num_array = NumArray(data[0])
    result = []
    for [i, j] in data[1]:
        result.append(num_array.sumRange(i, j))
    
    assert result == data[2], result
