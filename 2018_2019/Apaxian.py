def give_name(y, p):
    if y[-2:] == 'ex':
        return y+p
    elif y[-1] in ["a", "e","i",'o',"u"]:
        return y[:-1] + "e" + p
    else:
        return y + "ex" + p
    
# Input values as command-line arguments
y, p = input().split()

print(give_name(y, p))