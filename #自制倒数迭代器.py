#自制倒数迭代器


from time import sleep

class count_down(object):
    def __init__(self,the_list):
        self.index = len(the_list) 
        self.item = the_list
    def __iter__(self):
        return self
    def __next__(self):
        self.index = self.index - 1
        if self.index >=0:
            sleep (1)
            return self.item[self.index]
            
        else:
            raise StopIteration
