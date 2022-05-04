import collections
def finder(arr1, arr2):
    c = collections.defaultdict(int)

    for i in arr2:
        c[i] += 1

    for j in arr1:

        if c[j] == 0:
            return j

print(finder([1,2,3,4,5,6,7],[1,2,3,4,6,7]))
