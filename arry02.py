# Reversing an array with taking user input

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
# taking input from user for reversing an array
def manual_input_array():
    brr = []
    print("Enter the number of elements in the array:")
    x = int(input())  # Read the number of elements

    print("Enter the elements of the array one by one:")
    for _ in range(x):
        element = int(input())  # Read each element one by one
        brr.append(element)

    return brr

inpt = manual_input_array()  # Take input manually
reverse_array(inpt)
print("Reversed array:", inpt)


