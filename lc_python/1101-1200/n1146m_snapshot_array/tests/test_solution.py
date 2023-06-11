import pytest

from ..solution import SnapshotArray


DATASET = [
    (None, None),
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    snapshot_array = SnapshotArray(3)
    assert snapshot_array.length == 3
    snapshot_array.set(0, 5) 
    assert snapshot_array.snap() == 0
    snapshot_array.set(0, 6)
    assert snapshot_array.get(0, 0) == 5
    assert snapshot_array.get(1, 0) == 0
    snapshot_array.set(0, 6)
    assert snapshot_array.snap() == 1
    assert snapshot_array.get(0, 1) == 6
    assert snapshot_array.get(2, 1) == 0
