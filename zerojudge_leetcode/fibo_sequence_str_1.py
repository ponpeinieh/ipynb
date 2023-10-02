
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


def check_if_fibonacci(num_str1, num_str2, num_str3):
    return int(num_str1)+int(num_str2) == int(num_str3)


def calculate_list(head_num_str, head_num2_str, num_str): 
    result = []
    max_len = max(len(head_num_str), len(head_num2_str))
    if len(num_str)>=max_len:
        for i in range(max_len, min(max_len+1,len(num_str))+1):
            head_num3_str = num_str[0:i]
            if head_num3_str:
                if has_leading_zero(head_num3_str) or is_overflow(head_num3_str):
                    break
                if check_if_fibonacci(head_num_str, head_num2_str,head_num3_str): 
                    if i>=len(num_str):
                        result.append([head_num_str, head_num2_str,head_num3_str])
                    else:
                        sub_result = calculate_list(head_num2_str,head_num3_str,num_str[i:len(num_str)])
                        if sub_result:
                            for r in sub_result:
                                result.append([head_num_str]+r)
    return result

class Solution:
    def splitIntoFibonacci(self, num): 
        start_i = 0
        end_i = len(num)
        result = []

        if end_i >= 3:
            for i in range(start_i+1, end_i):
                head_num_str = num[start_i:i]
                if has_leading_zero(head_num_str) or is_overflow(head_num_str):
                    break
                for j in range(i+1, end_i):
                    head_num2_str = num[i:j]
                    if has_leading_zero(head_num2_str) or is_overflow(head_num2_str):
                        break
                    result= result+calculate_list(
                        head_num_str, head_num2_str, num[j:end_i])
        if result:
            result = list(map(int,result[0]))            
        return result

 

s = Solution().splitIntoFibonacci("7491213482516")
print(s)
s = Solution().splitIntoFibonacci("1101111")
print(s)
s = Solution().splitIntoFibonacci("0123")
print(s)
s = Solution().splitIntoFibonacci("11235813")
print(s)
