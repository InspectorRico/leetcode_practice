# ============================================================
# VALID PARENTHESES — how this solution works
# ============================================================
# Idea: use a STACK to keep track of opening brackets we're
# still "waiting" to close, in the order we opened them.
#
# Walk through the string one character at a time:
#
#   -> OPENING bracket ( [ {
#        Push it onto the stack (it's now waiting to be closed)
#        Then move on to the next character
#
#   -> CLOSING bracket ) ] }
#        It must match the bracket currently on TOP of the stack
#        (the most recently opened, still-unclosed one).
#
#        First check: is the stack even empty?
#          -> if yes, there's nothing to close -> INVALID
#
#        Then check: does it match what's on top?
#          -> ')' must match '('
#          -> ']' must match '['
#          -> '}' must match '{'
#          -> if it doesn't match -> INVALID
#
#        If it matched -> pop the stack (this pair is resolved,
#        move on to the next character)
#
# After going through the whole string:
#   -> if the stack is EMPTY, every bracket got closed properly -> VALID
#   -> if anything is LEFT in the stack, it never got closed -> INVALID
#
# Why a stack (not just a counter)? Because ORDER matters, not just
# count. "([)]" has matching counts but is still invalid — a stack
# naturally enforces that the MOST RECENTLY opened bracket must be
# the FIRST one closed.
# ============================================================

class Solution:
    def isValid(self, s: str) -> bool:
        ...

class Solution:
    def isValid(self, s: str) -> bool:
        # our "pile of plates" - opening brackets go here, waiting to be closed
        stack = []

        for char in s:

            # CASE 1: it's an opening bracket -> just remember it for later
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue  # move to next character

            # CASE 2: it's a closing bracket -> it needs to match
            # whatever opening bracket is on top of the stack right now

            # can't close anything if there's nothing open
            if len(stack) == 0:
                return False

            last_opened = stack[-1]  # peek at the top without removing yet

            if char == ")" and last_opened != "(":
                return False
            if char == "]" and last_opened != "[":
                return False
            if char == "}" and last_opened != "{":
                return False

            # if we get here, it matched correctly -> resolve it
            stack.pop()

        # if anything is still sitting in the stack, it was never closed
        if len(stack) == 0:
            return True
        else:
            return False

        