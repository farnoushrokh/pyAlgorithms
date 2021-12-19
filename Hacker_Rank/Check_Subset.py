"""
You are given two sets,  A and B.
Your job is to find whether set A is a subset of B set .

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases,T .
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of A set .
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of B set .
"""


for _ in range(int(input())):
    T, A, M, B = input(), input().split(), input(), input().split()
    if set(A).issubset(set(B)):
        print(True)
    else:
        print(False)
