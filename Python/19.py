def f(st):
    sl = st.lower().split()
    wors = {}
    for i in sl:
        if i in wors:
            wors[i] += 1
        else:
            wors[i] = 1
    return wors

a = input()
print(f(a))