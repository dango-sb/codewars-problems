def max_sum_between_two_negatives(arr):
    max_sum = 0
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            if (arr[start]<0 and arr[end]<0) and (sum(arr[start+1:end]) > max_sum) and len([i for i in arr[start:end+1] if i < 0]) == 2:
                max_sum = sum(arr[start+1:end])
                ind = [start, end]
    return max_sum, ind 
                
print(max_sum_between_two_negatives([4, -1, 6, -2, 3, 5, -7, 7]))

# def max_sum_between_two_negatives(arr):
#     max_sum = 0
#     i,j = 0
#     while j < len(arr) and i < len(arr):
#         if (arr[i]<0 and arr[j]<0) and (sum(arr[i+1:j]) > max_sum):
            
#         j += 1
#         i = j