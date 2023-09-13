def full_fill_ing(num, init_index, sub_value, arr):
    fill(num, init_index, arr[init_index], sub_value, arr)

def fill(num, init_index, original_value, sub_value, arr):

    if init_index <0 or init_index >= num:
        return
    
    if arr[init_index] != original_value:
        return
    
    if arr[init_index] == sub_value:
        return
    
    arr[init_index] = sub_value
    fill(num, init_index - 1, original_value, sub_value, arr)
    fill(num, init_index + 1, original_value, sub_value, arr)

num, init_index, sub_value = map(int, input().split())

arr = list(map(int, input().split()))


full_fill_ing(num, init_index, sub_value, arr)


print(" ".join(map(str, arr)))  # Format the output as a space-separated string


# Takeaway: when making modification on the original array, pass in the orifinal 
#           values but limit the index 