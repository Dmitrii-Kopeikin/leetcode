from solution import Solution


def test_count_pairs():
    solution = Solution()
    dataset = [
        (3, [[0, 1], [0, 2], [1, 2]], 0),
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14),
    ]

    for data in dataset:
        assert data[2] == solution.count_pairs(data[0], data[1])
