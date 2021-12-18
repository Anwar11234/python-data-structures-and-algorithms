from tree import BinaryTree
from pythonds import Stack
import operator

def buildParseTree(fpexp):
    fpList = fpexp.split()
    parentStack = Stack()
    expTree = BinaryTree('')
    parentStack.push(expTree)
    curr = expTree

    for i in fpList:
        if i == '(':
            curr.insertLeft('')
            parentStack.push(curr)
            curr = curr.getLeftChild()

        elif i not in '+-*/)':
            curr.setRootVal(int(i))
            curr = parentStack.pop()

        elif i in '+-*/':
            curr.setRootVal(i)
            curr.insertRight('')
            parentStack.push(curr)
            curr = curr.getrightChild() 

        elif i == ')':
            curr = parentStack.pop()

        else:
            print('error: cannot recognize ' + i)

    return expTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")

def evaluate(parsetree):
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }

    leftChild = parsetree.getLeftChild()
    rightChild = parsetree.getRightChild()

    if leftChild and rightChild:
        fn = opers[parsetree.getRootVal()]
        return fn(evaluate(leftChild) , evaluate(rightChild))
    else:
        return parsetree.getRootVal()