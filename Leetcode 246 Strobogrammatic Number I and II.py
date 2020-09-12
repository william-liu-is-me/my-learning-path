# 246 Leetcode Strobogrammatic Number I, II

class Strobogrammatic_num():
    def __init__(self,num):
        self.num = num
    @property
    def SN_method(self):
        if self.num == 1:
            return 1
        elif self.num == 6:
            return 9
        elif self.num == 8:
            return 8
        elif self.num == 9:
            return 6
        elif self.num == 0:
            return 0
    

def find_SN_num(num:int):
    lst = []
    new_lst = []
    for _ in str(num):
        lst.append(int(_))
    if 2 in lst or 3 in lst or 4 in lst or 5 in lst or 7 in lst:
        return False,'some numbers are not able to be SN'
    else:
        for _ in lst:
            new_lst.insert(0,str(Strobogrammatic_num(_).SN_method))
    num_2 = int(''.join(new_lst))
    if num_2 == num:
        return True
    return False,f'after SN:{num_2}, does not match {num}'
#print (find_SN_num(96))




#===========================================================================

class Strobogrammatic_num():
    def __init__(self,num):
        self.num = num
    @property
    def SN_method(self):
        if self.num == 1:
            return 1
        elif self.num == 6:
            return 9
        elif self.num == 8:
            return 8
        elif self.num == 9:
            return 6
        elif self.num == 0:
            return 0


def find_SN_num_within_N(Num):
    range_of_test = 10**Num
    potential_SN = []
    
    final_set = set()
    for _ in range(range_of_test):
        if '2' in str(_) or '3' in str(_) or '4' in str(_) or '5' in str(_) or '7' in str(_):
            continue
        else:
            potential_SN.append(_)  
    for i in potential_SN:
        new_lst=[] 
        for j in str(i): 
            new_lst.insert(0,str(Strobogrammatic_num(int(j)).SN_method))
            num_2 = int(''.join(new_lst))
            if num_2 == i:
                final_set.add(i)
    return final_set
from time import time
start = time()
re = find_SN_num_within_N(7)

end = time()
print (end - start)

#code before optimazation
#=============================================================================
#code after optimazation


def find_2(n):
    lst=[]
    if '2' in str(n):
        for i in str(n):
            lst.append(int(i))
        for i in range(len(lst)):
            if lst[i] == 2:
                return 4*10 ** (len(str(n))-1-i)
    elif '7' in str(n):
        for i in str(n):
            lst.append(int(i))
        for i in range(len(lst)):
            if lst[i] == 7:
                return 10**(len(str(n))-1-i)
    else:
        return 1

class my_iter():
    def __init__(self,start,end):
        self.a = start
        self.b = end
        #self.func = func

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            self.a += find_2(self.a)
            return self.a
        else:
            raise StopIteration



class Strobogrammatic_num():
    def __init__(self,num):
        self.num = num
    @property
    def SN_method(self):
        if self.num == 1:
            return 1
        elif self.num == 6:
            return 9
        elif self.num == 8:
            return 8
        elif self.num == 9:
            return 6
        elif self.num == 0:
            return 0


def find_SN_num_within_N(Num):
    range_of_test = my_iter(1,10**Num)
    final_lst = []
    for _ in range_of_test:
        if '2' in str(_) or '3' in str(_) or '4' in str(_) or '5' in str(_) or '7' in str(_):
            continue
        else:
            new_lst= []
            for j in str(_): 
                new_lst.insert(0,str(Strobogrammatic_num(int(j)).SN_method))
                num_2 = int(''.join(new_lst))
                if num_2 == _:
                    final_lst.append(_)
    return final_lst

from time import time
start = time()
re = find_SN_num_within_N(7)
#print (re)
end = time()
print (end - start)


