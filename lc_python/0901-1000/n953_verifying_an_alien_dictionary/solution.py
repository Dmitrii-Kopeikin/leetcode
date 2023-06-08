class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        words_length = len(words)
        for word_index, word in enumerate(words):
            if word_index == words_length - 1:
                break
            next_word = words[word_index + 1]
            next_word_length = len(next_word)
            for character_index, character in enumerate(word):
                if character_index == next_word_length:
                    return False
                if order.index(character) < order.index(next_word[character_index]):
                    print(word)
                    break
                if order.index(character) > order.index(next_word[character_index]):
                    return False
        return True
