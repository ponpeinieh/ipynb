interactive=False

def main():
    if interactive:
        n = int(input())
        a = [int(item) for item in input().split()]
    else:
        n=5
        a=[4,3,1,5,2]
    #selection sort
    for i in range(n-1):
        min = a[i]
        min_ind = i;
        for j in range(i,n):
            if a[j]<min:
                min=a[j];
                min_ind=j;
            #swap with a[i]
            temp = a[i]
            a[i]=a[min_ind]
            a[min_ind]=temp       
    print(a)

if __name__=='__main__':
    main()
