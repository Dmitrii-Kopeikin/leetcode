import pytest

from .solution import KthLargest


def test_solution():
    structure = KthLargest(3, [4, 5, 8, 2])
    assert 4 == structure.add(3)
    assert 5 == structure.add(5)
    assert 5 == structure.add(10)
    assert 8 == structure.add(9)
    assert 8 == structure.add(4)

    structure = KthLargest(1, [])
    assert -3 == structure.add(-3)
    assert -2 == structure.add(-2)
    assert -2 == structure.add(-4)
    assert 0 == structure.add(0)
    assert 4 == structure.add(4)

    structure = KthLargest(3, [5, -1])
    assert -1 == structure.add(2)
    assert 1 == structure.add(1)
    assert 1 == structure.add(-1)
    assert 2 == structure.add(3)
    assert 3 == structure.add(4)