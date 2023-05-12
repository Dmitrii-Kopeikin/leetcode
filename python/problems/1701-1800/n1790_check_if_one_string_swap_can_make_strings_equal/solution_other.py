class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        diff = ""
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2 or diff and diff != f"{s2[i]}{s1[i]}":
                    return False
                diff = f"{s1[i]}{s2[i]}"
        
        return count == 2