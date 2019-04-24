#Romer temperature
def celsius_to_romer(temp):
    #C × ​21⁄40 + 7.5
    return temp * (21/40) + 7.5

#Pixelart Planning
def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0

#Blue and Red Marbles
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start+red_start-blue_pulled-red_pulled)

#Congo Pizza
def box_capacity(length, width, height):
    return (length * 12 // 16) * (width * 12 // 16) * (height * 12 // 16)

#Quadratic formula
def quadratic_formula(a, b, c):
    
    root1 = (-b + ((b**2 - 4*a*c)**.5))/(2*a)
    
    root2 = (-b - ((b**2 - 4*a*c)**.5))/(2*a)
    
    return [root1, root2]




