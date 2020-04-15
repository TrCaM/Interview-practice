"""
This file includes all convenient basic function for bit manipulation
"""


def setBit(A, i):
    return A | (1 << i)


A = int("0b1100", base=0)
print(bin(setBit(A, 1)))  # 1110


def clearBit(A, i):
    return A & ~(1 << i)


print(bin(clearBit(A, 2)))  # 1000


def extractLastBit(A):
    return A & -A


print(bin(extractLastBit(A)))  # 100


def removeLastBit(A):
    return A & (A - 1)


print(bin(removeLastBit(A)))  # 1000


def isPowerOfFour(self, num: int) -> bool:
    return not (num & (num -1)) and (num & 0x55555555)
