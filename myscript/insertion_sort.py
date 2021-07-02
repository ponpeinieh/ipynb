interactive=True

def main():
    if interactive:
        n = int(input())
        a = [int(item) for item in input().split()]
    else:
        n=5
        a=[4,3,1,5,2]
    #insertion sort
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    print(a)

if __name__=='__main__':
    main()
