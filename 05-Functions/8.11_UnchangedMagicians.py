magicians = ['harry houdini', 'david copperfield', 'david blake', 'criss angel',]


def make_great(magicians):
    great = []
    for magician in magicians:
        magician = 'The Great' + ' ' + magician.title()
        great.append(magician)
    print(great)

def show_magicians(magicians):
    for magician in magicians:
        magician = magician.title()
        print(magician)

make_great(magicians[:])
show_magicians(magicians)
