memory_data = {}

def get_substring_list(original, start_i, end_i):
    if memory_data.get((start_i,end_i)):
        return memory_data.get((start_i,end_i))
    substr_list=[]
    if check_larger_number(original[start_i:end_i+1]):
        substr_list.append([original[start_i:end_i+1]])
    for i in range(start_i+1, end_i+1):
        head_str = original[start_i:i]
        if check_larger_number(head_str):
            tail_list=check_if_fibonacci2(get_substring_list(original, i,end_i))
            for r in tail_list:
                new_list = [head_str]+r
                if check_if_fibonacci_leading_zero(new_list):
                    substr_list.append(new_list)
        else:
            break
    memory_data[(start_i,end_i)]=substr_list
    return substr_list

def check_larger_number(num_str):
    print(num_str)
    if len(num_str)>10:
        return False
    elif len(num_str)<10:
        return True
    else:
        num = int(num_str)
        if num> (2**31)-1:
            return False
        else:
            return True
def check_larger_number2(num):
    if num> (2**31)-1:
        return False
    else:
        return True

def has_leading_zero(num_str_list):
    for n in num_str_list:
        if len(n)>1 and n[0]=='0':
            return True
    return False
    
def check_if_fibonacci_leading_zero(num_str_list):
    if has_leading_zero(num_str_list):
        return False
    else:
        num_list = list(map(int, num_str_list))
        for i in range(2, len(num_list)):
            if not check_larger_number2(num_list[i]):
                return False
            if num_list[i]!=num_list[i-1]+num_list[i-2]:
                return False
        return True
def check_if_fibonacci(num_str_list):
    num_list = list(map(int, num_str_list))
    for i in range(2, len(num_list)):
        if num_list[i]!=num_list[i-1]+num_list[i-2]:
            return False
    return True
def check_if_fibonacci2(num_str_list2):
    result=[]
    for num_str_list in num_str_list2:
        if has_leading_zero(num_str_list):
            continue
        if len(num_str_list)==1:
            result.append(num_str_list)
            continue
        elif len(num_str_list)==2 and num_str_list[0]<num_str_list[1]:
            result.append(num_str_list)
            continue
        elif check_if_fibonacci(num_str_list):
            result.append(num_str_list)
    return result   

class Solution:
    def splitIntoFibonacci(self, input_num) :
        global memory_data 
        memory_data = {}
        result = get_substring_list(input_num,0,len(input_num)-1)
        is_fibo=False
        for num_str_list in result:
            if len(num_str_list)>=3 and check_if_fibonacci_leading_zero(num_str_list):
                is_fibo=True
                return list(map(int,num_str_list))
        if not is_fibo:
            return []

s = Solution().splitIntoFibonacci("7491213482516")
print(s)