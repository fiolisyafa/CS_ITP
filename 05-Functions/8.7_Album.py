def make_album(name, title, tracks=''):
    """Return artist name and album name as a dictionary"""
    if tracks:
        album = {
            'Group': name,
            'Album name': title,
            'Number of tracks': int(tracks),
        }
    else:
        album = {name: title}
    return album

mcr = make_album('MCR', 'Welcome to the Black Parade')
print(mcr)
patd = make_album('P!ATD', 'Death of a Bachelor')
print(patd)
fob = make_album('FOB', 'American Beauty', 11)
print(fob)
