from stack import Stack

def isValid(s):
    s1 = Stack()
    for char in s:
        if char in "({[":
            s1.push(char)
        elif char in ")}]":
            if s1.isEmpty():
                return False
            else:
                opening = s1.pop()
                if  (opening == "(" and char != ")") or \
                    (opening == "{" and char != "}") or \
                    (opening == "[" and char != "]"):
                    return False

    return s1.isEmpty()

print(isValid("(){}]"))    