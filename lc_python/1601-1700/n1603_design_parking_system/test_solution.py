import pytest

from .solution import ParkingSystem


DATASET = [
    ([1, 1, 0], [1, 2, 3, 1], [True, True, False, False]),
]


@pytest.mark.parametrize("data", DATASET)
def test_parking_system(data):
    parking_system = ParkingSystem(*data[0])

    result = []
    for car in data[1]:
        result.append(parking_system.addCar(car))

    assert result == data[2], result
