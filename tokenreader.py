
import keyword
trans_table = {
    'start':{'a' : 'buang', 'h' : 'var', 'o' : 'buang', 'k' : 'awalstr'},
    'var':{'a' : 'var', 'h' : 'var', 'o' : 'buang','k' : 'buang'},
    'buang':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'buang' },
    'awalstr':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x2' },
    'str6x2':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'akomen' },
    'akomen':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr4' },
    'failstr4':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr5' },
    'failstr5':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x' },
    'str6x':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr7' },
    'failstr7':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x2' }
}

wrong_string_state = ['buang', 'failstr4', 'failstr5', 'failstr7']
valid_symbols = ['print','+','-','*','/','//','%', '**','=','+=','-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=','>>=','<<=','==','!=', '>','<', '>=','<=','&','|','^','~','<<','>>',':','(',')','[',']','{','}']
def dfa(transitions,initial,s):
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
        elif asc == 34 or asc == 39:
            tok = 'k'
        else:
            tok = 'o'
        state = transitions[state][tok]
    return state

with open("input.py",'r') as f:
    lines = f.readlines()
    words = ""
    brack = ['[',']', '(', ')', ',', "#", '{', '}', ':', '~']
    ops = ['/', '*', '+', '-', '=', '|', '&', '<', '>', '!']
    bef = False #Periksa ada ops sebelumnya
    kutbool1 = False
    kutbool2 = False
    for line in lines:
        for char in line:
            if char == "'" :
                if kutbool1 == False :
                    words += (" " + char)
                    kutbool1 = True
                else :
                    words += char
            elif char == '"' :
                if kutbool2 == False :
                    words += (" " + char)
                    kutbool2 = True
                else :
                    words += char
            else :
                if kutbool1 == True or kutbool2 == True: words += " "
                kutbool1, kutbool2 = False, False
                if char in brack :
                    words += (" " +char+" ")
                elif char in ops:
                    if bef == True :
                        words += char
                    else :
                        words+=(" " + char)
                        bef = True
                elif char == '\n':
                    words += " " + "\\n" + " "
                else :
                    if bef == True:
                        words += " " + char
                        bef = False
                    else : words+= char
    Tokens = words.split()

    #print(Tokens)
    StartKomen2 = False
    StartKomen1 = False
    newTokens = []
    # hapus komen """ """
    for tok in Tokens:
        if tok[0] == '"':
            state = dfa(trans_table, 'start',tok)
            if state == 'akomen' :
                StartKomen2 = not StartKomen2
            elif state in wrong_string_state:
                print("fail comments")
                break
            else:
                newTokens.append(tok)
            continue

        if StartKomen2 == False :
            newTokens.append(tok)

    Tokens = []
    for tok in newTokens:
        if tok[0] == "'":
            state = dfa(trans_table, 'start',tok)
            if state == 'akomen' :
                StartKomen1 = not StartKomen1
            elif state in wrong_string_state :
                print("fail comments")
                break
            else:
                Tokens.append(tok)
            continue

        if StartKomen1 == False :
            Tokens.append(tok)
    #print(Tokens)
    if StartKomen2 == True or StartKomen1 == True:
        print("fail comments")

    # Delete komen #
    StartHash = False
    newTokens = []
    for tok in Tokens:
        if tok == "#":
            StartHash = True
        elif tok == "\\n":
            StartHash = False
            continue
        if StartHash == False :
            newTokens.append(tok)
    #print(newTokens)

    Tokens = []
    StartStr2 = False
    for tok in newTokens:
        if tok == '"' :
            if StartStr2 == False:
                newStr = '"'
            else :
                newStr += '"'
                Tokens.append(newStr)
            StartStr2 = not StartStr2
            continue
        if StartStr2 == False :
            Tokens.append(tok)
        else:
            newStr += tok

    #print(Tokens)
    newTokens = []
    StartStr1 = False
    for tok in Tokens:
        if tok == "'" :
            if StartStr1 == False:
                newStr = '"'
            else :
                newStr += '"'
                newTokens.append(newStr)
            StartStr1 = not StartStr1
            continue
        if StartStr1 == False :
            newTokens.append(tok)
        else:
            newStr += tok
    #print(newTokens)

    if StartStr1 == True or StartStr2 == True :
        print("fail string")

    variables = []
    strings = []
    for tok in newTokens :
        if tok[0] == "'" or tok[0] == '"':
            variables.append(tok)
        else:
            if dfa(trans_table,'start', tok) == 'buang' and not (tok in keyword.kwlist) and not (tok in valid_symbols):
                print(tok + " wrong variables")
                break
            else :
                if not(tok in valid_symbols) and not(tok in keyword.kwlist):
                    variables.append(tok)
    print(variables)
    print(newTokens)
