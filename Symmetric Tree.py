'''Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
   1
   / \
  2   2
 / \ / \
3  4 4  3
'''

old_list = [1,2,2,'null',3,3,'null']
#print (len(a))
import math

flag = False
#print (int(s))
'''this is to determine if the binary list is a binary tree
'''
for i in range(int(math.log2(len(old_list))),int(math.log2(len(old_list))+1)+1):
    if 2**i - 1 == len(old_list):
        lvl_of_i = i
        flag_2 = True
        '''this is to check weather it is a symmetric)
        I slice each layer to make it as new list, and compare the element from
        each new list
        eg. [a,b,b,a]
            [a,b,c,d,d,c,b,a]
        '''
        for i in range(1,lvl_of_i):
            new_list = old_list[2**i-1:2**(i+1)-1]
            for j in range(int(len(new_list)/2)):
                if new_list[j] != new_list[(2**i)-1-j]:
                    
                    flag_2 = False
                    break
            if not flag_2:
                break
        if flag_2:
            print('it is symmetric tree')
            flag = True

if not flag:
    print('not symmetric tree')
