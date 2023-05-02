class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        o_d = {c: o_i for o_i, c in enumerate(order)}

        w_i = 0
        n_w_i = 1
        while n_w_i < len(words):
            w = words[w_i]
            w_i += 1
            n_w = words[n_w_i]
            n_w_i += 1
            for c_i, c in enumerate(w):
                if c_i == len(n_w):
                    return False
                if o_d[c] < o_d[n_w[c_i]]:
                    break
                if o_d[c] > o_d[n_w[c_i]]:
                    return False

        return True


solution = Solution()
print(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print(
    solution.isAlienSorted(
        [
            "fxasxpc",
            "dfbdrifhp",
            "nwzgs",
            "cmwqriv",
            "ebulyfyve",
            "miracx",
            "sxckdwzv",
            "dtijzluhts",
            "wwbmnge",
            "qmjwymmyox",
        ],
        "zkgwaverfimqxbnctdplsjyohu",
    )
)
