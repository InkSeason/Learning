def make_album(name, album, songs = None):
    if songs:
        album_info = {"name": name, "album": album,}
    else:
        album_info = {"name": name, "album": album, "songs": songs}
    return album_info

active = True
while active:
    print("\nPlease tell me your favorite album.")
    print("Enter 'q' at any time to quit.")

    name = input("Artist name: ")
    if name == 'q':
        active = False
        break
    album = input("Album name: ")
    if album == 'q':
        active = False
        break
    songs = input("Number of songs: ")
    if songs == 'q':
        active = False
        break
    album_info = make_album(name, album, songs)
    print(album_info)
