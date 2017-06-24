list = [5,2,0,3,0,1,6,0]
list.sort(key=int)

list1 =  list[0:3]
list2 = list[3:]
list_end = list2 + list1

print list_end


mylist = [5,2,0,3,0,1,6,0]
new_list = []
new_zero = []
def srted_list(list):
    list.sort(key=int)
    n = len(mylist)
    for n in range(n):
        if list[n] > 0:
            new_list.append(list[n])
        elif list[n] == 0:
            new_zero.append(list[n])
    print new_list + new_zero

srted_list(mylist)
