#Longest word
def longest(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)

#Grade calculator
def calculate_grade(scores):
    total = 0
    for score in scores:
        total += score
    mean = total / len(scores)
    
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 60:
        return "D"
    else:
        return "F"

#Lists of lists
def process_data(data):
    store = []
    for a,b in data:
        store.append(a-b)
    x = len(store)
    total = 1 
    i = 0
    while i < x:
        total = total * store[i]
        i += 1
    return total

#Inverse slicer
def inverse_slice(items, a, b):
    r = []
    i = 0
    while i < len(items):
        if i < a:
            r.append(items[i])
            i += 1
        elif i >= b:
            r.append(items[i])
            i += 1
        else:
            i += 1
    return r
        
