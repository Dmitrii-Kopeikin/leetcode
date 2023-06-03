from typing import List, Optional
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not all([beginWord, endWord, endWord in wordList, wordList]):
            return 0

        combinations = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                combinations[f"{word[:i]}*{word[i + 1:]}"].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, step = queue.popleft()
            for i in range(len(word)):
                w = f"{word[:i]}*{word[i + 1:]}"
                for next_word in combinations[w]:
                    if next_word == endWord:
                        return step + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, step + 1))
                combinations[w] = {}

        return 0

# SLOW
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0

#         def is_valid_word(word: str, other_word: str):
#             count = 0
#             for i in range(len(word)):
#                 if word[i] != other_word[i]:
#                     count += 1
#             return count == 1

#         visited = set([beginWord])
#         quaue = deque([(beginWord, 0)])

#         print(quaue)

#         while quaue:
#             start_word, steps = quaue.pop()
#             if start_word == endWord:
#                 return steps + 1
#             for word in wordList:
#                 if word not in visited and is_valid_word(start_word, word):
#                     visited.add(word)
#                     quaue.appendleft((word, steps + 1))

#         return 0
