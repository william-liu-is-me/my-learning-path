#Nested List Weight Sum


lst = [1,[4,[6]],[1]]

def getsum(lst):
    result = 0
    depth = 1
    while lst:
        new_lst =[]
        result += depth * sum([i for i in lst if type(i) == type(int())])
        for i in lst:
            if type(i) != type(int()):
                new_lst += i
        depth += 1
        print (new_lst)
        lst = new_lst
    return result
print (getsum(lst))