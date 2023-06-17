class Solution:
    # Bottom-up dp
    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        len_s = len(s)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]

        dp[-1][-1] = True

        for i in range(len_s, -1, -1):
            for j in range(len_p - 1, -1, -1):
                first_match = i < len_s and p[j] in [s[i], '.']
                if j + 1 < len_p and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        
        return dp[0][0]

    # Top-down dp
    # def isMatch(self, s: str, p: str) -> bool:
    #     len_p = len(p)
    #     len_s = len(s)
    #     memo = {}

    #     def dp(i, j):
    #         if (i, j) not in memo:
    #             if j == len_p:
    #                 memo[(i, j)] = i == len_s
    #             else:
    #                 first_match = i < len_s and p[j] in [s[i], '.']

    #                 if j + 1 < len_p and p[j+1] == '*':
    #                     memo[(i, j)] = dp(
    #                         i, j + 2) or first_match and dp(i + 1, j)
    #                 else:
    #                     memo[(i, j)] = first_match and dp(i + 1, j + 1)

    #         return memo[(i, j)]

    #     return dp(0, 0)


    # Python built-in cache
    # @cache
    # def isMatch(self, s: str, p: str) -> bool:
    #     if not p:
    #         return not s

    #     first_match = bool(s) and p[0] in [s[0], '.']

    #     if len(p) >= 2 and p[1] == '*':
    #         return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
    #     else:
    #         return first_match and self.isMatch(s[1:], p[1:])
