with open("test.py",'r') as f:
    lines = f.readlines()
    words = ""
    brack = ['[',']', '(', ')']
    ops = ['/', '*', '+', '-', '=']
    bef = False #Periksa ada ops sebelumnya
    for line in lines:
        for char in line:
            if char in brack :
                words += (" " +char+" ")
            elif char in ops:
                if bef == True :
                    words += (char + " ")
                else :
                    words+=(" " + char)
                    bef = True
            elif char == '\n':
                words += " "
            else :
                if bef == True:
                    words += " " + char
                    bef = False
                else : words+= char
    tokens = words.split()
print(tokens)
