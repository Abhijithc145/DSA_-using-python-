# add 2 values to find the sum = 10

target=10
arr=[1,2,5,7,8,3,8,0,2]


def find_value(arr_value):
    for i in range(len(arr_value)-1):
        for j in range(i+1,len(arr_value)):
            if arr_value[i]+arr_value[j]==10:
                print(arr_value[i] ,"+",arr_value[j],"=",target)
                

find_value(arr)


# Time complexity = o(n)
# space complexity=o(1)
