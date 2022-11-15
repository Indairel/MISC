import random
from sty import fg

def gen_RGB():
    blue = random.randint(0, 256)
    green = random.randint(0, 256)
    red = random.randint(0, 256)
    return blue, green, red

def gen_Color(blue, green, red):
    return fg(blue, green, red)

blue, green, red = gen_RGB()
color = gen_Color(blue, green, red)
print(color, "This is a random text with a different font color")
print(gen_RGB())
