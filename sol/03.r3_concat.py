def concat(lists):
    out = []
    for entry in lists:
        for x in entry:
            out.append(x)
    return out
