
from collections import Counter
from itertools import permutations

def Find_Palin(strs):
    if len(strs) % 2 == 0 and len(strs) != 0:
        return check_even_pali(strs)
    return check_odd_pali(strs)
'''the Algorithm consider two situations: even or odd strs'''
'''this is for even'''
def check_even_pali(strs):
    my_dict = dict(Counter(strs))
    for k,v in my_dict.items():
        if v % 2 != 0:
            return f'due to {k}, this is not a palidrome'
        else:
            return find_even_pali(strs)

def find_even_pali(strs):
    my_dict = dict(Counter(strs))
    my_lst = []
    for k,v in my_dict.items():
        for i in range(int(v/2)):
            my_lst.append(k)
    '''range(int(v/2)): the idea is we only need to find the permutation for 
    first half of the str.
    '''
    new_set = set(list(permutations(my_lst,len(my_lst))))
    '''the idea for using set is to remove duplicate,(it is very costly for memory in this Algorithm,
    but this is what i can think of now.
    duplicate means: for eg. aab. Actually there is only aab aba baa, but permutation function considers two a
    as different a, it will return aab aab aba aba baa baa, which is not correct. 
    '''
    new_lst2 = list(new_set)
    final_lst = []
    for i in new_lst2:
        i += i[::-1]
    '''#this is where we add the second half to first half, to make it as one complete
    str. '''
    
    final_lst.append(i)
    result =[]
    for i in final_lst:
        strs = ''.join(i)
        result.append(strs)
    #this is where we make the list back to str ''.join()
    return result
'''this is for odd below'''

def check_odd_pali(strs):
    my_dict = dict(Counter(strs))
    counter = 0
    records =''
    #odd strs in order to be palin, it must have 1 and only 1 odd letter, that
    #letter will be in the middle. eg. aba, b must b in the middle. acacb: b must 
    #be in the middle. abace: no way to be palin. 
    
    for k,v in my_dict.items():
        if v % 2 != 0:
            counter += 1
            records += k
    if counter == 1:
        return find_odd_pali(strs,records)
    #check if only 1 odd letter exist
    else:
        return f'this is not pali due to {records}'  

def find_odd_pali(strs,records):
    my_dict = dict(Counter(strs))
    my_dict[records] -= 1
    my_lst = []
    for k,v in my_dict.items():
        for i in range(int(v/2)):
            my_lst.append(k)
    new_set = set(list(permutations(my_lst,len(my_lst))))
    new_lst2 = list(new_set)
    final_lst = []
    for i in new_lst2:
        i += i[::-1]
        i = list(i)
    #i was tuple, immutable data
        i.insert(int(len(i)/2),records)
    #insert the letter in the mid
        final_lst.append(i)
    result =[]
    for i in final_lst:
        strs = ''.join(i)
        result.append(strs)
    return result



strs = 'abace'

result = Find_Palin(strs)

print (result)
