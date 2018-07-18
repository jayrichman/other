##### Task-1 Generate list for sort [1,2,3,5,6,0,0,0] #####
list = [5,2,0,3,0,1,6,0]
list.sort(key=int)

list1 =  list[0:3]
list2 = list[3:]
list_end = list2 + list1
print list_end

##### Task2 - Generate list for sort [1,2,3,5,6,0,0,0] #####


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

##### Task3 - Concatenate the list values #####
my_list = ['p','r','o','b','e']

def con_word(list):
    word = ""
    ln = len(list)
    for key in range(ln):
        word += list[key]
    print word
con_word(my_list)

##### Task4 - Print quantity of values from the list which have the same value in [1:-1] #####    
count_str = ['abc', 'xyz', 'aba', '1221']

def len2(list):
    words = 0
    for i in list:
        if len(i) > 1 and i[0] == i[-1]:
            words += 1
    print words
len2(count_str)
##### Task5 - Remove dublicates from list #####
list_dublicates = [1,1,2,3,4,55,6,7,7,8]

def remove_dublicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print new_list

remove_dublicates(list_dublicates)
##### Task6 - Sort list by last element of tuple inside of list #####
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
##### Task7 - Empty List #####
emply_list = []
def check_list(list):
    if not list:
        print "List epty"
    else:
        print "Not empty %s" %list
check_list(emply_list)

##### Task8 - find the list of words that are longer than n from a given list of words #####


sentance = "Hello my name is Eugene"

def longer_then(n,str):
    word_len = []
    txt = str.split(" ")
    for i in txt:
        if len(i) > n:
            word_len.append(i)
    return word_len

print longer_then(1,sentance)

##### Task9 - removing the 0th, 4th and 5th elements #####

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

##### Task10 - Battleship Game #####
battleship =[
    [1,0,1,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,0],
]
print "COORDENATES WHRE THE SHIPS ARE:"


def find_ship(array):
    l = 1
    for i,k in enumerate(battleship):
        print ""
        print "X:Y LINE %s:"% l
        print ""
        l += 1
        for x,y in enumerate(battleship[i]):
            if y == 1:
                print ("%s:%s"% (x, i))
            else:
                print None
find_ship(battleship)

##### Task11 - Pig Latin Sentence #####


def pin_latin(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    new_sentence = ''
    cntr = 1
    for word in words:
        if word[0].lower() in vowels:
            word = word[1:] + word[0].lower()
        word += "ni" 'j'*cntr
        cntr += 1
        new_sentence += word + ' '
    return new_sentence.rstrip()


print pin_latin("Ello is the Youtube channel")

##### Task12 - Count Things in File #####
def count_words(path):
    with open(path) as f:
        count_strings = 0
        count_words = 0
        count_chars = 0
        for line in f:
            words = line.split()
            count_words += len(words)
            count_strings += 1
            count_chars += len(line)
        print count_strings
        print count_words
        print count_chars

##### Task13 - Concatenate dictionaries #####
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

dic = {}

for i in (dic1,dic2,dic3):
    dic.update(i)
print dic

##### Task14 - Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x) #####
n=int(input("Input a number: "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)

##### Task15 ##### 
string = "abcing"

def swipe(str):
    if len(str) > 2:
        if str[-3:] == 'ing':
            print str[0:3] + 'ly'
    elif len(str) > 3:
        print str + 'ing'
    elif len(str) < 3:
        print str 
swipe(string)

##### Task16 #####
def not_poor(str1):
  snot = str1.find('not')
  sbad = str1.find('poor')

  if sbad > snot:
    str1 = str1.replace(str1[snot:(sbad+4)], 'good')

  return str1
print(not_poor('The lyrics is not that poor!'))
##### Task17 Get pid of user from /etc/passwd #####
def get_userid(user):
    user_pid = {}
    with open('/etc/passwd') as f:
        for line in f:
            currentline = line.split(':')
            user_name = currentline[0].replace('_', "")
            user_id = (currentline[2:3])
            user_pid[user_name] = user_id
        for key, value in user_pid.items():
            if key == user:
                print str(value[0])
get_userid("root")

##### Task18 Print prime numbers ##### 


in_list = [ 1, 12, 131, 11, 17, 21 ,2143 ]
out_list = []

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return out_list.append(n)

            
out_list = []
for i in in_list:
     isprime(i)
    
print out_list



##### Task 19 Fibonacci ####
# recursion method

def fibonacci1(n):
      if n == 1 or n == 2:
         return 1
     return fibonacci1(n -1) + fibonacci1(n -2 )


for i in range(1,10):
     print (fibonacci1(i))
        
#loop method
def fibonacci2(n):
         a,b = 1,1
         for i in range(n-1):
             a,b = b, a + b
             print (a)
             return a
#generator method 
 def fibgen(num):
     a,b = 0,1
     for i in range(0, num):
         yield "{}: {}".format(i+1, a)
         a,b = b, a + b
for item in fibgen(10):
    print(item)
#### Task 20 FizzBuzz ####
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
        
### Task 21 Square the numbers. How to use list comprehensive ####
my_list = [1,2,3,4,5,6,7,8,9,10]
squared = [num*num for num in my_list]
print (squared)
