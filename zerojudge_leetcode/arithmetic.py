def doSimplyPlusAndMinusCalc(tokens):
    if len(tokens) == 1:
        return int(tokens[0])
    i = 0
    num1 = None
    num2 = None
    op = None
    result = None
    while i < len(tokens):
        t = tokens[i]
        i += 1
        if t.isdigit():
            if num1 == None:
                num1 = int(t)
            else:
                num2 = int(t)
                result = doMath(num1, num2, op)
                num1 = result
        elif t in "+-":
            op = t
    return result


def doSimplyMulDivModCalc(tokens):
    if len(tokens) == 1:
        return tokens
    store = []
    i = 0
    num1 = None
    num2 = None
    op = None
    result = None
    while i < len(tokens):
        t = tokens[i]
        i += 1
        if t.isdigit():
            store.append(t)
        elif t in "+-":
            store.append(t)
        elif t in "*/%":
            num1 = int(store.pop())
            num2 = int(tokens[i])
            i += 1
            result = doMath(num1, num2, t)
            store.append(str(result))
    return store


def doSimpleCalc(tokens):
    return doSimplyPlusAndMinusCalc(doSimplyMulDivModCalc(tokens))


def doParenthesisCalc(tokens):
    store = []
    store2 = []
    i = 0
    lp = False
    num1 = None
    num2 = None
    op = None
    result = None
    while i < len(tokens):
        t = tokens[i]
        i += 1
        if t.isdigit() or t in "+-*/%":
            if lp:
                store2.append(t)
            else:
                store.append(t)
        elif t == "(":
            store2.append(t)
            if not lp:
                lp = True
        elif t == ")":
            # find the last "(" from store2
            pos = None
            for n in range(len(store2)-1, -1, -1):
                if store2[n] == '(':
                    pos = n
                    break
            result = doSimpleCalc(store2[pos+1:])
            # remove tokens from store2
            store2 = store2[:pos]
            if store2:
                store2.append(str(result))
            else:
                lp = False
                store.append(str(result))
    return store


def doMath(num1, num2, op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return num1//num2
    elif op == '%':
        return num1 % num2


# statement = '1 + 2 - 3 + 4 - 5 - 6'
# tokens = statement.split()
# result = doSimplyPlusAndMinusCalc(tokens)
# print(result)
# statement = '10 / 2 * 3 + 4 - 5 % 6'
# tokens = statement.split()
# tokens = doSimplyMulDivModCalc(tokens)
# print(tokens)
# result = doSimplyPlusAndMinusCalc(tokens)
# print(result)
# statement = '10 / 2 * ( 3 + 4 ) - 5 % 6'
while True:
    try:
        statement = input()
        tokens = statement.split()
        tokens = doParenthesisCalc(tokens)
        # print(tokens)
        result = doSimpleCalc(tokens)
        print(result)
    except EOFError:
        break
