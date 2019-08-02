def swap_unique_keys_values(d):
    new_d = {}
    for k, v in d.items():
        if v not in new_d:
            new_d[v] = k
        else:
            del(new_d[v])
    return new_d
