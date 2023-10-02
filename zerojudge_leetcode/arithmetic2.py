
def doMath(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        result = num1+num2 
    elif op == '-':
        result = num1-num2
    elif op == '*':
        result = num1*num2
    elif op == '/':
        result = num1//num2
    elif op == '%':
        result = num1 % num2
    return str(result)

def arithmetic_op(tokens):
    operand_queue=[]
    operator_queue=[]
    i = 0
    while i<len(tokens):
        t = tokens[i]
        i+=1
        if t.isdigit():
            operand_queue.append(t)
        elif t in "+-":
            if len(operator_queue)>=1 and operator_queue[-1] in "+-":
                opd2 = operand_queue.pop()
                opd1 = operand_queue.pop()
                opr = operator_queue.pop()
                result = doMath(opd1, opd2, opr)
                operand_queue.append(result)
            operator_queue.append(t)
        elif t in "*/%":
            next_token = tokens[i]
            i+=1
            if next_token.isdigit():
                opd1 = operand_queue.pop()
                opd2 = next_token
                result = doMath(opd1,opd2,t)
                operand_queue.append(result)
            elif next_token == '(': # must be a left parenthesis
                operator_queue.append(t)
                operator_queue.append(next_token)
        elif t == "(":
            operator_queue.append(t)
        elif t == ")":
            if operator_queue[-1] in "+-":
                opd2 = operand_queue.pop()
                opd1 = operand_queue.pop()
                opr = operator_queue.pop()
                result = doMath(opd1, opd2, opr)
                operand_queue.append(result)
                operator_queue.pop() #remove left parenthesis
            else:
                operator_queue.pop() # remove left parenthesis
            if len(operator_queue)>=1 and operator_queue[-1] in "*/%":
                opd2 = operand_queue.pop()
                opd1 = operand_queue.pop()
                opr = operator_queue.pop()
                result = doMath(opd1, opd2, opr)
                operand_queue.append(result)
    if len(operator_queue)>=1:
        opd2 = operand_queue.pop()
        opd1 = operand_queue.pop()
        opr = operator_queue.pop()
        result = doMath(opd1, opd2, opr)
    else:
        result = operand_queue.pop()
    return int(result)

# statement = "( 10 / ( 2 ) * ( ( ( 3 + 4 ) * ( 5 - 2 ) ) % 6 ) )"
# tokens = statement.split()
# print(tokens)
# result = arithmetic_op(tokens)
# print(result)

while True:
    try:
        statement = input()
        tokens = statement.split()
        result = arithmetic_op(tokens)
        print(result)
    except EOFError:
        break