import operator
OPERATIONS = ["+","-","/","*"]
ops = {
       "+":operator.add,
       "-":operator.sub,
       "*":operator.mul,
       "/":operator.div,

       "%":operator.mod,
       "^":operator.pow
       }

def solveRPN(symbols):
    symbols = symbols.split() #" 1 2 +" => ["1","2","+"]
    a = reduce(action,symbols,[])
    print a
    return a


def action(stack,op):
    if op not in ops:
        stack.append(int(op))
        return stack

    if len(stack) < 2:
        raise "error"

    x,y = stack.pop() , stack.pop()
    stack.append( ops[op](x,y) )
    return stack


