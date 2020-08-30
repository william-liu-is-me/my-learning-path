#Intersection of Two Linked Lists

class solution():
    def __init__(self,list_A,list_B):
        self.list_A = list_A
        self.list_B = list_B
    @property
    def find_tail(self):
        if len(self.list_A) > len(self.list_B):
            self.list_A, self.list_B = self.list_B, self.list_A
        #list_B is always longer
        i = 1
        tail = []
        if len(self.list_A) <= 1:
            return 'null'
        else:
            while i < len(self.list_A):#for i in range(len(list_A),0,-1):
                if self.list_A[-1 * i] != self.list_B[-1 * i]:
                    return 'null'
                    break
                else:
                    tail.insert(0,self.list_A[-1*i])
                i += 1
            return tail

list_A = [5,4,5]
list_B = [5,6,1,8,4,5]
x = solution(list_A,list_B)
print (x.find_tail)
