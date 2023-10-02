'''
請參看largest_product ipynb的注解說明
'''

minus_count=0
def calc_temp_list(n, data):
    if n==1:
        return data[0]
    global minus_count
    minus_count=0
    product = 1
    temp_list = []
    for k in data:
        if k < 0 :
            minus_count+=1
            temp_list.append(product)
            temp_list.append(k)
            product=1
        else:
            product*=k
    temp_list.append(product)
    return temp_list

def calc(temp_list):
    if len(temp_list)==1:
        return temp_list[0]
    if minus_count%2 == 0:
        product = 1
        for k in temp_list:
            product*=k
        return product
    else:
        products=[]
        product1 = 1
        for k in temp_list[:-2]:
            product1*=k
        products.append(product1)
        products.append(temp_list[-1])
        products.append(temp_list[0])
        product4=1
        for k in temp_list[2:]:
            product4*=k
        products.append(product4)
    print(products)
    return max(products)

n = 10
data = [2, 3, -1, 4, 6, -2, 10, 8, -3, 5]
result = calc_temp_list(n,data)
max_product = calc(result)
print(max_product)
