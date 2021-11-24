# infix to postfix algorithm:

# # 1 Create an empty stack called opstack for keeping
# #   operators. Create an empty list for output. 

# # 2 Convert the input infix string to a list by using the string
# #   method split.

# #3 Scan the token list from left to right.
#         # If the token is an operand, append it to the end of the output
#         # list.
#         # If the token is a left parenthesis, push it on the opstack.
#         # If the token is a right parenthesis, pop the opstack until
#         # the corresponding left parenthesis is removed. Append
#         # each operator to the end of the output list.
#         # If the token is an operator, ^, *, /, +, or -, push it on the
#         # opstack. However, first remove any operators already on
#         # the opstack that have higher or equal precedence and
#         # append them to the output list.
        
# # 4 When the input expression has been completely
# # processed, check the opstack. Any operators still on the
# # stack can be removed and appended to the end of the
# # output list.
from stack import Stack

def infixToPostfix(infixexpr):
    prec = { 
        "^": 4,
        "*":3,
        "/":3,
        "+":2,
        "–":2,
        "(":1,
    }

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        # if the token is an operand (A , B , ..) add it to the output
        if token not in prec and token != ')': 
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ')':
            top = opStack.pop()
            while top != '(':
                postfixList.append(top)
                top = opStack.pop()

        else:
            while (not opStack.isEmpty()) and (prec[token] <= prec[opStack.peek()]):
                postfixList.append(opStack.pop())
            opStack.push(token)    

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)                        

# postfix evaluation algorithm:
# 1. If the current item is an operand, push its value onto the stack.
# 2. If the current item is an operator:
    # (a) Pop the top two operands off the stack.
    # (b) Perform the operation. (Note the top value is the right operand while the
    # next to the top value is the left operand.)
    # (c) Push the result of this operation back onto the stack.
# The final result of the expression will be the last value on the stack    

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    operators = ['+' , '–' , '*' , '/']
    for token in tokenList:
        if token in operators:
            second = (operandStack.pop())
            first = operandStack.pop()
            result = doMath(first , second , token)
            operandStack.push(result)
        else:
            operandStack.push(int(token)) 

    return operandStack.pop()        

def doMath(op1 , op2 , operator):
    if operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2               
    elif operator == '–':
        return op1 - op2               
    elif operator == '+':
        return op1 + op2                  

print(infixToPostfix("v * w * x + y - z"))                 