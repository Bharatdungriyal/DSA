"""Array basics Questions"""
def find_Min_Max(arry):
    if not arry:
        raise "array is empty"

    min_value = arry[0]
    max_value = arry[0]
    for item in arry:
        if item>min_value:
            min_value= item
        if item<max_value:
            max_value = item

    return max_value, min_value


my_array = [-71,2,3,45,5,65,7,28,9]
min_value,max_value = find_Min_Max(my_array)
print(f"The minimum and maximum values are {min_value, max_value}")


def reverse_array(arr):
    y = len(arr)
    for i in range(y//2):
        temp= arr[i]
        arr[i]=arr[y-i-1]
        arr[y-i-1]= temp

arr = [1,2,3,1,5,4,5]
reverse_array(arr)
print(arr)



def reverse_string(s):
    reversed_string= ""
    for item in s:
        reversed_string = item + reversed_string
    return reversed_string

strng = "Hello Bharat"
input= reverse_string(strng)
print(input)




