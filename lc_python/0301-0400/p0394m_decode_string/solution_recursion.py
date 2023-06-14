class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s: list) -> list:
            l = 0
            r = len(s) - 1
            while l < len(s) and s[l] != '[':
                l += 1
            r = l
            c = 0
            while r < len(s):
                if s[r] == '[':
                    c += 1
                if s[r] == ']':
                    c -= 1
                    if c == 0:
                        break
                r += 1

            count_p = l - 1
            while count_p > 0 and s[count_p - 1].isdigit():
                count_p -= 1

            if l != r:
                s = s[0:count_p] + decode(s[l+1:r]) * int(''.join(s[count_p:l])) + decode(s[r+1:])
            return s

        return ''.join(decode(list(s)))