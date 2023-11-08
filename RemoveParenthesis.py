from collections import deque

def removeInvalidParentheses(s):
    def is_valid(string):
        count = 0
        for char in string:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    queue = deque()
    visited = set()
    result = []

    queue.append(s)
    visited.add(s)
    found_valid = False

    while queue:
        current = queue.popleft()
        if is_valid(current):
            result.append(current)
            found_valid = True

        if found_valid:
            continue

        for i in range(len(current)):
            if current[i] not in ('(', ')'):
                continue

            new_string = current[:i] + current[i+1:]
            if new_string not in visited:
                queue.append(new_string)
                visited.add(new_string)

    return result

# Test cases
s1 = "()())()"
print(removeInvalidParentheses(s1)) 

s2 = "(a)())()"
print(removeInvalidParentheses(s2))  

s3 = ")("
print(removeInvalidParentheses(s3)) 
