#235 Lowest Common Ancestor of a Binary Search Tree
''' this is actually not 235 but a general method to solve such problem.
binary tree has the traits that left is always less than right, and right is 
larger than left. and there is no duplicate nodes on the tree.

but this algorithm doesnt consider these special situation.

the only issue for this algorithm is that if one num is the ancestor of the other,
they go back to the root, instead of itself. still working on this to resolve.
'''
class Binary_Tree():
    dict_of_nodes = dict()
    
    
    def __init__(self,value,obj= None):
        cls = type(self)
        self._value = value
        self._left = None
        self._right = None
        self._obj = obj
        cls.dict_of_nodes[self]=self._value
        
    @property
    def value(self):
        return self._value

    def set_left(self,value):
        cls = type(self)
        self._left = value
        return cls(value,self)

    def set_right(self,value):
        cls = type(self)
        self._right = value
        return cls(value,self)

    def find(self):
        return self._obj
        
    def find_ancs(self,other):
        if self.find() in other:
            return self.find().value
        else:
            return self.find().find_ancs(other)

start = Binary_Tree(6)
node_1 = start.set_left(2)
node_2 = start.set_right(8)
node_3 = node_1.set_left(0)
node_4 = node_1.set_right(4)
node_5 = node_2.set_left(7)
node_6 = node_2.set_right(9)
node_7 = node_4.set_left(3)
node_8 = node_4.set_right(5)


def create_path(obj,lst = list()):
    lst = list(lst)
    if obj.value != start.value:
        lst.append(obj.find())
        return create_path(obj.find(),lst)
    return lst
def find_common_ancestor(num_1,num_2,my_dict = Binary_Tree.dict_of_nodes):
    for k,v in my_dict.items():
        if v == num_1:
            path = create_path(k)
            for k,v in my_dict.items():
                if v == num_2:
                    return k.find_ancs(path)

print(find_common_ancestor(7,9))
