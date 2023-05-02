import pytest

from .solution import LFUCache
from .solution_deque import LFUCache as LFUCacheDeque
from .solution_dict_accepted import LFUCache as LFUCacheDict
from .solution_my_linked_list import LFUCache as LFUCacheLinkedList


@pytest.mark.parametrize(
    "cls", [LFUCache, LFUCacheDeque, LFUCacheDict, LFUCacheLinkedList]
)
def test_lfu_cache(cls):
    lfu_cache = cls(2)
    lfu_cache.put(1, 1)
    lfu_cache.put(2, 2)
    assert lfu_cache.get(1) == 1
    lfu_cache.put(3, 3)
    assert lfu_cache.get(2) == -1
    assert lfu_cache.get(3) == 3
    lfu_cache.put(4, 4)
    assert lfu_cache.get(1) == -1
    assert lfu_cache.get(3) == 3
    assert lfu_cache.get(4) == 4
