#order
def fillable(stock, merch, n):
    if merch not in stock:
        return False
    elif stock[merch] >= n:
        return True
    else: 
        return False
#user contacts
def user_contacts(data):
    my_dict = {}
    for n in data:
        if len(n) == 1:
            my_dict[n[0]] = None
        else:
            my_dict[n[0]] = n[1]
    return my_dict   


#Multiple modes
def modes(data):
    mult_modes = {}
    l = len(data)
    i = 0
    while i < l:
        mult_modes[data[i]] = 0
        i += 1
    x = mult_modes.keys()
    lx = len(x)
    for n in data:
        mult_modes[n] += 1
    mode1 = [key for m in [max(mult_modes.values())] for key,val in mult_modes.items() if val == m]
    mode1.sort()
    lxl = len(mode1)
    if lx == lxl:
        return []
    else:
        return mode1 


#user contacts - with executable script
def user_contacts(data):
    my_dict = {}
    for n in data:
        if len(n) == 1:
            my_dict[n[0]] = None
        else:
            my_dict[n[0]] = n[1]
    return my_dict   

if __name__ == "__main__":
    a = user_contacts([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]])
    print(a)
