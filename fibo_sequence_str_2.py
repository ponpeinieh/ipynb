
def is_overflow(num_str):
    if len(num_str)>10:
        return True
    elif len(num_str)<10:
        return False
    elif int(num_str)>2147483647:
        return True
    else:
        return False 


def has_leading_zero(num_str):
    if num_str[0] == '0' and len(num_str) > 1:
        return True
    return False


def check_if_fibonacci(triplet):
    return int(triplet[0])+int(triplet[1]) == int(triplet[2])

def calculate_list(result, num):
    if len(result)==1:
        start_i = 0
        end_i = len(num)
        for i in range(start_i+1, end_i+1):
            next_num_str = num[start_i:i]
            if has_leading_zero(next_num_str) or is_overflow(next_num_str):
                break
            result.append(next_num_str)
            if calculate_list(result, num[i:]):
                return True
            else:
                result.pop()
        return False
    elif len(result)>=2:
        start_i = 0
        end_i = len(num)

        max_len = max(len(result[-2]), len(result[-1]))
        if len(num)>=max_len:
            for i in range(max_len, min(max_len+1,len(num))+1):
                next_num_str = num[start_i:i]
                if has_leading_zero(next_num_str) or is_overflow(next_num_str):
                    break
                result.append(next_num_str)
                if check_if_fibonacci(result[-3:]):
                    if i == end_i: #!!!
                        return True
                    if calculate_list(result, num[i:]):
                        return True
                    else:
                        result.pop()
                else:
                    result.pop()
        return False
   
class Solution:
    def splitIntoFibonacci(self, num): 
        start_i = 0
        end_i = len(num)
        result = []
        if end_i >= 3:
            for i in range(start_i+1, end_i-1):
                head_num_str = num[start_i:i]
                if has_leading_zero(head_num_str) or is_overflow(head_num_str):
                    break
                result.append(head_num_str)
                if calculate_list(result, num[i:]):
                    return list(map(int,result)) 
                else:
                    result.pop()
        return result
    

s = Solution().splitIntoFibonacci("1101111")
print(s)
s = Solution().splitIntoFibonacci("11235813")
print(s)
s = Solution().splitIntoFibonacci("7491213482516")
print(s)
