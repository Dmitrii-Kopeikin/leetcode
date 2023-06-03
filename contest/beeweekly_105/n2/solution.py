from typing import List
from collections import deque


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        queue = deque([(s, set(), len(s))])
        dictionary.sort(key=len)
        print(dictionary)
        min_left = len(s)
        while queue:
            big_word, visited, big_word_len = queue.pop()
            for word in dictionary:
                if word not in visited and word in big_word:
                    end = 0
                    while end < len(big_word) - len(word) and (start := big_word.find(word, end)) != -1:
                        end = start + len(word)
                        next_word = big_word[:start] + big_word[end:]
                        queue.appendleft((next_word, visited.union({word}), big_word_len - len(word)))
                        min_left = min(min_left, big_word_len - len(word))

        return min_left