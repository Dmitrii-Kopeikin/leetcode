import pytest

from ..solution import UndergroundSystem


DATASET = [
    (
        (
            [
                "UndergroundSystem",
                "checkIn",
                "checkIn",
                "checkIn",
                "checkOut",
                "checkOut",
                "checkOut",
                "getAverageTime",
                "getAverageTime",
                "checkIn",
                "getAverageTime",
                "checkOut",
                "getAverageTime",
            ],
            [
                [],
                [45, "Leyton", 3],
                [32, "Paradise", 8],
                [27, "Leyton", 10],
                [45, "Waterloo", 15],
                [27, "Waterloo", 20],
                [32, "Cambridge", 22],
                ["Paradise", "Cambridge"],
                ["Leyton", "Waterloo"],
                [10, "Leyton", 24],
                ["Leyton", "Waterloo"],
                [10, "Waterloo", 38],
                ["Leyton", "Waterloo"],
            ],
        ), [None, None, None, None, None, None, None, 14.00000, 11.00000, None, 11.00000, None, 12.00000]),
    (
        (
            [
                "UndergroundSystem",
                "checkIn",
                "checkOut",
                "getAverageTime",
                "checkIn",
                "checkOut",
                "getAverageTime",
                "checkIn",
                "checkOut",
                "getAverageTime",
            ],
            [
                [],
                [10, "Leyton", 3],
                [10, "Paradise", 8],
                ["Leyton", "Paradise"],
                [5, "Leyton", 10],
                [5, "Paradise", 16],
                ["Leyton", "Paradise"],
                [2, "Leyton", 21],
                [2, "Paradise", 30],
                ["Leyton", "Paradise"],
            ]
        ),
        [None, None, None, 5.00000, None, None, 5.50000, None, None, 6.66667],
    ),
]


def get_average_time_rounded(underground_system: UndergroundSystem, precision: int):

    def func(*args, **kwargs):
        return round(underground_system.getAverageTime(*args, **kwargs), precision)

    return func


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    underground_system = UndergroundSystem()
    commands_dict = {
        'checkIn': underground_system.checkIn,
        'checkOut': underground_system.checkOut,
        # wrap for limited precision
        'getAverageTime': get_average_time_rounded(underground_system, 5),
    }
    commands = data[0][0][1:]
    commands_args = data[0][1][1:]
    target_result = data[1]
    result = [None]
    for i, command in enumerate(commands):
        result.append(commands_dict[command](*commands_args[i]))

    assert result == target_result, result
