import random
interactive=False
random_gen_data=True
num_data=1000000

def merge(a,p,q,r): 
    a1=a[p:q+1]
    a2=a[q+1:r+1]
    a1.append(float('inf'))
    a2.append(float('inf'))
    i1=0
    i2=0
    for i in range(r-p+1):
        if a1[i1]<=a2[i2]:
            a[p+i]=a1[i1]
            i1+=1
        else:
            a[p+i]=a2[i2]
            i2+=1
def merge_sort(a,p,r):
    if p>=r:
        return
    else:
        q=(p+r)//2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)
def main():
    if interactive:
        n = int(input())
        a = [int(item) for item in input().split()]
    elif random_gen_data:
        a=[]
        n=num_data
        for i in range(n):
            a.append(random.randint(1,100))
    else:
        n=5
        a=[4,3,1,5,2]
    #merge sort
    merge_sort(a,0,n-1)
    #print(a)

if __name__=='__main__':
    main()
