count=0
mystoredata = {} #dict
def factorial(n):
    global count
    count+=1
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        if n-1 in mystoredata:
            r1 = mystoredata[n-1]
        else: 
            r1 = factorial(n-1)
        if n-2 in mystoredata:
            r2 = mystoredata[n-2]
        else:
            r2 = factorial(n-2)
        result = r1+r2
        mystoredata[n]=result
        return result
result = factorial(10)
print(f'result={result}')
print(f'count={count}')
print(mystoredata)
