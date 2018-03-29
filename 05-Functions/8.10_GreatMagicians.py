magicians = ['harry houdini', 'david copperfield', 'david blake', 'criss angel',]


def show_magicians(magicians):
    for magician in magicians:
        magician = magician.title()
        print(magician)

show_magicians(magicians)

def make_great(magicians):
    great = []
    while magicians:
        magician = magicians.pop()
        magician = "The Great " + magician.title()
        great.append(magician)
        print(magicians)

make_great(show_magicians[:])
