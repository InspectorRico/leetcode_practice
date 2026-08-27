class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing_brackets = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closing_brackets:
                if stack and stack[-1] == closing_brackets[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)


        if len(stack) == 0:
            return True
        else:
            return False