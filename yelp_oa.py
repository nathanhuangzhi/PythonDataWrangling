def rem_dup(rest_list):
    rest_list = set(rest_list)
    output = list(rest_list)
    return output


def split_input(rest_list):
    return [x.split(' - ') for x in rest_list]

def find_loc(sl, loc):

    output = []
    for i in sl:

        if i[1] == loc:

            output.append(i)

    return output

import collections
def aggre_sum(rl):
    rdict = collections.defaultdict(int)

    for i in rl:
        rdict[i[0]] += 1

    return rdict

def overrall_count(rest_list,loc):

    rest_list_nodup = rem_dup(rest_list)
    rest_list_split = split_input(rest_list_nodup)

    rest_list_inlocation = find_loc(rest_list_split,loc)

    summary_stat = aggre_sum(rest_list_inlocation)
    summary_list = summary_stat.items()
    output = []
    for i in summary_list:
        output.append(i[0]+' - '+ str(i[1]))

    return output



rest_input = ['Starbucks - Seattle - 101','Starbucks - Seattle - 101','Peets Coffee - San Francisco - 102',
              'Whole Foods - Austin - 103','Whole Foods - Austin - 104','Peets Coffee - Austin - 101']
print(overrall_count(rest_input,'Austin'))

print(('1'.isnumeric()))