def make_album(artist, title, tracks=0):
    """A dictionary describing about a music album."""
    album_dict =  {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('kao denero', 'class in session')
print(album)

album = make_album('kaligraph jones', 'yes bana')
print(album)

album = make_album('sarkodie', 'azonto fiesta')
print(album)

album = make_album('m.i abaga', 'black bill gates', tracks=8)
print(album)
