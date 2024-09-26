def BubbleSort(my_lst):
    lst_len = len(my_lst)
    for i in range(lst_len-1):
        for j in range(lst_len-1-i):
            if my_lst[j]>my_lst[j+1]:
                my_lst[j], my_lst[j+1] = my_lst[j+1],my_lst[j]
    
    return my_lst

lst = [4,6,2,3,1]

print(BubbleSort(lst))