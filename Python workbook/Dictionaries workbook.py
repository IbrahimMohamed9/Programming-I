"""Task #1 First Solve"""
print("-" * 15)

def summdic(dict1, dict2, dict3):
    dict4 = {}
    for i in dict1:
        dict4[i] = dict1[i]
    for j in dict2:
        dict4[j] = dict2[j]
    for k in dict3:
        dict4[k] = dict3[k]
    return dict4

    
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
summdic(dic1, dic2, dic3) #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# -----------------------------------------------------------------------
"""Task #1 Second Solve"""
print("-" * 15)

def summdic(dict1, dict2, dict3):
    dict4 = {}
    for i in dict1:dict4.update({i:dict1[i]})
    """
    abbreviation for:
    for i in dict1:
        dict4.update({i:dict1[i]}) 
    """
    """
     The update() method:
     
    #The update() method: inserts the specified items to the dictionary.
    
    (The specified items can be a dictionary,
    or an iterable object with key value pairs).
    """
    for j in dict2:dict4.update({j:dict2[j]})
    for k in dict3:dict4.update({k:dict3[k]})
        
    return dict4

    
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
summdic(dic1, dic2, dic3) #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# -----------------------------------------------------------------------
"""Task #1 Third Solve"""
print("-" * 15)
def summdic(dict1, dict2, dict3):
    dict4 = {}
    for i in (dict1, dict2, dict3):dict4.update(i)
    """
    abbreviation for:
    for i in (dict1, dict2, dict3):  #I will take the first dictionary and add it
          dict4.update(i)                     after it second, etc
    """
    return dict4

    
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
summdic(dic1, dic2, dic3) #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# -----------------------------------------------------------------------
"""Task #2 First Solve"""
print("-" * 15)

def check(dict, n):
    if n in dict:return True
    """
    if n in dict:
        return True
    If element(n) in keys of dictionary 
    will go return True and if those are not
    equal will go to return False.
    """
    return False #you can add else but it is not important.

car = {"brand": "Ford","model": "Mustang","year": 1964}
print(check(car, "hi")) #False
print(check(car, "brand")) #True

# -----------------------------------------------------------------------
"""Task #2 Second Solve"""
print("-" * 15)

def check(dict, n):
    for i in dict:
        if i == n: return True
        """
        abbreviation for:
        if i == n:
            return True
        """
    return False #you can add else but it is not important.

car = {"brand": "Ford","model": "Mustang","year": 1964}
print(check(car, "hi")) #False
print(check(car, "brand")) #True

# -----------------------------------------------------------------------
"""Task #3 First Solve"""
print("-" * 15)

def iterate(dictt):
    return [i for i in dictt.items()]
    """
    abbreviation for:
    listt = []
    for i in dictt.items():
        listt.append(i)
    return listt
    """

names = {"first": "ibrahim","second": "fatima","third": "roqia"}
iterate(names)#[('first', 'ibrahim'), ('second', 'fatima'), ('third', 'roqia')]

# -----------------------------------------------------------------------
"""Task #3 Second Solve"""
print("-" * 15)

def iterate(dictt):
    list1 = [i for i in dictt.keys()]
    """
    abbreviation for:
    
    list1 = []
    for i in dictt.keys():
        list1.append(i)
    """
    list2 = [j for j in dictt.values()]
    """
    abbreviation for:
    
    list2 = []
    for j in dictt.values():
        list2.append(j)
    """
    list3 = [k for k in zip(list1, list2)] #zip will take the first element in the list1 with
                                                  #the first element in list2 in tuples
                                                                #etc
    """
    abbreviation for:
    
    list3 = []
    for k in zip(list1, list2):
        list3.append(k)
    """
    return list3


names = {"first": "ibrahim","second": "fatima","third": "roqia"}
iterate(names)#[('first', 'ibrahim'), ('second', 'fatima'), ('third', 'roqia')]

# -----------------------------------------------------------------------
"""Task #4 First Solve"""
print("-" * 15)

def generate(n):
    j = {}
    for i in range(1, n+1):j[i] = i*i
    """
    abbreviation for:
    
    j = {}
    for i in range(1, n+1):
        j[i] = i*i
    """
    return j

generate(5)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# -----------------------------------------------------------------------
"""Task #4 Second Solve"""
print("-" * 15)

def generate(n):
    j = {}
    for i in range(1, n+1):j.update({i:i*i})
    """
    abbreviation for:
    
    j = {}
    for i in range(1, n+1):
        j.update({i:i*i})
    """
    return j

generate(5)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# -----------------------------------------------------------------------
"""Task #5 First Solve"""
print("-" * 15)

def sumdic(n):
    sum = 0
    for i in n.values():sum += i
    """
    abbreviation for:
    
    for i in n.values():
        sum += 1
    """
    return sum

Numbers = {5:50,6:60, 7:70}
sumdic(Numbers) #180

# -----------------------------------------------------------------------
"""Task #5 Second Solve"""
print("-" * 15)

def sumdic(n):
    return sum(n.values())#The sum function returns the sum of the list.

Numbers = {5:50,6:60, 7:70}
sumdic(Numbers) #180

# -----------------------------------------------------------------------
"""Task #6 First Solve"""
print("-" * 15)

def mult(n):
    n1 = 1
    for i in n.values(): 
        n1 *= i
    return n1

mult({5:50,6:60, 7:70}) #210000

# -----------------------------------------------------------------------
"""Task #6 Second Solve"""
print("-" * 15)

import math
def mult(n):
    return math.prod(n.values())#The prod(product) function returns the product of the list.

mult({5:50,6:60, 7:70}) #210000

# -----------------------------------------------------------------------
"""Task #6 Third Solve"""
print("-" * 15)

from math import prod #now we can put prod without math.prod  :)
def mult(n):
    return prod(n.values())#The prod(product) function returns the product of the list.

mult({5:50,6:60, 7:70}) #210000

# -----------------------------------------------------------------------
"""Task #7 First Solve"""
print("-" * 15)

def remove(n, k):
    del n[k]
    return n

remove({5:50,6:60, 7:70}, 5) #{6:60, 7:70}

# -----------------------------------------------------------------------
"""Task #7 Second Solve"""
print("-" * 15)

def remove(n, k):
    dict = {}
    for i in n.keys():
        if i != k:
            dict[i] = n[i]
    return dict

remove({5:50,6:60, 7:70}, 5) #{6:60, 7:70}

# -----------------------------------------------------------------------
"""Task #8 First Solve"""
print("-" * 15)

def the_max_min(n):
    return "The maximum ", max(list(n.values())),"The minimum ", min(list(n.values()))
    """
    why did we put list?
    
    we put list() because we want convert the the 
    element from dict_values type to list type
    """
    """
    what is the max and min methods?
    
    min method returns the elements from the list with minimum value.
    max method returns the elements from the list with maximum value.
    """
            
    
dic = {'ite  m1': 1150, 'ite  m2': 300}
the_max_min(dic)#('The maximum ', 1150, 'The minimum ', 300)

# -----------------------------------------------------------------------
"""Task #8 Second Solve"""
print("-" * 15)

def the_max_min(n):
    m, mi = list(n.values())[0], list(n.values())[0] #we put list() because we want convert the
                                                          #the element from dict_values type
                                                                        #to list type
    """                                                              
    m = list(n.values())[0]
    mi = list(n.values())[0]
    """
    for i in n.values():
        if i > m: m = i
        if i < mi:mi = i
        """
        if i > m:
            m = i
        if i < mi:
            mi = i
        """
    return "The maximum ", m,"The minimum ", mi
     
            
    
dic = {'ite  m1': 1150, 'ite  m2': 300}
the_max_min(dic)#('The maximum ', 1150, 'The minimum ', 300)

# -----------------------------------------------------------------------
"""Task #9 First Solve"""
print("-" * 15)

def Counter(n1, n2):
    d = {}
    for i in n1: d.update({i:n1.get(i, 0) + n2.get(i, 0)})
    """
    abbreviation for:
    
    for i in n1:
        d[i] = n1.get(i, 0) + n2.get(i, 0)
    """
    for j in n2 :
        if j not in d: d.update({j: n2[j]}) #we took all keys in n1 and all common keys between 
                                                    #n2 and n1 now we want make sure all keys
                                                                #in n2 took
    """
    abbreviation for:

    if j not in d:
        d[j] = n2[j]
    """
    return d


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Counter(d2, d1)#{'a': 400, 'b': 400, 'd': 400, 'c': 300}

# -----------------------------------------------------------------------
"""Task #9 Second Solve"""
print("-" * 15)

def Counter(n1, n2):
    listKeys1 = [i for i in n1.keys()]
    """
    abbreviation for:
    
    listKeys1 = []
    for i in n1.keys():
        listKeys1.append(i)
    """
    listKeys2 = [j for j in n2.keys()]
    """
    abbreviation for:
    
    listKeys2 = []
    for j in n2.keys():
        listKeys2.append(j)
    """
    commonKeys = set(listKeys1).intersection(listKeys2)
    dic = {}
    for k in commonKeys:
        dic[k] = n1[k] + n2[k]
    listKeys3 = [m for m in listKeys1 + listKeys2]
    """
    abbreviation for:
    
    listKeys3 = []
    for m in listKeys1 + listKeys2:
        listKeys3.append(m)
    """
    listKeys4 = [q for q in listKeys3 if q not in commonKeys]
    """
    abbreviation for:
    
    listKeys4 = []
    for q in listKeys3:
        if q not in commonKeys:
            listKeys4.append(q)
    """
    for r in listKeys4:
        dic.update({r:n1.get(r, 0) + n2.get(r, 0)})
#      same  dic[r] = n1.get(r, 0) + n2.get(r, 0)
    return dic

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Counter(d2, d1)#{'a': 400, 'b': 400, 'd': 400, 'c': 300}

# -----------------------------------------------------------------------
"""Task #9 Third Solve"""
print("-" * 15)

from collections import Counter

def counter(d1, d2):
    return Counter(d1) + Counter(d2)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
counter(d2, d1)#{'a': 400, 'b': 400, 'd': 400, 'c': 300}

# -----------------------------------------------------------------------
"""Task #10 First Solve"""
print("-" * 15)

def uniq(n):
    listt = []
    for i in n:
        for j in i.values():
            if j not in listt:
                listt.append(j)
    return listt
    

uniq([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
      {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])
#['S001', 'S002', 'S005', 'S009', 'S007']

# -----------------------------------------------------------------------
"""Task #10 Second Solve"""
print("-" * 15)

def uniq(n):
    return set(j for i in n for j in i.values())
#Set type no duplicate members we can use it when we want to delete duplicates members.
    """
    abbreviation for:
    
    n1 = []
    for i in n:
        for j in i.values():
            n1.append(j)
    return set(n1)
    """
uniq([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
      {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])
#{'S002', 'S005', 'S007', 'S001', 'S009'}

# -----------------------------------------------------------------------
"""Task #11 First Solve"""
print("-" * 15)

def combinations(dict):
    listvalues = list(dict.values())
    listvalues1 = listvalues[0]
    listvalues2 = listvalues[1]
    listvalues3 = [i+j for i in listvalues1 for j in listvalues2]
    """
    abbreviation for:
    
    listvalues3 = []
    for i in listvalues1:
        for j in listvalues2:
            listvalues3.append(i+j)
    """
    return listvalues3
        
combinations({'1':['a','b'], '2':['c','d']}) #['ac', 'ad', 'bc', 'bd']

# -----------------------------------------------------------------------
"""Task #11 Second Solve"""
print("-" * 15)

def combinations(n):
    n1 = n.copy()
    n2 = []
    for i in n:
        del n1[i]
        for j in n1:
            for k in range(len(n[i])):
                for q in range(len(n1[j])):
                    n2.append(n[i][k] + n1[j][q])
    return n2
    
    
combinations({'1':['a','b'], '2':['c','d']}) #['ac', 'ad', 'bc', 'bd']

# -----------------------------------------------------------------------
"""Task #12"""
print("-" * 15)

def counter(n):
    z = [j for i in n for j in i.values()]
    """
    abbreviation for:
    
    z = []
    for i in n:
        for j in i.values():
            z.append(j)
    """
    z1, d = [(z[a-1],z[a]) for a in range(1, len(z), 2)], {}
    """
    abbreviation for:
    
    z1 = []
    for a in range(1, len(z1), 2):
        z1.append((z1[a-1],z1[a]))
    d = {}
    """
    for k in z1:d.update({k[0]:k[1] + d.get(k[0], 0)})
    """
    abbreviation for:
    
    for k in z1:
        d[k[0]] = k[1] + d.get(k[0], 0)
    """
    return d

x = [{'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
counter(x) #{'item1': 1150, 'item2': 300}


# -----------------------------------------------------------------------
"""Task #13 First Solve"""
print("-" * 15)

def remove_space(dict):
    dict1, z = {},[]
    """
    abbreviation for:
    
    dict1 = {}
    z = []
    """
    for i in dict:
        strr = ""
        for j in i:
            if j != " ":
                strr += j
        dict1[strr] = dict[i]
    return dict1
    
        

remove_space({'ite  m1': 1150, 'ite  m2': 300})#{'item1': 1150, 'item2': 300}

# -----------------------------------------------------------------------
"""Task #13 Second Solve"""
print("-" * 15)

def remove_space(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[key.replace(" ", "")] = value 
        #The replace() method replaces a specified phrase with another specified phrase.
    return new_dict

remove_space({'ite  m1': 1150, 'ite  m2': 300})#{'item1': 1150, 'item2': 300}

# -----------------------------------------------------------------------
"""Task #14 First Solve"""
print("-" * 15)
def find(x, y):
    for (key, value) in x.items():
        for (key1, value1) in y.items():
            if (key, value) == (key1, value1):
                print('{0}: {1} is present in both x and y'.format(key, value))

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
find(x, y) #key1: 1 is present in both x and y


# -----------------------------------------------------------------------
"""Task #14 Second Solve"""
print("-" * 15)

def find(dic1, dic2):
    z = [i for i in dic1 if i in dic2]
    """
    abbreviation for:
    
    z = []
    for i in dic1:
        if i in dic 2:
            z.append(i)
    """
    z1 = [[b, dic1[b]] for b in z if dic1[b] == dic2[b]]
    """
    abbreviation for:
    
    z1 = []
    for b in z:
        if dic1[b] == dic2[b]:
            z1.append((b, dic1[b]))
    """
    for j in range(len(z1)):print(str(z1[j][0]) + ": " + str(z1[j][1]) + " is present in both x and y")
    """
    abbreviation for:
    
    for j in range(len(z1)):
        print(str(z1[j][0]) + ": " + str(z1[j][1]) + " is present in both x and y")
    """
    
    
x, y = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
find(x, y) #key1: 1 is present in both x and y

# -----------------------------------------------------------------------
"""Task #15 First Solve"""
print("-" * 15)

def filter_even(dict1):
    new_dict = {}
    for i in dict1:
        new_dict[i] = [j for j in dict1[i] if j % 2 == 0]
        """                 ""
                            abbreviation for:
                            
                        for i in dic1:
                            z = []
                            for j in dict1[i]:
                                if j % 2 == 0:
                                    z.append(j)
                            dic1[i] = z
        """                  ""
    return new_dict 
    
print(filter_even({'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}))
#{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
print(filter_even({'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}))
#{'V': [], 'VI': [], 'VII': [2]}

# -----------------------------------------------------------------------
"""Task #15 Second Solve"""
print("-" * 15)

def filter_even(dic1):
    dic2 = {}
    for i in dic1:dic2.update({i:[j for j in dic1[i] if j % 2 == 0]})
    """
    abbreviation for:
    
    dic2= {}
    for i in dic1:
        z = []
        for j in dic1[i]:
            if j % 2 == 0:
                z.append(j)
        dic2[i] = z
    return dic2
    """
    return dic2
    
    
print(filter_even({'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}))
#{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
print(filter_even({'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}))
#{'V': [], 'VI': [], 'VII': [2]}

# -----------------------------------------------------------------------
"""Task #16 First Solve"""
print("-" * 15)

def find_len(d):
    sum = 0
    for i in d.values():
        sum += len(i)
    return sum
    
d = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
find_len(d) #20

# -----------------------------------------------------------------------
"""Task #16 Second Solve"""
print("-" * 15)

def find_len(d):
    return len([j for i in d.values() for j in i])
    """
    abbreviation for:
    
    z = []
    for i in d.values():
        for j in i:
            z.append(j)
    m = len(z)
    return m
    """
    
d = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
find_len(d) #20


# -----------------------------------------------------------------------
"""Task #17 First Solve"""
print("-" * 15)

def find(d):
    return list(d.keys()) #we wrote list bacause we want convert the type from dict_keys
                                                #to list

find({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20})
#['Theodore', 'Roxanne', 'Mathew', 'Betty']

# -----------------------------------------------------------------------
"""Task #17 Second Solve"""
print("-" * 15)

def find(d):
    return [i for i in d]
    '''
    abbreviation for:
    
    j = []
    for i in d:
        j.append(i)
    return j
    '''

find({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20})
#['Theodore', 'Roxanne', 'Mathew', 'Betty']

# -----------------------------------------------------------------------
"""Task #18 First solve"""
print("-" * 15)

def find(d):
    return list(d.values())#we wrote list bacause we want convert the type from dict_values
                                                #to list
    """
    abbreviation for:
    
    z = []
    for i in d.values():
        z.append(i)
    return z
    """
find({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20})#[19, 20, 21, 20]

# -----------------------------------------------------------------------
"""Task #18 Second Solve"""
print("-" * 15)

def find(d):
    return [i for i in d.values()]
    """
    abbreviation for:
    
    z = []
    for i in d.values():
        z.append(i)
    return z
    """
find({'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20})#[19, 20, 21, 20]

# -----------------------------------------------------------------------
"""Task #19 First Solve"""
print("-" * 15)

def find(n):
    minn, maxx = min(list(n.values())), max(list(n.values()))
    """
    abbreviation for:
    
    minn = min(list(n.values()))
    maxx = max(list(n.values()))
    """
    return [j for j in n if n[j] == minn or n[j] == maxx]
    """
    abbreviation for:
    
    lst = []
    for j in n:
        if n[j] == minn or n[j] == maxx:
            lst.append(j)
    return lst
    """

find({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})#['Theodore', 'Roxanne']

# -----------------------------------------------------------------------
"""Task #19 Second Solve"""
print("-" * 15)

def find(n):
    minn, maxx = min([i for i in n.values()]), max([i for i in n.values()])
    """
    abbreviation for:
    
    lst = []
    for i in n.values():
        lst.append()
    minn = min(lst)
    max = max(lst)
    """
    return [j for j in n if n[j] == minn or n[j] == maxx]
    """
    abbreviation for:
    
    lst1 = []
    for j in n:
        if n[j] == minn or n[j] == maxx:
            lst1.append(j)
    return lst1
    """

find({'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20})
#['Theodore', 'Roxanne']

# -----------------------------------------------------------------------
"""Task #20 First Solve"""
print("-" * 15)

def find(d):
    return list(d.items()) #we wrote list bacause we want convert the type from dict_items
                                                #to list
    
find({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4})
#[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

# -----------------------------------------------------------------------
"""Task #20 Second Solve"""
print("-" * 15)

def find(d):
    return [i for i in d.items()]
    """
    abbreviation for:
    
    z = []
    for i in d.items():
        z.append(i)
    return z
    """
find({'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4})
#[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

# -----------------------------------------------------------------------
"""Task #21 First Solve"""
print("-" * 15)

def find(list1, list2):
    dict = {}
    if len(list1) > len(list2):
        list1=list1[:len(list2)]
    elif len(list1) < len(list2):
        list2 = list2[:len(list1)]
        
    for i in range(len(list1)):
        dict.update({list1[i]:list2[i]})
    return dict
    

find(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# -----------------------------------------------------------------------
"""Task #21 Second Solve"""
print("-" * 15)

def find(n1, n2):
    d, c = {}, 0
    for i in n1:
        d.update({i:n2[c]})
        c += 1
        if len(n2) == c:
            break
    return d     

find(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# -----------------------------------------------------------------------
"""Task #22 First Solve"""
print("-" * 15)

def mostright(d):
    for i in d:
        d[i] = int(str(d[i])[-1]) #we convert it from integer to string because we 
                                    #want use index -1 and return it integer again.
    """
    abbreviation for:
    
    for i in d:
        d.update({i:int(str(d[i])[-1])})
    return d
    """
    return d

dictt = {"qw": 45, "en":1334, "fro": 774, "klo": 223}

mostright(dictt)#{'qw': 5, 'en': 4, 'fro': 4, 'klo': 3}

# -----------------------------------------------------------------------
"""Task #22 Second Solve"""
print("-" * 15)

def mostright(d):
    for i in d:d.update({i:int(str(d[i])[-1])})#we convert it from integer to string because we 
                                                #want use index -1 and return it integer again.
    """
    abbreviation for:
    
    for i in d:
        d.update({i:int(str(d[i])[-1])})
    return d
    """
    return d

dictt = {"qw": 45, "en":1334, "fro": 774, "klo": 223}

mostright(dictt)#{'qw': 5, 'en': 4, 'fro': 4, 'klo': 3}


# -----------------------------------------------------------------------
"""Task #23 First Solve"""
print("-" * 15)

def dubled(dictt):
    z = [i for i in dictt.values() if i < 14]
    """
    abbreviation for:
    
    z = []
    for i in dictt.values():
        if i < 14:
            z.append(i)
    """
    for j in dictt:
        if dictt[j] in z:
            dictt[j] = dictt[j]*2
    return dictt

dictt = {"for": 4, "hi": 14, "hallow": 13}
dubled(dictt)#{'for': 8, 'hi': 14, 'hallow': 26}

# -----------------------------------------------------------------------
"""Task #24 Second Solve"""
print("-" * 15)

def dubled(dictt):
    for j in dictt:
        if dictt[j] < 14:
            dictt[j] = dictt[j]*2
    return dictt

dictt = {"for": 4, "hi": 14, "hallow": 13}
dubled(dictt)#{'for': 8, 'hi': 14, 'hallow': 26}

# -----------------------------------------------------------------------
"""Task #24 First Solve"""
print("-" * 15)

def dubled(dictt):
    z = [i for i in dictt.values() if i < 9]
    """
    abbreviation for:
    
    z = []
    for i in dictt.values():
        if i < 9:
            z.append(i)
    """
    for j in dictt:
        if dictt[j] in z:
            dictt[j] = dictt[j]*2
    return dictt

dictt = {"for": 4, "hi": 14, "hallow": 13}
dubled(dictt) #{'for': 8, 'hi': 14, 'hallow': 13}

# -----------------------------------------------------------------------
"""Task #24 Second Solve"""
print("-" * 15)

def dubled(dictt):
    for j in dictt:
        if dictt[j] < 9:
            dictt[j] = dictt[j]*2
    return dictt

dictt = {"for": 4, "hi": 14, "hallow": 13}
dubled(dictt)##{'for': 8, 'hi': 14, 'hallow': 13}


#line number 1000 :)