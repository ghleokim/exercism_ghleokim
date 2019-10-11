def distance(strand_a, strand_b):
    count = 0
    al, bl = len(strand_a), len(strand_b)
    if al != bl:
        raise ValueError(r".+")

    for i in range(al):
        if strand_a[i] != strand_b[i]:
            count += 1
    
    return count
