#traffic light
def update_light(current):
    if current == "red" : 
        return "green"
    elif current == "green" :
        return "yellow"
    else:
        return "red"

#umbrella decider
def take_umbrella(weather, rain_chance):
    if weather == 'sunny' and rain_chance > 0.50:
        return True
    elif weather == 'sunny':
        return False
    elif weather == 'cloudy' and rain_chance > 0.20:
        return True
    elif weather == 'cloudy':
        return False
    elif weather == 'rainy':
        return True
    else:
        return False

#graceful addition
def my_add(a, b):
    try:
        return a + b
    except TypeError:
        return None

#red and bumpy
def color_probability(color, texture):
    if color == 'red' and texture == 'bumpy':
        return '0.57'
    elif color == 'yellow' and texture == 'bumpy':
        return '0.28'
    elif color == 'green' and texture == 'bumpy':
        return '0.14'
    else:
        return '0.33'

#hacking p-hackers
def categorize_study(p_value, requirements):
    if requirements == 6:
        bs = 1 * p_value
    elif requirements == 5:
        bs = 2 * p_value
    elif requirements == 4:
        bs = 4 * p_value
    elif requirements == 3:
        bs = 8 * p_value
    elif requirements == 2:
        bs = 16 * p_value
    elif requirements == 1:
        bs = 32 * p_value
    else:
        bs = 64 * p_value
        if bs <= 0.15:
            return "Needs review"
        else:
            return "Pants on fire"                         
    if bs < 0.05:
        return "Fine"
    elif bs >= 0.15:
        return "Pants on fire"
    else:
        return "Needs review"