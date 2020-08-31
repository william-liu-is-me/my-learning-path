#Excel Sheet Column Title


my_key = range(1,27)
my_value = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
my_dict = dict(zip(my_key,my_value))
num = 12345678912346578912346579
base = 26
#listA = []
result=''
while True:
    result = my_dict[num%base] + result
    #listA.insert(0,num%base)
    num = num//base
    if num < 26:
        result = my_dict[num] + result
        break
#for i in range(len(listA)):
#    result += my_dict[listA[i]]
print (result)
'''comment:I am not familiar with chr(), nor the number for A-Z. so I create a dict myself.
the code in while loop is learned from the code below. creating a list to store each num
is not necessary.
'''



#
'''code from the website'''
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ""
        
        #convert decimal number to a 26-base number
        while n > 0:
            n -= 1
            letter = n % 26
            n = n // 26
            #convert number to letter
            title = chr(letter + 65) + title
            
        return title#

S = Solution()
print (S.convertToTitle(12345678912346578912346579))#

'''