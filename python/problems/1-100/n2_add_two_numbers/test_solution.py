import pytest

from .solution import Solution, ListNode


def create_node_from_list(nums: list) -> ListNode:
    if nums == None:
        return None
    
    if len(nums) == 1:
        return ListNode(nums[0])
    
    return ListNode(nums[0], create_node_from_list(nums[1:]))


DATASET = [
    (
        (
            ListNode(2, ListNode(4, ListNode(3))),
            ListNode(5, ListNode(6, ListNode(4))),
        ),
        ListNode(7, ListNode(0, ListNode(8))),
    ),
    (
        (
            ListNode(0),
            ListNode(0),
        ),
        ListNode(0),
    ),
    (
        (
            create_node_from_list([9,9,9,9,9,9,9]),
            create_node_from_list([9,9,9,9]),
        ),
        create_node_from_list([8,9,9,9,0,0,0,1]),
    ),
]


def is_nodes_equal(node1: ListNode, node2: ListNode) -> bool:
    while node1 or node2:
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        node1 = node1.next
        node2 = node2.next

    return True


def test_is_nodes_equal():
    node1 = ListNode(10)
    node2 = ListNode(10)
    assert is_nodes_equal(node1, node2), f"{node1} : {node2}"
    node1 = ListNode(1, ListNode(2, ListNode(3)))
    node2 = ListNode(1, ListNode(2, ListNode(3)))
    assert is_nodes_equal(node1, node2), f"{node1} : {node2}"
    node2 = ListNode(1, ListNode(2, ListNode(3)))
    node2 = ListNode(10)
    assert not is_nodes_equal(node1, node2), f"{node1} : {node2}"


def test_create_node_from_list():
    assert is_nodes_equal(create_node_from_list([1, 2, 3]), ListNode(1, ListNode(2, ListNode(3))))


@pytest.mark.parametrize("data", DATASET)
def test_solution(data):
    result = Solution().addTwoNumbers(*data[0])
    assert is_nodes_equal(result, data[1]), f"{result} : {data[1]}"
