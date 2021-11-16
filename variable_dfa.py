import keyword
var_check = {
    0:{'a' : 2, 'h' : 1, 'o' : 2 },
    1:{'a' : 1, 'h' : 1, 'o' : 2 },
    2:{'a' : 2, 'h' : 2, 'o' : 2 },
}


def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        asc = ord(c)
        if asc in range(48,58):
            tok = 'a'
        elif asc in range(65,91):
            tok = 'h'
        elif asc in range(97,123):
            tok = 'h'
        elif asc == 95:
            tok = 'h'
        else:
            tok = 'o'
        state = transitions[state][tok]
    return state in accepting

while True:
    s = input()
    print(accepts(var_check, 0, {1}, s) and not (s in keyword.kwlist))
