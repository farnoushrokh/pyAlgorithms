# Array Pair Sum

"""Problem

Given an integer array, output all the ** *unique* ** pairs that sum up to a specific value **k**.

So the input:

    pair_sum([1,3,2,2],4)

would return **2** pairs:

     (1,3)
     (2,2)

**NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS**"""


def unique_pairs(lst, num):
    final_answer = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == num:
                if (lst[i], lst[j]) not in final_answer:
                    final_answer.append((lst[i], lst[j]))
    return final_answer


print(unique_pairs(lst=[1, 3, 2, 4, 4], num=5))

