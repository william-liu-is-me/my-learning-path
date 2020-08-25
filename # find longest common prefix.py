# find longest common prefix

def find_shortest(word_list):
    new_list = []
    for i in range(len(word_list)):
        new_list.append(len(word_list[i]))
    shortest = min(new_list)
    return shortest 

def find_prefix(shortest,word_list):
    prefix = ''
    for i in range(shortest):
        flag = False
        for j in range((len(word_list) - 1)):
            if word_list[j][i] != word_list[j+1][i]:
                flag = False
                break
            else:
                flag = True
        if flag:
            prefix += word_list[0][i]#
    print (prefix)

def main():
    word_list = ["flow","flower","flowght"]
    find_prefix(find_shortest(word_list),word_list)

if __name__ == '__main__':
    main()