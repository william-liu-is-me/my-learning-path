#test

'''idea of this code:
learn the idea of the code below online, but i dont think that is very simple and
clear. so I made some updates.

1. I use try except to capture the TypeError when these is no instance below nodes.
this also means that the num I am looking for doesnt exist in the tree.

2. I create a dict to store the differece of k and the node. 
the difference is the key, the node is the value.
later on I can just min() the dict.keys() to find the smallest different, and then
find the value(which is the node)

however, there is one issue in this code: if there are 2 nodes the same difference
to K, the code can only return 1 node. as the dict wil replace the value if key exist.

'''
class Binary_tree():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

    def find_k(self,k,my_dict=dict()):

        try:
            if self.value == k:
                return self.value
            elif self.value > k:
                my_dict[abs(self.value-k)]=self.value
                return self.left.find_k(k,my_dict)
            elif self.value < k :
                my_dict[abs(self.value-k)]=self.value
                return self.right.find_k(k,my_dict)
        except Exception:
            result = f'{k} doesnt exist in the tree, but the closest value to {k} is {my_dict[min(my_dict.keys())]},the difference is {min(my_dict.keys())}。'
            return result



root = Binary_tree(15)
root.left=Binary_tree(3)
root.right = Binary_tree(30)
root.left.left = Binary_tree(1)
root.right.left= Binary_tree(25)
root.left.right = Binary_tree(10)


print (root.find_k(16))

