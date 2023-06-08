import pytest

from .solution import Solution


DATASET = [
    ([1,2], 1),
    ([3,4,6,8], 11),
    ([1,2,3,4,5,6], 14),
    ([415,230,471,705,902,87], 23),
    ([9,17,16,15,18,13,18,20], 91),
    ([773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730], 3032),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxScore(data[0])
    assert result == data[1], result
