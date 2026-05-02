def make_album(name, album, songs = None):
    if songs:
        album_info = {"name": name, "album": album,}
    else:
        album_info = {"name": name, "album": album, "songs": songs}
    return album_info