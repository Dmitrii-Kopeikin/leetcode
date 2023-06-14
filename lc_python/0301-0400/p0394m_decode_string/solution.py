class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for l in s:
            if l != ']':
                stack.append(l)
                continue
            substr = l = ''
            while l != '[':
                substr += l
                l = stack.pop()
            substr = substr[::-1]

            count = ''
            while stack and stack[-1].isdigit():
                count += stack.pop()
            count = count[::-1]
            num = int(count)

            stack.extend(substr * num)

        return ''.join(stack)