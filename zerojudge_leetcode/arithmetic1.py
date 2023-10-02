def doPlusAndMinusCalc(tokens):
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
                num1 = t
            else:
                num2 = t
                result = doMath(num1, num2, op)
                num1 = result
        elif t in "+-":
            op = t
    return int(num1)


def doMulDivModCalc(tokens):
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
            num1 = store.pop()
            num2 = tokens[i]
            i += 1
            result = doMath(num1, num2, t)
            store.append(result)

    return doPlusAndMinusCalc(store)

# def doParenthesisCalc(tokens):
#     store = []
#     store2 = []
#     i = 0
#     lp = False
#     num1 = None
#     num2 = None
#     op = None
#     result = None
#     while i < len(tokens):
#         t = tokens[i]
#         i += 1
#         if t.isdigit() or t in "+-*/%":
#             if lp:
#                 store2.append(t)
#             else:
#                 store.append(t)
#         elif t == "(":
#             store2.append(t)
#             if not lp:
#                 lp = True
#         elif t == ")":
#             # find the last "(" from store2
#             pos = None
#             for n in range(len(store2)-1, -1, -1):
#                 if store2[n] == '(':
#                     pos = n
#                     break
#             result = doMulDivModCalc(store2[pos+1:])
#             # remove tokens from store2
#             store2 = store2[:pos]
#             if store2:
#                 store2.append(str(result))
#             else:
#                 lp = False
#                 store.append(str(result))
#     return doMulDivModCalc(store)

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

def replace_in_place(tokens, pos1, pos2, result):
    for _ in range(pos2-pos1+1):
        del tokens[pos1]
    tokens.insert(pos1,result)



def doParenthesisCalc2(tokens):
    # find the inner most pair of parenthesis from tokens
    while True:
        pos1 = None
        pos2 = None
        for n in range(len(tokens)-1, -1, -1):
            if tokens[n] == ')':
                pos2 = n
            elif tokens[n] == '(':
                pos1 = n
                break
        if pos1!=None and pos2!=None:
            result = str(doMulDivModCalc(tokens[pos1+1:pos2]))
            # replace tokens from pos1 and pos2 with result
            replace_in_place(tokens, pos1, pos2, result)
        else:
            break
    return doMulDivModCalc(tokens)

# statement = '1 + 2 - 3 + 4 - 5 - 6'
# statement = '10 / 2 * 3 + 4 - 5 % 6'
# statement = '10 / 2 * ( 3 + 4 ) - 5 % 6'
# statement = "( ( 10 / ( 2 ) ) * ( ( ( 3 + 4 ) * ( 5 - 2 ) ) % 6 ) )"
# tokens = statement.split()
# print(doParenthesisCalc2(tokens))
while True:
    try:
        statement = input()
        tokens = statement.split()
        print(doParenthesisCalc2(tokens))
    except EOFError:
        break
