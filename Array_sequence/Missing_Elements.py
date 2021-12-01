"""
# Find the Missing Element

## Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

    5 is the missing number
"""
def missing_element(a, b):
    missing_number = list()
    if len(a)> len(b):
        for i in a:
            if i not in b:
                missing_number.append(i)
            elif len(a) < len(b):
                for j in b:
                    if j not in a:
                        missing_number.append(j)
        print(missing_number)
    else:
        print('Two arrays are the same')



import collections

def finder(arr1, arr2):
    all_elms = dict()
    all_elms2 = dict()
    for el in sorted(arr1):
        if el not in all_elms.keys():
            all_elms[el] = 1
        else:
            all_elms[el] += 1

    for el in sorted(arr2):
        if el not in all_elms2.keys():
            all_elms2[el] = 1
        else:
            all_elms2[el] += 1

    for el in all_elms.keys():
        if el not in all_elms2.keys():
            print(el)
        else:
            if all_elms[el] != all_elms2[el]:
                print(el)


# collections Dictionary solution
def finder_4(arr1, arr2):
    all_elms2 = collections.defaultdict(int)

    for el in arr2:
        all_elms2[el] += 1

    for el in arr1:
        if all_elms2[el] == 0:
            return el
        else:
            all_elms2[el] -= 1


def finder2(arr1, arr2):
    for i in range(len(arr1)):
        if sorted(arr1)[i] != sorted(arr2)[i]:
            print(sorted(arr1)[i])
            break


def finder3(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for el1, el2 in zip(arr1, arr2):
        if el1 != el2:
            return el1
    return arr1[-1]


# Exclusive OR solution
def finder5(arr1, arr2):
    res = 0
    for el in arr1+arr2:
        # print("{} XOR {} = ".format(res, el))
        res ^= el
        # print(res)

    return res
