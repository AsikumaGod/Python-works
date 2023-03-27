# This script print the highest even number
def highest(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item)
    return max(even)


print(highest([1, 2, 4, 6, 9, 4, 10, 23]))
