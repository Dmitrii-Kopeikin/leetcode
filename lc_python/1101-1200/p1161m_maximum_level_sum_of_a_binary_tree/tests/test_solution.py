import pytest

from ..solution import Solution
from ..solution import TreeNode


def create_bt(values: list) -> TreeNode:
    ...


DATASET = [
    (
        TreeNode(
            1,
            TreeNode(
                7,
                TreeNode(7),
                TreeNode(-8),
            ),
            TreeNode(0),
        ),
        2,
    ),
    (
        TreeNode(
            989,
            None,
            TreeNode(
                10250,
                TreeNode(98693),
                TreeNode(
                    -89388,
                    None,
                    TreeNode(-32127)
                )
            )
        ),
        2,
    ),
    (
        TreeNode(
            -100,
            TreeNode(
                -200,
                TreeNode(-20),
                TreeNode(-5),
            ),
            TreeNode(
                -300,
                TreeNode(-10)
            )
        ),
        3,
    )
]


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().maxLevelSum(data[0])
    assert result == data[1], result
