def make_album(name, title):
    """Return artist name and album name as a dictionary"""
    album = {name: title}
    return album

while True:
    print("\nEnter a band and album. Press q to quit.")
    name = input('Band: ')
    if name == 'q':
        break
    title = input('Album: ')
    if title == 'q':
        break
    music = make_album(name, title)
    print(music)
