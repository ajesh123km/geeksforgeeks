def intersection(a, b):
    set_b = set(b)
    res = []
    seen = set()
    for x in a:
        if x in set_b and x not in seen:
            res.append(x)
            seen.add(x)
    return res

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersection(a, b)
print(" ".join(map(str, res)))
