"""
# String Compression

## Problem

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem,
you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1'
even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""

#First algorithm
def compress_str(string):
    lst = list()
    dict_ = dict()
    new_ = []
    for i in string.replace(' ', ''):
        if i not in lst:
            dict_[i] = string.count(i)

    for key, value in dict_.items():
        temp = [key, value]
        new_.append(temp)

    # convert list of lists to a list
    lst_final = []
    for i in new_:
        for j in i:
            lst_final.append(str(j))
    final = "".join(new for new in lst_final)
    return final

#Second algorithm
def compression(str_s):
    removeSpace = ''.join(str_s.split())
    unique_els = dict()
    for i in range(len(removeSpace)):
        if removeSpace[i] not in unique_els.keys():
            unique_els[removeSpace[i]] = 1
        else:
            unique_els[removeSpace[i]] += 1
    final_str = ''
    for i in range(len(unique_els.keys())):
        final_str += str(list(unique_els.keys())[i]) + str(list(unique_els.values())[i])

    return final_str