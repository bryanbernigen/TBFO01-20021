import keyword

trans_table = {
    'start':{'a' : 'buang', 'h' : 'var', 'o' : 'buang', 'k' : 'awalstr', 't' : 'last_titik'},
    'last_titik':{'a' : 'buang', 'h' : 'var', 'o' : 'buang', 'k' : 'buang', 't' : 'buang'},
    'var':{'a' : 'var', 'h' : 'var', 'o' : 'buang','k' : 'buang', 't' : 'last_titik'},
    'buang':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'buang' , 't' : 'buang'},
    'awalstr':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x2', 't' : 'buang' },
    'str6x2':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'akomen', 't' : 'buang' },
    'akomen':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr4', 't' : 'buang' },
    'failstr4':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr5', 't' : 'buang' },
    'failstr5':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x', 't' : 'buang' },
    'str6x':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'failstr7' , 't' : 'buang'},
    'failstr7':{'a' : 'buang', 'h' : 'buang', 'o' : 'buang','k' : 'str6x2', 't' : 'buang' }
}

trans_angka = {
    'start' : {'a' : '0koma', 'h' : 'buang', 'o' : 'buang', 'k' : 'buang', 't' : '1koma'},
    '0koma' : {'a' : '0koma', 'h' : 'buang', 'o' : 'buang', 'k' : 'buang', 't' : '1koma'},
    '1koma' : {'a' : '1koma', 'h' : 'buang', 'o' : 'buang', 'k' : 'buang', 't' : 'buang'},
    'buang' : {'a' : 'buang', 'h' : 'buang', 'o' : 'buang', 'k' : 'buang', 't' : 'buang'},
}

wrong_string_state = ['buang', 'failstr4', 'failstr5', 'failstr7']
valid_symbols = ['\\',',','+','-','*','/','//','%', '**','=','+=','-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=','>>=','<<=','==','!=', '>','<', '>=','<=','&','|','^','~','<<','>>',':','(',')','[',']','{','}']
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
        elif asc == 46:
            tok = 't'
        else:
            tok = 'o'
        state = transitions[state][tok]
    return state

def readtokens(fname):
    with open(fname,'r') as f:
        lines = f.readlines()
        words = ""
        brack = ['[',']', '(', ')', ',', "#", '{', '}', ':', '~']
        ops = ['/', '*', '+', '-', '=', '|', '&', '<', '>', '!','\\']
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

        StartHash = False
        newTokens = []
        line_counter = []
        line = 1
        for tok in Tokens:
            if tok == "#":
                StartHash = True
            elif tok == "\\n":
                StartHash = False
                line += 1
            if StartHash == False :
                newTokens.append(tok)
                line_counter.append(line)


        #print(newTokens)

        #print(Tokens)
        StartKomen2 = False
        StartKomen1 = False
        Tokens = []
        # hapus komen """ """
        idx = -1
        for tok in newTokens:
            idx+=1
            if tok[0] == '"':
                state = dfa(trans_table, 'start',tok)
                if state == 'akomen' :
                    StartKomen2 = not StartKomen2
                    del line_counter[idx]
                    idx -= 1
                elif state in wrong_string_state:
                    print("SyntaxError: EOF while scanning triple-quoted string literal")
                    return False, [], [], []
                    break
                else:
                    Tokens.append(tok)
                continue

            if StartKomen2 == False :
                Tokens.append(tok)
            else:
                del line_counter[idx]
                idx-=1

        newTokens = []
        idx = -1
        for tok in Tokens:
            idx+=1
            if tok[0] == "'":
                state = dfa(trans_table, 'start',tok)
                if state == 'akomen' :
                    StartKomen1 = not StartKomen1
                    del line_counter[idx]
                    idx -=1
                elif state in wrong_string_state :
                    print("SyntaxError: EOF while scanning triple-quoted string literal")
                    return False, [], [], []
                    break
                else:
                    newTokens.append(tok)
                continue
            if StartKomen1 == False :
                newTokens.append(tok)
            else :
                del line_counter[idx]
                idx -= 1
        #print(Tokens)
        if StartKomen2 == True or StartKomen1 == True:
            print("SyntaxError: EOF while scanning triple-quoted string literal in line " + str(line_counter[-1]))
            return False, [], [], []

        Tokens = []
        StartStr2 = False
        idxstart = 0
        idxlast = 0
        idx = -1
        for tok in newTokens:
            idx += 1
            if tok == '"' :
                if StartStr2 == False:
                    newStr = '"'
                    idxstart = idx
                else :
                    newStr += '"'
                    idxlast = idx
                    del line_counter[idxstart:idxlast]
                    Tokens.append(newStr)
                StartStr2 = not StartStr2
                continue
            if StartStr2 == False :
                Tokens.append(tok)
            else:
                if tok == "\\n" :
                    print("SyntaxError: EOL while scanning string literal in line "+ str(line_counter[idxstart]))
                    return False, [], [], []
                else :
                    newStr += tok

        newTokens = []
        StartStr1 = False
        idxstart = 0
        idxlast = 0
        idx = -1
        for tok in Tokens:
            idx +=1
            if tok == "'" :
                if StartStr1 == False:
                    newStr = '"'
                    idxstart = idx
                else :
                    newStr += '"'
                    idxlast = idx
                    del line_counter[idxstart:idxlast]
                    idx -= idxlast-idxstart
                    newTokens.append(newStr)
                StartStr1 = not StartStr1
                continue
            if StartStr1 == False :
                if tok == "\\n" :
                    del line_counter[idx]
                    idx -= 1
                    continue
                else :
                    newTokens.append(tok)
            else:
                if tok == "\\n" :
                    print("SyntaxError: EOL while scanning string literal in line "+ str(line_counter[idxstart]))
                    return False, [], [], []
                else :
                    newStr += tok

        if StartStr1 == True or StartStr2 == True :
            print("SyntaxError: EOL while scanning string literal")
            return False, [], [], []

        variables = []
        numbers = []
        fail_states = ["buang","failstr7", "failstr4", "failstr5","last_titik"]
        idx = -1
        for tok in newTokens :
            idx +=1
            if tok[0] == "'" or tok[0] == '"':
                variables.append(tok)
            else:
                f_angka = dfa(trans_angka,'start', tok)
                f_state = dfa(trans_table,'start', tok)
                if (f_state in fail_states) and not (tok in valid_symbols) and f_angka == 'buang':
                    print(tok)
                    print("SyntaxError: invalid syntax in line " + str(line_counter[idx]))
                    return False, [], [], []
                    break
                else :
                    if not(tok in valid_symbols) and not(tok in keyword.kwlist) and not(f_angka == '0koma' or f_angka == '1koma'):
                        variables.append(tok)
                    elif not(tok in valid_symbols) and not(tok in keyword.kwlist):
                        numbers.append(tok)
        variables = list(set(variables))
        numbers = list(set(numbers))
        return True, newTokens, variables, numbers
