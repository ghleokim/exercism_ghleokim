def is_isogram(string):
    if not string: return True
    
    arr = [0 for _ in range(256)]
    for char in string:
        cur = ord(char.lower())
        if cur == 32 or cur == 45: continue
        elif arr[cur]: return False
        else: arr[cur] += 1
    
    return True