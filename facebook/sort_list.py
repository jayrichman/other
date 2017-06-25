########################Task-1 Generate list for sort [1,2,3,5,6,0,0,0]########################
list = [5,2,0,3,0,1,6,0]
list.sort(key=int)

list1 =  list[0:3]
list2 = list[3:]
list_end = list2 + list1

########################Task2 - Generate list for sort [1,2,3,5,6,0,0,0]########################
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

########################Task3 - Concatenate the list values########################
my_list = ['p','r','o','b','e']

def con_word(list):
    word = ""
    ln = len(list)
    for key in range(ln):
        word += list[key]
    print word
con_word(my_list)
########################Task4 - Print quantity of values from the list which have the same value in [1:-1]########################    
count_str = ['abc', 'xyz', 'aba', '1221']

def len2(list):
    words = 0
    for i in list:
        if len(i) > 1 and i[0] == i[-1]:
            words += 1
    print words
len2(count_str)
########################Task5 - Remove dublicates from list########################
list_dublicates = [1,1,2,3,4,55,6,7,7,8]

def remove_dublicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print new_list

remove_dublicates(list_dublicates)
########################Task6 - Sort list by last element of tuple inside of list########################
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
########################Task7 - Empty List########################
emply_list = []
def check_list(list):
    if not list:
        print "List epty"
    else:
        print "Not empty %s" %list
check_list(emply_list)


