# Python implementation for the
# CYK Algorithm

# Non-terminal symbols
non_terminals = []
terminals = [":", "(", ")", "as", "else", "elif",
             "from", "if", "import", "not"]

# Rules of the grammar
R = {
    # STARTSTATE=================================================================================
    # harus bisa mangil semua state
    "S":
        # ifstate
    [["IFCON2", "SELIF"], ["IFCON2", "SS"], ["IFCON2", "SELSE"],
     # importstate
     ["FROM_IMP", "AS"], ["IMPORT", "AS"], [
        "FROM", "IMPORT"], ["I_IMPORT", "VAR"],
        # CONDITIONALSTATE
        ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONALSTATE", "OPERATORCONDITIONAL"], ["LOGICOPERATORCONDITIONAL", "CONDITIONALSTATE"], [
            "0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"], ["TITIK", "FLOAT"],
     ["b"]],
    "SS":	[["IMPORTSTATE", "SS"], ["IMPORTSTATE", "S"], ["IFSTATE", "ENDSTATE"],
           ["IFSTATE", "SS"], ["IFSTATE", "S"], ["IFSTATE", "ENDSTATE"],
           ["CONDITIONALSTATE", "SS"], ["CONDITIONALSTATE", "S"], [
               "CONDITIONALSTATE", "ENDSTATE"],
           ["NOTSTATE", "SS"], ["NOTSTATE", "S"], ["NOTSTATE", "ENDSTATE"],
           ["b"]],
    "ENDSTATE": [["."]],

    # CONDITIONAL=================================================================================
    "CONDITIONALSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"], ["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"], ["TITIK", "FLOAT"]],
    "CONDITIONAL": [["KURUNGKIRICONDITIONAL", "KURUNGKANAN"], ["CONDITIONAL", "OPERATORCONDITIONAL"], ["CONDITIONAL", "LOGICOPERATORCONDITIONAL"], ["True"], ["False"], ["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"], ["TITIK", "FLOAT"]],
    "OPERATORCONDITIONAL": [["OPERATOR", "CONDITIONAL"]],
    "LOGICOPERATORCONDITIONAL": [["LOGICOPERATOR", "CONDITIONALSTATE"]],
    "KURUNGKIRICONDITIONAL": [["KURUNGKIRI", "CONDITIONAL"]],

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
    "T2": [[":"]],

    # importing===================================================================================
    "IMPORTSTATE": [["FROM_IMP", "AS"], ["IMPORT", "AS"], ["FROM", "IMPORT"], ["I_IMPORT", "VAR"]],
    "FROM_IMP": [["FROM", "IMPORT"]],
    "AS": [["A_AS", "VAR"]],
    "FROM": [["F_FROM", "VAR"]],
    "IMPORT": [["I_IMPORT", "VAR"]],
    "A_AS": [["as"]],
    "F_FROM": [["from"]],
    "I_IMPORT": [["import"]],

    # NOTSTATE=====================================================================================
    "NOTSTATE": [["KURUNGKIRINOT", "KURUNGKANAN"], ["NOT", "CONDITIONALSTATE"]],
    "NOTSESUATU": [["NOT", "CONDITIONALSTATE"]],
    "KURUNGKIRINOT": [["KURUNGKIRI", "NOTSESUATU"]],

        # TRUEORFALSESTATE==================================================================================

        # variabel====================================================================================
    "VAR": [["numpy"], ["np"]],
    "OPERATOR": [["+"], ["-"], ["*"], ["/"], ["%"], ["**"], ["//"]],
    "LOGICOPERATOR": [["=="], ["!="], ["<"], ["<="], [">"], [">="], ["is"], ["and"], ["or"]],
        "NOT": [["not"], ["!"]],
    "KURUNGKIRI": [["("]],
    "KURUNGKANAN": [[")"]],

    # NUMBER========================================================================================
    "NUMBER": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["NUMBER", "NUMBER"], ["TITIK", "FLOAT"]],
    "BOL": [["True"], ["False"]],
    "FLOAT": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], ["FLOAT", "FLOAT"]],
    "TITIK": [["."]],
}

# Function to perform the CYK Algorithm


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
a += (" .")
w = a.split()

# Function Call
cykParse(w)
