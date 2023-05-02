class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dict = {
            character: order_index for order_index, character in enumerate(order)
        }

        first_index = 0
        second_index = 1

        while second_index < len(words):
            first_word = words[first_index]
            second_word = words[second_index]

            character_index = 0
            while character_index < len(first_word):
                if character_index == len(second_word):
                    return False
                if (
                    order_dict[first_word[character_index]]
                    < order_dict[second_word[character_index]]
                ):
                    break
                if (
                    order_dict[first_word[character_index]]
                    > order_dict[second_word[character_index]]
                ):
                    return False

                character_index += 1

            first_index += 1
            second_index += 1

        return True
