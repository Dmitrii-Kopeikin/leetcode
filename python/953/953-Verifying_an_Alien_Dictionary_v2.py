class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dict = {character: order_index for order_index,
                      character in enumerate(order)}

        word_index = 0
        next_word_index = 1
        words_len = len(words)
        while next_word_index < words_len:
            word = words[word_index]
            word_index += 1
            next_word = words[next_word_index]
            next_word_index += 1
            next_word_length = len(next_word)
            for character_index, character in enumerate(word):
                if character_index == next_word_length:
                    return False
                if order_dict[character] < order_dict[next_word[character_index]]:
                    break
                if order_dict[character] > order_dict[next_word[character_index]]:
                    return False

        return True


solution = Solution()
print(solution.isAlienSorted(
    ['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'))
print(solution.isAlienSorted(
    ['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'))
print(solution.isAlienSorted(
    ['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'))
print(solution.isAlienSorted(
    ['fxasxpc', 'dfbdrifhp', 'nwzgs', 'cmwqriv', 'ebulyfyve', 'miracx', 'sxckdwzv',
     'dtijzluhts', 'wwbmnge', 'qmjwymmyox'], 'zkgwaverfimqxbnctdplsjyohu'))
