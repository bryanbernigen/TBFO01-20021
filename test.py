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
'''

# Rules of the grammar
R = {
    # STARTSTATE=================================================================================
    # STARTSTATE
    "START": [["TITIK", "SS"], ["TITIK", "S"]],
    "TITIK": [["."]],

    # harus bisa mangil semua state
    "SS":	[["IMPORTSTATE", "SS"], ["IMPORTSTATE", "S"],
           ["IFSTATE", "SS"], ["IFSTATE", "S"],
           ["CONDITIONALSTATE", "SS"], ["CONDITIONALSTATE", "S"],
           ["NOTSTATE", "SS"], ["NOTSTATE", "S"],
           ["ASSIGNSTATE", "SS"], ["ASSIGNSTATE", "S"],
           ["ASSIGNMENTNOTUPLESTATE", "SS"], ["ASSIGNMENTNOTUPLESTATE", "S"],
           ["RANGESTATE", "SS"], ["RANGESTATE", "S"],
           ["FORSTATE", "SS"], ["FORSTATE", "S"],
           ["WHILESTATE", "SS"], ["WHILESTATE", "S"],
           ["b"]],
    "S":
    # IFSTATE
    [["IFCON2", "SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"], ["IFCON2", "SELSE"],
     # IMPORTSTATE
     ["FROM_IMP", "AS"], ["IMPORT", "AS"], [
         "FROM", "IMPORT"], ["I_IMPORT", "VAR"],
     # CONDITIONALSTATE
     ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONALSTATE", "OPERATORCONDITIONAL"], ["LOGICOPERATORCONDITIONAL", "CONDITIONALSTATE"], [
        "0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"], ["TITIK", "FLOAT"],
     # NOTSTATE
     ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"],
     # ASSIGNSTATE
     ["VARNGULANGASSIGNMENT", "CONDITIONALNGULANG"],
     # ASSIGNMENTNOTUPLESTATE
     ["VARMULTIOP", "CONDITIONALSTATE"],
     # RANGE
     ["R_RANGEKURUNGKIRI", "ISIRANGEKURUNGKANAN"],
     # FORSTATE
     ["F_FORVARI_IN", "VART2"], ["F_FORVARI_IN", "NUMBERT2"], [
         "F_FORVARI_IN", "RANGESTATET2"],
     # WHILESTATE
     ["W_WHILE", "CON2"], ["W_WHILE", "RANGESTATET2"],
     ["b"]],

    # ASSIGMENT STATE=============================================================================
    "ASSIGNSTATE": [["VARNGULANGASSIGNMENT", "CONDITIONALNGULANG"]],
    "VARNGULANGASSIGNMENT": [["VARNGULANG", "SAMADENGAN"]],
    "VARNGULANG": [["VARKOMA", "VAR"], ["numpy"], ["np"]],
    "VARKOMA": [["VAR", "KOMA"]],
    "CONDITIONALNGULANG": [["CONDITIONALSTATEKOMA", "CONDITIONALSTATE"], ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "CONDITIONALSTATEKOMA": [["CONDITIONALSTATE", "KOMA"]],

    # ASSIGNMENT NOTUPLE===========================================================================
    "ASSIGNMENTNOTUPLESTATE": [["VARMULTIOP", "CONDITIONALSTATE"]],
    "VARMULTIOP": [["VAR", "MULTIOP"]],


    # CONDITIONAL=================================================================================
    "CONDITIONALSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "CONDITIONAL": [["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "OPERATORCONDITIONAL": [["OPERATOR", "CONDITIONAL"]],
    "LOGICOPERATORCONDITIONAL": [["LOGICOPERATOR", "CONDITIONALSTATE"]],
    "KURUNGKIRICONDITIONAL": [["KURUNGKIRI", "CONDITIONAL"]],

    # FORSTATE=====================================================================================
    "FORSTATE": [["F_FORVARI_IN", "VART2"], ["F_FORVARI_IN", "NUMBERT2"], ["F_FORVARI_IN", "RANGESTATET2"]],
    "F_FOR": [["for"]],
    "F_FORVAR": [["F_FOR", "VAR"]],
    "I_IN": [["in"]],
    "F_FORVARI_IN": [["F_FORVAR", "I_IN"]],
    "VART2": [["VAR", "T2"]],
    "NUMBERT2": [["NUMBER", "T2"]],
    "RANGESTATET2": [["RANGESTATE", "T2"]],

    # periIFan====================================================================================
    "IFSTATE": [["IFCON2", "SELIF"], ["IFCON2", "SS"], ["IFCON2", "S"], ["IFCON2", "SELSE"]],
    "ELIF": [["E_ELIFCON2", "SELIF"], ["E_ELIFCON2", "SELSE"], ["E_ELIFCON2", "SS"], ["E_ELIFCON2", "S"]],
    "ELSE": [["E_ELSE", "T2SS"]],
    "IFCON2": [["I_IF", "CON2"]],
    "CON2": [["CONDITIONALSTATE", "T2"]],
    "SELIF": [["SS", "ELIF"], ["S", "ELIF"]],
    "SELSE": [["SS", "ELSE"], ["S", "ELSE"]],
    "T2SS": [["T2", "SS"], ["T2", "S"]],
    "E_ELIFCON2": [["E_ELIF", "CON2"]],
    "I_IF": [["if"]],
    "E_ELSE": [["else"]],
    "E_ELIF": [["elif"]],


    # importing===================================================================================
    "IMPORTSTATE": [["FROM_IMP", "AS"], ["IMPORT", "AS"], ["FROM", "IMPORT"], ["I_IMPORT", "VAR"]],
    "FROM_IMP": [["FROM", "IMPORT"]],
    "AS": [["A_AS", "VAR"]],
    "FROM": [["F_FROM", "VAR"]],
    "IMPORT": [["I_IMPORT", "VAR"]],
    "A_AS": [["as"]],
    "F_FROM": [["from"]],
    "I_IMPORT": [["import"]],

    # RANGE========================================================================================
    "RANGESTATE": [["R_RANGEKURUNGKIRI", "ISIRANGEKURUNGKANAN"]],
    "R_RANGEKURUNGKIRI": [["R_RANGE", "KURUNGKIRI"]],
    "ISIRANGEKURUNGKANAN": [["ISIRANGE", "KURUNGKANAN"]],
    "R_RANGE": [["range"]],
    "ISIRANGE": [["CONDITIONALSTATE", "NGULANGISIRANGE"], ["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "NGULANGISIRANGE": [["KOMA", "ISIRANGE"]],

    # NOTSTATE=====================================================================================
    "NOTSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"]],
    "NOTSESUATU": [["NOT", "CONDITIONALSTATE"]],
    "KURUNGKIRINOT": [["KURUNGKIRI", "NOTSESUATU"]],

    # variabel====================================================================================
    "VAR": [["numpy"], ["np"]],
    "OPERATOR": [["+"], ["-"], ["*"], ["/"], ["%"], ["**"], ["//"], [">>"], ["<<"]],
    "LOGICOPERATOR": [["=="], ["!="], ["<"], ["<="], [">"], [">="], ["is"], ["and"], ["or"]],
    "MULTIOP": [["+="], ["-="], ["*="], ["/="], ["%="], ["//="], ["**="], ["&="], ["|="], ["^="], [">>="], ["<<="]],
    "NOT": [["not"], ["!"]],
    "KURUNGKIRI": [["("]],
    "KURUNGKANAN": [[")"]],
    "KOMA": [[","]],
    "SAMADENGAN": [["="]],
    "T2": [[":"]],

    # NUMBER========================================================================================
    "NUMBER": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"]],
    "BOL": [["True"], ["False"]],

    # WHILE============================================================================================
    "WHILESTATE" : [["W_WHILE", "CON2"], ["W_WHILE", "RANGESTATET2"]],
    "W_WHILE" : [["while"]],
}

# Function to perform the CYK Algorithm

# tokens -> untuk diperiksa CYK, variables diappend ke CNF
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
        print("True")
    else:
        print("False")

# Driver Code


# Given string
a = input()
b = ". "
b += a
w = b.split()

# Function Call
cykParse(w)
