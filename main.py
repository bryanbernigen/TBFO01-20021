#import token reader
from tokenreader import readtokens

# Python implementation for the
# CYK Algorithm

# Non-terminal symbols
non_terminals = []
terminals = [":", "(", ")", "as", "else", "elif",
             "from", "if", "import", "not"]
'''
yang di append : num / var
yang berubah:
1. S di bagian conditional state
2. conditional state
3. conditional ngulang
4. conditional
5. varngulang
6. ISIRANGE <-- VAR sama NUM
7. ISIFUNC diisi VARONLY
8. SS DAN S DITAMBAHIN VAR DAN NUMM
9. VARNOTITIK
'''

# Rules of the grammar
R = {
    # STARTSTATE=================================================================================
    # STARTSTATE
    "START": [["TITIK", "SS"], ["TITIK", "S"]],
    "TITIK": [["."]],

    # harus bisa mangil semua state
    "SS":[
           ["ASSIGNSTATE", "SS"], ["ASSIGNSTATE", "S"],
           ["ASSIGNMENTNOTUPLESTATE", "SS"], ["ASSIGNMENTNOTUPLESTATE", "S"],
           ["CONDITIONALSTATE", "SS"], ["CONDITIONALSTATE", "S"],
           ["CLASSSTATE","SS"],["CLASSSTATE","S"], 
           ["DEFSTATE", "SS"], ["DEFSTATE", "S"],
           ["FORSTATE", "SS"], ["FORSTATE", "S"],
           ["FUNCSTATE", "SS"], ["FUNCSTATE", "S"],
           ["IFSTATE", "SS"], ["IFSTATE", "S"],
           ["IMPORTSTATE", "SS"], ["IMPORTSTATE", "S"],
           ["NOTSTATE", "SS"], ["NOTSTATE", "S"],
           ["RANGESTATE", "SS"], ["RANGESTATE", "S"],
           ["WHILESTATE", "SS"], ["WHILESTATE", "S"],
           ["WITHSTATE", "SS"], ["WITHSTATE", "S"],
           ["pass"], ["raise"], ["SS", "SS"],
           ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"],["NEGASI","VAR"],
           ["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
           
    "S":
    [
     # ASSIGNSTATE
     ["VARNGULANGASSIGNMENT", "CONDITIONALNGULANG"],
     # ASSIGNMENTNOTUPLESTATE
     ["VARMULTIOP", "CONDITIONALSTATE"],
     # CLASSSTATE
     ["C_CLASS","VARNOTITIKT2"],
     # CONDITIONALSTATE
     ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"],["numpy"], ["np"], ["True"], ["False"], ["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"],
     # DEFSTATE
     ["HEADERDEF","RETURNULANG"],["HEADERDEF","SS"],["HEADERDER","S"],["D_DEF", "FUNCT2"],
     # FORSTATE
     ["HEADERFOR","BREAKULANG"],["HEADERFOR","SS"],["HEADERFOR","S"],["F_FORVARNOFUNCI_IN", "CON2"], ["F_FORVARNOFUNCI_IN", "RANGESTATET2"],
     # FUNCSTATE
     ["VARONLYKURKI", "CONKOMAKURKAN"],
     # IFSTATE
     ["IFCON2", "SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"],["IFCON2","ELIF"],["IFCON2","ELSE"], ["IFCON2", "SELSE"],["I_IF", "CON2"],
     # IMPORTSTATE
     ["FROM_IMP", "AS"], ["IMPORT", "AS"], ["FROM", "IMPORT"], ["I_IMPORT", "VARNOFUNC"],
     # NOTSTATE
     ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"],
     # RANGE
     ["R_RANGEKURUNGKIRI", "ISIRANGEKURUNGKANAN"], ["R_RANGEKURUNGKIRI", "KURUNGKANAN"],
     # WHILESTATE
     ["HEADERWHILE","BREAKULANG"],["HEADERWHILE","SS"],["HEADERWHILE","S"],["W_WHILE", "CON2"], ["W_WHILE", "RANGESTATET2"],["WHILEVARIN","RANGESTATET2"],
     # WITHSTATE
     ["W_WITH", "VART2"], ["WITH", "ASNOFUNCT2"],
     #VAR
     ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"],["NEGASI","VAR"],
     #NUMBERS
     ["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"],["pass"]],


    # ASSIGMENT STATE=============================================================================
    "ASSIGNSTATE": [["VARNGULANGASSIGNMENT", "CONDITIONALNGULANG"]],
    "VARNGULANGASSIGNMENT": [["VARNGULANG", "SAMADENGAN"]],
    "VARNGULANG": [["VARKOMA", "VARONLY"], ["numpy"], ["np"]],
    "VARKOMA": [["VARONLY", "KOMA"]],
    "CONDITIONALNGULANG": [["CONDITIONALSTATEKOMA", "CONDITIONALSTATE"], ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"], ["True"], ["False"], ["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
    "CONDITIONALSTATEKOMA": [["CONDITIONALSTATE", "KOMA"]],

    # ASSIGNMENT NOTUPLE===========================================================================
    "ASSIGNMENTNOTUPLESTATE": [["VARMULTIOP", "CONDITIONALSTATE"]],
    "VARMULTIOP": [["VAR", "MULTIOP"]],

    # CONDITIONAL=================================================================================
    "CONDITIONALSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"], ["True"], ["False"],["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
    "CONDITIONAL": [["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"], ["True"], ["False"],["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
    "OPERATORCONDITIONAL": [["OPERATOR", "CONDITIONAL"]],
    "LOGICOPERATORCONDITIONAL": [["LOGICOPERATOR", "CONDITIONALSTATE"]],
    "KURUNGKIRICONDITIONAL": [["KURUNGKIRI", "CONDITIONAL"],["KURUNGKIRI", "CONDITIONALNGULANG"]],
    "KURAWALKIRICONDITIONAL": [["KURAWALKIRI","CONDITIONAL"],["KURAWALKIRI","CONDITIONALNGULANG"]],
    "SIKUKIRICONDITIONAL":[["SIKUKIRI","CONDITIONAL"],["SIKUKIRI","CONDITIONALNGULANG"]],

    # CLASSSTATE===================================================================================
    "CLASSSTATE":[["C_CLASS","VARNOTITIKT2"]],
    "C_CLASS":[["class"]],
    "VARNOTITIKT2":[["VARNOTITIK","T2"]],

    # DEFSTATE========================================================================================
    "DEFSTATE" : [["HEADERDEF","RETURNULANG"],["HEADERDEF","SS"],["HEADERDER","S"],["D_DEF", "FUNCT2"]],
    "HEADERDEF" : [["D_DEF", "FUNCT2"],],
    "D_DEF" : [["def"]],
    "FUNCT2" : [["DEF_FUNC", "T2"]],
    "DEF_FUNC" : [["VARONLYKURKI", "ISIFUNCKANAN"], ["VARONLYKURKI", "KURUNGKANAN"]],
    "ISIFUNCKANAN" : [["ISIFUNC", "KURUNGKANAN"]],
    "ISIFUNC" : [["numpy"], ["np"], ["VARONLY", "SAMADENGANCONDITIONAL"], ["ISIFUNCKOMA", "ISIFUNC"]],
    "SAMADENGANCONDITIONAL" : [["SAMADENGAN", "CONDITIONAL"]],
    "ISIFUNCKOMA" : [["ISIFUNC", "KOMA"]],
    "RETURNULANG":[["return"], ["RETURNULANG","RETURNULANG"],["SS","RETURNULANG"],["S","RETURNULANG"],["RETURNULANG","SS"],["RETURNULANG","S"],["RETURNULANG","D_IFSTATE"],["D_IFSTATE","RETURNULANG"],["D_IFSTATE","SS"],["D_IFSTATE","S"],["SS","D_IFSTATE"],["S","D_IFSTATE"]],

    # FORSTATE=====================================================================================
    "FORSTATE" : [["HEADERFOR","BREAKULANG"],["HEADERFOR","SS"],["HEADERFOR","S"],["F_FORVARNOFUNCI_IN", "CON2"], ["F_FORVARNOFUNCI_IN", "RANGESTATET2"]],
    "HEADERFOR": [["F_FORVARNOFUNCI_IN", "CON2"], ["F_FORVARNOFUNCI_IN", "RANGESTATET2"]],
    "F_FOR": [["for"]],
    "F_FORVARNOFUNC": [["F_FOR", "VARNOFUNC"]],
    "I_IN": [["in"]],
    "F_FORVARNOFUNCI_IN": [["F_FORVARNOFUNC", "I_IN"]],
    "VART2": [["VAR", "T2"]],
    "NUMBERT2": [["NUMBER", "T2"]],
    "RANGESTATET2": [["RANGESTATE", "T2"]],

    # FUNCTIONSTATE===========================================================================================
    "FUNCSTATE" : [["VARONLYKURKI", "CONKOMAKURKAN"]],
    "CONKOMA" : [["CONSTATEKOMA", "CONKOMA"], ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"], ["True"], ["False"],["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
    "CONSTATEKOMA" : [["CONDITIONALSTATE", "KOMA"]],
    "VARONLYKURKI" : [["VARONLY", "KURUNGKIRI"]],
    "CONKOMAKURKAN" : [["CONKOMA", "KURUNGKANAN"],[")"]],

    # IFSTATE====================================================================================
    "IFSTATE": [["IFCON2", "SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"],["IFCON2","ELIF"],["IFCON2","ELSE"], ["IFCON2", "SELSE"],["I_IF", "CON2"]],
    "ELIF": [["E_ELIFCON2", "SELIF"], ["E_ELIFCON2", "SELSE"], ["E_ELIFCON2", "ELIF"],["E_ELIFCON2", "SS"],["E_ELIFCON2", "ELSE"], ["E_ELIFCON2", "S"],["E_ELIF", "CON2"]],
    "ELSE": [["E_ELSE", "T2SS"],["E_ELSE","T2"]],
    "IFCON2": [["I_IF", "CON2"]],
    "CON2": [["CONDITIONALSTATE", "T2"]],
    "SELIF": [["SS", "ELIF"], ["S", "ELIF"]],
    "SELSE": [["SS", "ELSE"], ["S", "ELSE"]],
    "T2SS": [["T2", "SS"], ["T2", "S"]],
    "E_ELIFCON2": [["E_ELIF", "CON2"]],
    "I_IF": [["if"]],
    "E_ELSE": [["else"]],
    "E_ELIF": [["elif"]],


    #L_IFSTATE===================================================================================
    "L_IFSTATE": [["IFCON2", "L_SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"],["IFCON2","BREAKULANG"],["IFCON2","BREAKULANGL_ELSE"],["IFCON2","BREAKULANGL_ELIF"],["IFCON2","L_ELIF"],["IFCON2","L_ELSE"], ["IFCON2", "L_SELSE"],["I_IF", "CON2"]],
    "L_ELIF": [["L_E_ELIFCON2", "L_SELIF"], ["L_E_ELIFCON2", "L_SELSE"],["BREAKULANGL_ELIF","L_ELIF"],["L_E_ELIFCON2","BREAKULANGL_ELSE"], ["L_E_ELIFCON2", "L_ELIF"],["L_E_ELIFCON2", "SS"],["L_E_ELIFCON2", "L_ELSE"], ["L_E_ELIFCON2", "S"],["L_E_ELIFCON2","BREAKULANG"],["L_E_ELIF", "CON2"]],
    "L_ELSE": [["L_E_ELSE", "L_T2SS"],["L_E_ELSE","T2"]],
    "L_SELIF": [["SS", "L_ELIF"], ["S", "L_ELIF"],["BREAKULANG","L_ELIF"]],
    "L_SELSE": [["SS", "L_ELSE"], ["S", "L_ELSE"],["BREAKULANG","L_ELSE"]],
    "L_T2SS": [["T2", "SS"], ["T2", "S"], ["T2","BREAKULANG"]],
    "L_E_ELIFCON2": [["L_E_ELIF", "CON2"]],
    "L_I_IF": [["if"]],
    "L_E_ELSE": [["else"]],
    "L_E_ELIF": [["elif"]],
    "BREAKULANGL_ELIF": [["BREAKULANG","L_ELIF"]],
    "BREAKULANGL_ELSE":[["BREAKULANG","L_ELSE"]],

    #D_IFSTATE===================================================================================
    "D_IFSTATE": [["IFCON2", "D_SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"],["IFCON2","RETURNULANG"],["IFCON2","RETURNULANGL_ELSE"],["IFCON2","RETURNULANGL_ELIF"],["IFCON2","D_ELIF"],["IFCON2","D_ELSE"], ["IFCON2", "D_SELSE"],["I_IF", "CON2"]],
    "D_ELIF": [["D_E_ELIFCON2", "D_SELIF"], ["D_E_ELIFCON2", "D_SELSE"],["RETURNULANGL_ELIF","D_ELIF"],["D_E_ELIFCON2","RETURNULANGL_ELSE"], ["D_E_ELIFCON2", "D_ELIF"],["D_E_ELIFCON2", "SS"],["D_E_ELIFCON2", "D_ELSE"], ["D_E_ELIFCON2", "S"],["D_E_ELIFCON2","RETURNULANG"],["D_E_ELIF", "CON2"]],
    "D_ELSE": [["D_E_ELSE", "D_T2SS"],["D_E_ELSE","T2"]],
    "D_SELIF": [["SS", "D_ELIF"], ["S", "D_ELIF"],["RETURNULANG","D_ELIF"]],
    "D_SELSE": [["SS", "D_ELSE"], ["S", "D_ELSE"],["RETURNULANG","D_ELSE"]],
    "D_T2SS": [["T2", "SS"], ["T2", "S"], ["T2","RETURNULANG"]],
    "D_E_ELIFCON2": [["D_E_ELIF", "CON2"]],
    "D_I_IF": [["if"]],
    "D_E_ELSE": [["else"]],
    "D_E_ELIF": [["elif"]],
    "RETURNULANGL_ELIF": [["RETURNULANG","D_ELIF"]],
    "RETURNULANGL_ELSE":[["RETURNULANG","D_ELSE"]],

    # IMPORTSTATE===================================================================================
    "IMPORTSTATE": [["FROM_IMP", "AS"], ["IMPORT", "AS"], ["FROM", "IMPORT"], ["I_IMPORT", "VARNOFUNC"]],
    "FROM_IMP": [["FROM", "IMPORT"]],
    "AS": [["A_AS", "VARONLY"]],
    "FROM": [["F_FROM", "VARNOFUNC"]],
    "IMPORT": [["I_IMPORT", "VARONLY"]],
    "A_AS": [["as"]],
    "F_FROM": [["from"]],
    "I_IMPORT": [["import"]],

    # NOTSTATE=====================================================================================
    "NOTSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"]],
    "NOTSESUATU": [["NOT", "CONDITIONALSTATE"]],
    "KURUNGKIRINOT": [["KURUNGKIRI", "NOTSESUATU"]],

    # RANGE========================================================================================
    "RANGESTATE": [["R_RANGEKURUNGKIRI", "ISIRANGEKURUNGKANAN"], ["R_RANGEKURUNGKIRI", "KURUNGKANAN"]],
    "R_RANGEKURUNGKIRI": [["R_RANGE", "KURUNGKIRI"]],
    "ISIRANGEKURUNGKANAN": [["ISIRANGE", "KURUNGKANAN"]],
    "R_RANGE": [["range"]],
    "ISIRANGE": [["CONDITIONALSTATE", "NGULANGISIRANGE"], ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"],["KURAWALKIRICONDITIONAL","KURAWALKANAN"],["SIKUKIRICONDITIONAL","SIKUKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["VARONLYKURKI", "CONKOMAKURKAN"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "NGULANGISIRANGE": [["KOMA", "ISIRANGE"]],

    # variabel====================================================================================
    "VAR": [["VARONLYKURKI", "CONKOMAKURKAN"],["VAR","DOTVAR"],["SIKUKIRIVARNUMBER","SIKUKANAN"],["KURAWALKIRIDICT","KURAWALKANAN"],["NEGASI","VAR"]],
    "DOTVAR":[["NEGASI","DOTVAR"],["TITIK","VAR"],["DOTVAR","DOTVAR"]],
    "VARONLY" : [["NEGASI","VARONLY"]],
    "VARNOFUNC" : [["NEGASI","VARNOFUNC"], ["VARNOFUNC", "DOTVARNOFUNC"]],
    "DOTVARNOFUNC" : [["NEGASI","DOTVARNOFUNC"],["TITIK", "VARNOFUNC"], ["DOTVARNOFUNC", "DOTVARNOFUNC"]],
    "VARNOTITIK":[["VARONLYKURKI", "CONKOMAKURKAN"],["NEGASI","VARNOTITIK"]],
    "NEGASI":[["~"],["NEGASI","NEGASI"]],
    "OPERATOR": [["+"], ["-"], ["*"], ["/"], ["%"], ["**"], ["//"], [">>"], ["<<"],["&"],["|"],["^"]],
    "LOGICOPERATOR": [["=="], ["!="], ["<"], ["<="], [">"], [">="], ["is"], ["and"], ["or"], ["NOT", "I_IN"]],
    "MULTIOP": [["+="], ["-="], ["*="], ["/="], ["%="], ["//="], ["**="], ["&="], ["|="], ["^="], [">>="], ["<<="]],
    "NOT": [["not"]],
    "KURUNGKIRI": [["("]],
    "KURUNGKANAN": [[")"]],
    "SIKUKIRI":[["["]],
    "SIKUKANAN":[["]"]],
    "SIKUKIRIVARNUMBER":[["SIKUKIRI","VAR"],["SIKUKIRI","NUMBER"],["SIKUKIRI","DOUBLEVARNUMBER"]],
    "DOUBLEVARNUMBER": [["VAR","KOMAVARNUMBER"],["NUMBER","KOMAVARNUMBER"],["CONDITIONALSTATE","KOMAVARNUMBER"]],
    "KOMAVARNUMBER": [["KOMA","VAR"],["KOMA","NUMBER"],["KOMA","CONDITIONALSTATE"]],
    "KURAWALKIRI":[["{"]],
    "KURAWALKANAN":[["}"]],
    "KURAWALKIRIDICT":[["KURAWALKIRI","VART2VAR"]],
    "VART2VAR":[["VART2","VAR"],["VART2","NUMBER"],["NUMBERT2","NUMBER"],["NUMBERT2","VAR"],["VART2VAR","KOMAVART2VAR"]],
    "KOMAVART2VAR": [["KOMA","VART2VAR"],["KOMAVART2VAR","KOMAVART2VAR"]],
    "KOMA": [[","]],
    "SAMADENGAN": [["="]],
    "T2": [[":"]],

    # NUMBER========================================================================================
    "NUMBER": [["+"],["-"],["NEGASI", "NUMBER"],["NUMBER","NUMBER"]],
    "BOL": [["True"], ["False"]],

    # WHILE============================================================================================
    "WHILESTATE" : [["HEADERWHILE","BREAKULANG"],["HEADERWHILE","SS"],["HEADERWHILE","S"],["W_WHILE", "CON2"], ["W_WHILE", "RANGESTATET2"],["WHILEVARIN","RANGESTATET2"]],
    "HEADERWHILE": [["W_WHILE", "CON2"], ["W_WHILE", "RANGESTATET2"],["WHILEVARIN","RANGESTATET2"]],
    "BREAKULANG":[["break"], ["continue"],["BREAKULANG","BREAKULANG"],["SS","BREAKULANG"],["S","BREAKULANG"],["BREAKULANG","SS"],["BREAKULANG","S"],["BREAKULANG","L_IFSTATE"],["L_IFSTATE","BREAKULANG"],["L_IFSTATE","SS"],["L_IFSTATE","S"],["SS","L_IFSTATE"],["S","L_IFSTATE"]],
    "W_WHILE" : [["while"]],
    "WHILEVARIN": [["W_WHILE","VARIN"]],
    "VARIN":[["VAR","I_IN"]],

    # WITH================================================================================================
    "WITHSTATE" : [["W_WITH", "VART2"], ["WITH", "ASNOFUNCT2"]],
    "ASNOFUNCT2" : [["A_AS", "VARNOFUNCT2"]],
    "VARNOFUNCT2" : [["VARNOFUNC", "T2"]],
    "WITH" : [["W_WITH", "VAR"]],
    "W_WITH" : [["with"]],
}

# Function to perform the CYK Algorithm

# tokens -> untuk diperiksa CYK, variables diappend ke CNF
'''
berhasil, tokens,variables = readtokens()
for vars in variables :
    R["S"].append(vars)
    R["SS"].append(vars)
    R["CONDITIONALSTATE"].append(vars)
    R["CONDITIONALNGULANG"].append(vars)
    R["CONDITIONAL"].append(vars)
    R["VARNGULANG"].append(vars)
    R["ISIRANGE"].append(vars)
    R["VAR"].append(vars)
    R["NUMBER"].append(vars)
'''
def cykParse(w):
    n = len(w)

    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]

    # Filling in the table
    for j in range(0, n):

        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:

                # If a terminal is found
                if len(rhs) == 1 and \
                        rhs[0] == w[j]:
                    T[j][j].add(lhs)

        for i in range(j, -1, -1):

            # Iterate over the range i to j + 1
            for k in range(i, j + 1):

                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:

                        # If a terminal is found
                        try:
                            if len(rhs) == 2 and \
                                    rhs[0] in T[i][k] and \
                                    rhs[1] in T[k + 1][j]:
                                T[i][j].add(lhs)
                        except:
                            pass

    # If word can be formed by rules
    # of given grammar
    if len(T[0][n-1]) != 0:
        print("Accepted")
    else:
        print("Syntax Error")

# Driver Code
fname = input("Masukkan nama file yang akan ditest: ")
berhasil, tokens,variables, numbers = readtokens(fname)

if berhasil :
    splitted_tokens = ['.']
    for tok in tokens:
        if tok in variables:
            split_tokens = [y for x in tok.split('.') for y in (x, '.')]
            splitted_tokens.extend(split_tokens[:-1])
        else :
            splitted_tokens.append(tok)

    splitted_variables = []
    for vars in variables:
        splitted_variables.extend(vars.split('.'))
    splitted_variables = list(set(splitted_variables))

    to_append_variables = ["S","CONDITIONALNGULANG","CONDITIONAL","CONKOMA","CONDITIONALSTATE","VAR","VARONLY","VARNOFUNC","VARNOTITIK","ISIRANGE","SS","ISIFUNC"]
    to_append_numbers = ["S", "SS", "CONDITIONALNGULANG","CONDITIONALSTATE", "CONDITIONAL","CONKOMA","ISIRANGE","NUMBER"]

    for prod in to_append_variables:
        for var in splitted_variables :
            R[prod].append([var])
    for prod in to_append_numbers:
        for num in numbers:
            R[prod].append([num])
    print(R["SS"])
    # Function Call
    cykParse(splitted_tokens)
