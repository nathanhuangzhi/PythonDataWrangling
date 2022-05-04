def pair_sum(pair, K):
    seen = set()
    output = set()

    for i in pair:

        target = K - i

        if target not in seen:

            seen.add(target)

        if target in pair:

            output.add((min(target,i),max(target,i)))

    print(output)

pair_sum({1,2,3,2},4)
