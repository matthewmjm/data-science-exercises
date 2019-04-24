#Hello World
def hello(name):
    return('Hello, ' + name)

#Quotable
def quotable(name, quote):
    return name + ' said: \"' + quote + '\"'

#Repeater
def repeater(string, n):
    return string * n

#Repeater, level 2
def repeater(string, n):
      return '\"' + string + '\"' + ' repeated ' + str(n) + ' times is: \"' + (string * n) + '\"'

#Jedi name
def greet_jedi(first, last):
    return "Greetings, master " + last[0:3].capitalize() + first[0:2].capitalize() + ""

#Areacode extractor
def area_code(message):
    ac_start = message.find("(")
    ac_end = message.find(")")
    return message[ac_start+1:ac_end]

#Poem formatter
def format_poem(poem):
    lst = poem.split('. ')
    s = ".\n"
    return  s.join(lst)