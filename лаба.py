with open("text.txt", encoding="utf-8") as f:
    prep = [',', ';', ':', '-', '\'', '\"', '(', ')', '—']
    predl = ['.', '!', '?']
    l, c, w, s, p, d, n = 1, 0, 0, 0, 0, 0, 0
    cw, cn = 0, 0
    t = ' '
    while t != '':
        t = f.read(1)
        if t == "\n":
            l += 1
        else:
            c += 1
        if t.isalpha():
            cw += 1
        elif t.isdigit():
            cn += 1
            d += 1
        elif t in prep:
            p += 1
        elif t in predl:
            s += 1
            p += 1
        if cw != 0 and not t.isalpha() and t != '-':
            w += 1
            cw = 0
        elif cn != 0 and not t.isdigit():
            n += 1
            cn = 0
    print(f"В тексте:\n{l} строк(и); {c - 1} символов; {w} слов; {s} предложений; {p} знаков препинания; {d} цифр; {n} чисел")