class Thing(object):
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self. weight = weight
    def value(self):
        return self.price / self.weight

def what_thing():
    thing_name,thing_price,thing_weight= input('请依次输入物品名称，价格，重量：').split()
    return thing_name,int(thing_price),int(thing_weight)

def main():
    max_weight,num_of_thing = map(int,input('请输入最大重量和物品数量：').split())
    all_things = []
    for _ in range(num_of_thing):
        all_things.append(Thing(*what_thing()))
        #这个地方我忘记了*， *表示有多个参数，what_thing()函数return 了 3个数字，需要用*表示多个
    all_things.sort(key =lambda x:x.value(),reverse=True)
    '''这里x是列表里面的实例，可以
    #调用对象的方法x.value。sort函数用法，（key: , reverse=) sort本身不接受参数''' 
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            total_weight += thing.weight
            total_price += thing.price
            print(f'拿走了{thing.name},价值{thing.price}元,目前总价值{total_price}元')
        else:
            continue
            '''请注意这里 break 和 continue 的区别
            '''
    print(f'今天这一波总共收获了{total_price}元')

main()
