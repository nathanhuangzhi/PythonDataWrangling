import numpy as np

unif_list = list(np.random.uniform(0, 1, 2))
list_max = max(unif_list)
list_2nd_max = min(unif_list)

while True:
    ll = np.random.uniform(0, 1, 1)[0]
    if ll >= list_max:
        list_2nd_max = list_max
        list_max = ll

    elif ll < list_max and ll >= list_2nd_max:
        list_2nd_max = ll
        print(list_max,list_2nd_max)
        print(unif_list)
        break
    else: pass

    unif_list.append(ll)

