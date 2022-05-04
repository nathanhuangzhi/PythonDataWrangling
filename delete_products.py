import pandas as pd
def deleteProducts(id,n,m):
    id = pd.Series(id)
    op = id.value_counts().sort_values()
    del_count = 0
    del_list = []
    for i in op.index:
        del_count = del_count + op[i]
        if del_count > m:
            break
        del_list.append(i)

    return del_list, len(del_list)



id = [1,1,1,1,3,3,4,5]
n = 8
m = 2
print(deleteProducts(id,n,m))