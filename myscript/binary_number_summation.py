interactive=True

def main():
    if not interactive:
        n = 5
        a=[1,0,1,0,1]
        b=[0,1,1,1,1]
    else:
        #input from stdin
        n = int(input())
        a = [int(item) for item in input().split()]
        b = [int(item) for item in input().split()]
    #add two integers stored in binary form
    carry=0
    c=[]
    for i in range(n):
        k=a[i]+b[i]+carry
        c.append(k%2)
        carry=1 if k>1 else 0
    if carry==1:
        c.append(1)
    print(c)

if __name__ == '__main__':
    main()
    
