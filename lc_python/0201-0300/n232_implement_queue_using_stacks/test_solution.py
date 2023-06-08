import pytest

from .solution import MyQueue
from .solution_other import MyQueue as OtherMyQueue


DATASET = [
    MyQueue,
    OtherMyQueue,
]


@pytest.mark.parametrize('cls', DATASET)
def test_my_queue(cls):
    my_queue = cls()
    my_queue.push(1)
    my_queue.push(2)

    assert my_queue.peek() == 1
    assert my_queue.pop() == 1
    assert my_queue.empty() == False
    assert my_queue.pop() == 2
    assert my_queue.empty() == True


