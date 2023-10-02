def get_substring_list(original, start_i, end_i):
    if memory_data.get((start_i,end_i)):
        return memory_data.get((start_i,end_i))
    substr_list=[]
    substr_list.append([original[start_i:end_i+1]])
    for i in range(start_i+1, end_i+1):
        head_str = original[start_i:i]
        tail_list=get_substring_list(original, i,end_i)
        for r in tail_list:
            new_list = [head_str]+r
            substr_list.append(new_list)  
    memory_data[(start_i,end_i)]=substr_list
    return substr_list

class Solution:
    def splitIntoFibonacci(self, input_num) :
        global memory_data 
        memory_data = {}
        result = get_substring_list(input_num,0,len(input_num)-1)
        return result
        
s = Solution().splitIntoFibonacci("hello")
print(s)