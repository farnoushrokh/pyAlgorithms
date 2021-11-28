"""# Anagram Check

## Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written
using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"

**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**"""

def anagram(sentence1, sentence2):
    sen1_dict= {}
    sen2_dict= {}
    for el in sentence1.replace(" ",""):
        sen1_dict[el] = sen1_dict.get(el, 0)+1
    for el in sentence2.replace(" ",""):
      sen2_dict[el] = sen2_dict.get(el, 0)+1
    #check the lendth of sentences
    if len(sentence1.replace(" ","")) == len(sentence2.replace(" ","")):
        if sen1_dict == sen2_dict:
            return True
        else:
            return False
    else:
        return False


def anagram_check(str1, str2):
    lst1 = [el for el in str1.lower().replace(" ", "")]
    lst2 = [el for el in str2.lower().replace(" ", "")]
    if sorted(lst1) == sorted(lst2):
        return "YES"
    return "NO"