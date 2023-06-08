import pytest

from ..solution import MyHashSet


# DATASET = [
#     (None, None),
# ]


# @pytest.mark.parametrize("data", DATASET)
def test_solution():
    my_hashset = MyHashSet()

    assert my_hashset.add(1) == None
    assert my_hashset.add(2) == None
    assert my_hashset.contains(1) == True
    assert my_hashset.contains(3) == False
    assert my_hashset.add(2) == None
    assert my_hashset.contains(2) == True
    assert my_hashset.remove(2) == None
    assert my_hashset.contains(2) == False

