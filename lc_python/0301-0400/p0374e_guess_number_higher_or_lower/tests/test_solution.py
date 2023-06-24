import pytest
from pytest_mock import mocker

from ..solution import Solution


DATASET = [
    (10, 6),
    (1, 1),
    (2, 1),
]

def get_guess_func(picked_num: int):
    def guess(num: int) -> int:
        if num == picked_num:
            return 0
        elif num < picked_num:
            return 1
        else:
            return -1
    return guess


@pytest.mark.parametrize("data", DATASET)
def test_solution(data, mocker):
    guess = get_guess_func(data[1])
    mocker.patch(Solution.__module__ + '.guess' , side_effect=guess)
    result = Solution().guessNumber(data[0])
    assert result == data[1], result
